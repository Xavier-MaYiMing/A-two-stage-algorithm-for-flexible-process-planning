# Feasible sequence oriented discrete particle swarm optimization (FSDPSO)
# Reference: Dou J, Li J, Su C. A discrete particle swarm optimisation for operation sequencing in CAPP[J]. International Journal of Production Research, 2018, 56(11): 3795-3814.
import copy
import numpy as np
from tqdm import tqdm


def transitive_closure(ops):
    # calculate transitive closure using the Floyd-Warshall's algorithm
    nodes = set()
    for op1_key, op1 in ops.items():
        if op1.prior:
            nodes.add(op1_key)
            for op2_key in op1.prior:
                nodes.add(op2_key)
    nodes = list(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]
    for op1_key, op1 in ops.items():
        if op1.prior:
            i = node_index[op1_key]
            for op2_key in op1.prior:
                j = node_index[op2_key]
                adj_matrix[j][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][k] and adj_matrix[k][j]:
                    adj_matrix[i][j] = 1
    closure_pairs = set()
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j]:
                closure_pairs.add((nodes[i], nodes[j]))
    return closure_pairs


def cal_objective(sol, specifications):
    # calculate the objective value
    objective = specifications['type']['objective']
    indices = specifications['indices']
    op2ind = specifications['op2ind']
    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']
    obj = 0
    ops = sol['operation']
    machines = []
    tools = []
    directions = []
    for op in ops:
        idx = op2ind[op]
        machines.append(sol['machine'][idx])
        tools.append(sol['tool'][idx])
        directions.append(sol['direction'][idx])
    for i in range(len(ops)):
        string = ops[i] + '&' + machines[i] + '&' + tools[i] + '&' + directions[i]
        obj += indices[ops[i]][string]
        if objective == 'cost':
            if i != 0:
                if machines[i] != machines[i - 1]:
                    obj += mcc
                if machines[i] != machines[i - 1] or tools[i] != tools[i - 1]:
                    obj += tcc
                if machines[i] != machines[i - 1] or directions[i] != directions[i - 1]:
                    obj += scc
        else:
            if i != 0:
                if machines[i] != machines[i - 1]:
                    obj += mct[machines[i - 1]][machines[i]]
                if machines[i] != machines[i - 1] or tools[i] != tools[i - 1]:
                    obj += tct
                if machines[i] != machines[i - 1] or directions[i] != directions[i - 1]:
                    obj += sct
    return obj


def cal_precedence(precedence):
    # calculate the precedence constraint satisfaction status
    nops_all = len(precedence)
    p = np.ones(nops_all)
    for i in range(nops_all):
        for j in range(nops_all):
            if precedence[j][i] != 0:
                p[i] = 0
                break
    return p


def initialize_population(npop, nops, precedence, specifications):
    # the initialization of operation, tool, machine, and TAD chromosomes
    operations = specifications['operations']
    ind2op = specifications['ind2op']

    pops = []
    for _ in range(npop):
        p = copy.deepcopy(precedence)
        selected_idx = []
        operation_chromosome = []
        machine_chromosome = []
        tool_chromosome = []
        direction_chromosome = []
        for i in range(nops):
            available = np.where(cal_precedence(p) == 1)[0]
            available = list(set(available) - set(selected_idx))
            op_ind = np.random.choice(available)
            p[op_ind] = 0
            op = ind2op[i]
            selected_idx.append(op_ind)
            operation_chromosome.append(ind2op[op_ind])
            machine_chromosome.append(np.random.choice(operations[op].machine))
            tool_chromosome.append(np.random.choice(operations[op].tool))
            direction_chromosome.append(np.random.choice(operations[op].direction))
        pops.append({
            'operation': operation_chromosome,
            'machine': machine_chromosome,
            'tool': tool_chromosome,
            'direction': direction_chromosome,
        })
    return pops


def fragment_crossover(sol1, sol2):
    # fragment crossover
    op1, op2 = sol1['operation'], sol2['operation']
    point1, point2 = sorted(np.random.choice(range(1, len(op1) - 1), 2, replace=False))
    temp_op = op1[point1: point2]
    idx = point1
    new_op = op1.copy()
    for i in range(len(op1)):
        if op2[i] in temp_op:
            new_op[idx] = op2[i]
            idx += 1
    new_sol = copy.deepcopy(sol1)
    new_sol['operation'] = new_op
    return new_sol


def uniform_crossover(sol1, sol2):
    # resource updating
    n = len(sol1['operation'])
    new_sol = copy.deepcopy(sol1)
    for i in range(n):
        new_sol['machine'][i] = sol2['machine'][i] if np.random.random() < 0.5 else sol1['machine'][i]
        new_sol['tool'][i] = sol2['tool'][i] if np.random.random() < 0.5 else sol1['tool'][i]
        new_sol['direction'][i] = sol2['direction'][i] if np.random.random() < 0.5 else sol1['direction'][i]
    return new_sol


def find_mutation_range(sol, closure_pairs, idx):
    # find the mutation range
    idx1, idx2 = idx, idx
    while idx1 - 1 >= 0 and (sol[idx1 - 1], sol[idx]) not in closure_pairs:
        flag = False
        for i in range(idx1, idx):
            if (sol[idx1 - 1], sol[i]) in closure_pairs:
                flag = True
                break
        if flag:
            break
        idx1 -= 1
    while idx2 + 1 < len(sol) and (sol[idx], sol[idx2 + 1]) not in closure_pairs:
        flag = False
        for i in range(idx + 1, idx2 + 1):
            if (sol[i], sol[idx2 + 1]) in closure_pairs:
                flag = True
                break
        if flag:
            break
        idx2 += 1
    return [i for i in range(idx1, idx2 + 1) if i != idx]


def fragment_mutation(parent, closure_pairs):
    # fragment mutation
    new_sol = copy.deepcopy(parent)
    chromosome = new_sol['operation']
    point1 = np.random.randint(0, len(chromosome))
    mutation_range = find_mutation_range(chromosome, closure_pairs, point1)
    while not mutation_range:
        point1 = np.random.randint(0, len(chromosome))
        mutation_range = find_mutation_range(chromosome, closure_pairs, point1)
    point2 = np.random.choice(mutation_range)
    new_sol['operation'][point1], new_sol['operation'][point2] = new_sol['operation'][point2], new_sol['operation'][point1]
    return new_sol


def uniform_mutation(sol, specifications):
    # uniform mutation
    operations = specifications['operations']
    ind2op = specifications['ind2op']

    n = len(sol['operation'])
    new_sol = copy.deepcopy(sol)
    point1, point2 = sorted(np.random.choice(range(n + 1), 2, replace=False))
    for k in range(point1, point2):
        op = ind2op[k]
        new_sol['machine'][k] = np.random.choice(operations[op].machine)
        new_sol['tool'][k] = np.random.choice(operations[op].tool)
        new_sol['direction'][k] = np.random.choice(operations[op].direction)
    return new_sol


def greedy_mutation(sol, specifications):
    # greedy mutation
    objective = specifications['type']['objective']
    operations = specifications['operations']
    op2ind = specifications['op2ind']
    if objective == 'cost':
        muc, tuc = specifications['muc'], specifications['tuc']

    n = len(sol['operation'])
    new_sol = copy.deepcopy(sol)
    point1, point2 = sorted(np.random.choice(range(n + 1), 2, replace=False))
    for k in range(point1, point2 - 1):
        op1, op2 = sol['operation'][k], sol['operation'][k + 1]
        op1_ind, op2_ind = op2ind[op1], op2ind[op2]
        if sol['machine'][op1_ind] in operations[op2].machine:
            new_sol['machine'][op2_ind] = sol['machine'][op1_ind]
        elif objective == 'cost':
            filtered_items = {index: muc[index] for index in operations[op2].machine}
            new_sol['machine'][op2_ind] = min(filtered_items, key=filtered_items.get)
        else:
            new_sol['machine'][op2_ind] = np.random.choice(operations[op2].machine)

        if new_sol['machine'][op1_ind] == new_sol['machine'][op2_ind]:
            if sol['tool'][op1_ind] in operations[op2].tool:
                new_sol['tool'][op2_ind] = sol['tool'][op1_ind]
            elif objective == 'cost':
                filtered_items = {index: tuc[index] for index in operations[op2].tool}
                new_sol['tool'][op2_ind] = min(filtered_items, key=filtered_items.get)
            else:
                new_sol['tool'][op2_ind] = np.random.choice(operations[op2].tool)

            if sol['direction'][op1_ind] in operations[op2].direction:
                new_sol['direction'][op2_ind] = sol['direction'][op1_ind]
            else:
                new_sol['direction'][op2_ind] = np.random.choice(operations[op2].direction)
    return new_sol


def main(npop, maxFE, c1, c2, w, k1, k2, specifications):
    """
    The main function.
    :param npop: population size (default = 500)
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
    :param c1: personal learning factor (default = 2)
    :param c2: global learning factor (default = 2)
    :param w: inertia weight (default = 0.9)
    :param k1: the first parameter in adaptive mutation probability (default = 0.5)
    :param k2: the second parameter in adaptive mutation probability (default = 0.005)
    :param specifications: the specifications of FPP
    :return:
    """
    operations = specifications['operations']
    op2ind = specifications['op2ind']
    if specifications['type']['alternative']:
        raise ValueError('FSDPSO cannot solve cases with alternative operations.')

    # Step 1. Initialization
    nops = len(operations)  # the number of operations
    FE = 0  # the number of function evaluations
    precedence = np.zeros((nops, nops))
    for op1 in operations:
        op1_ind = op2ind[op1]
        for op2 in operations:
            if op1 in operations[op2].prior:
                op2_ind = op2ind[op2]
                precedence[op1_ind, op2_ind] = 1
    closure_pairs = transitive_closure(operations)  # transitive closure pairs
    sols = initialize_population(npop, nops, precedence, specifications)  # solutions
    objs = [cal_objective(sol, specifications) for sol in sols]  # objectives
    pbest = objs.copy()  # the personal best
    pbest_sol = copy.deepcopy(sols)  # the personal best solutions
    FE += npop
    gbest = min(objs)  # the global best
    gbest_sol = copy.deepcopy(sols[objs.index(gbest)])  # the global best solution
    conFE = FE  # convergence function iteration

    # Step 2. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=npop) as pbar:
        while FE <= maxFE:

            for k in range(npop):
                r, r1, r2 = np.random.random(), np.random.random(), np.random.random()
                if r < w / (c1 * r1 + c2 * r2 + w):
                    new_sol = copy.deepcopy(sols[k])
                elif r < (w + c1 * r1) / (c1 * r1 + c2 * r2 + w):
                    new_sol = fragment_crossover(sols[k], pbest_sol[k])
                    new_sol = uniform_crossover(new_sol, pbest_sol[k])
                else:
                    new_sol = fragment_crossover(sols[k], gbest_sol)
                    new_sol = uniform_crossover(new_sol, gbest_sol)
                pm = k1 * (max(objs) - objs[k]) / (max(objs) - sum(objs) / len(objs)) + k2
                if np.random.random() < pm:
                    new_sol = fragment_mutation(new_sol, closure_pairs)
                if np.random.random() < pm:
                    new_sol = greedy_mutation(new_sol, specifications) if np.random.random() < 0.5 else greedy_mutation(new_sol, specifications)
                sols[k] = copy.deepcopy(new_sol)
                new_obj = cal_objective(new_sol, specifications)
                objs[k] = new_obj
                FE += 1
                pbar.update(1)
                if new_obj < pbest[k]:
                    pbest[k] = new_obj
                    pbest_sol[k] = copy.deepcopy(new_sol)
                    if new_obj < gbest:
                        gbest = new_obj
                        gbest_sol = copy.deepcopy(new_sol)
                        conFE = FE

    # Step 3. Output
    best_sol = []
    for i in range(len(gbest_sol['operation'])):
        best_sol.append(gbest_sol['operation'][i] + '&' + gbest_sol['machine'][i] + '&' + gbest_sol['tool'][i] + '&' + gbest_sol['direction'][i])
    return gbest, best_sol, conFE
