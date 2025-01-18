# Hybrid evolutionary algorithm (HEA)
# Reference: Liu Q, Li X, Gao L. Mathematical modeling and a hybrid evolutionary algorithm for process planning[J]. Journal of Intelligent Manufacturing, 2021, 32: 781-797.
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


def initialization_population(npop, nops, precedence, specifications):
    # the initialization of operation, resource, and OR chromosomes (Tables 3 and 4)
    operations = specifications['operations']
    alternatives = specifications['alternatives']
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
            selected_idx.append(op_ind)
            operation_chromosome.append(ind2op[op_ind])
            op = ind2op[i]
            machine_chromosome.append(np.random.choice(operations[op].machine))
            tool_chromosome.append(np.random.choice(operations[op].tool))
            direction_chromosome.append(np.random.choice(operations[op].direction))
        or_chromosome = []
        for i in range(len(alternatives)):
            or_chromosome.append(np.random.randint(0, len(alternatives[i])))
        pops.append({
            'operation': operation_chromosome,
            'machine': machine_chromosome,
            'tool': tool_chromosome,
            'direction': direction_chromosome,
            'or': or_chromosome,
        })
    return pops


def cal_objective(sol, specifications):
    # calculate the objective value
    objective = specifications['type']['objective']
    alternatives = specifications['alternatives']
    indices = specifications['indices']
    op2ind = specifications['op2ind']

    obj = 0
    not_performed_operations = []
    for i in range(len(sol['or'])):
        for j in range(len(alternatives[i])):
            if sol['or'][i] != j:
                not_performed_operations.append(alternatives[i][j])
    ops = [op for op in sol['operation'] if op not in not_performed_operations]
    machine = []
    tool = []
    direction = []
    for op in ops:
        idx = op2ind[op]
        machine.append(sol['machine'][idx])
        tool.append(sol['tool'][idx])
        direction.append(sol['direction'][idx])

    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
        for i in range(len(ops)):
            string = ops[i] + '&' + machine[i] + '&' + tool[i] + '&' + direction[i]
            obj += indices[ops[i]][string]
            if i != 0:
                if machine[i] != machine[i - 1]:
                    obj += mcc
                if machine[i] != machine[i - 1] or tool[i] != tool[i - 1]:
                    obj += tcc
                if machine[i] != machine[i - 1] or direction[i] != direction[i - 1]:
                    obj += scc
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']
        for i in range(len(ops)):
            string = ops[i] + '&' + machine[i] + '&' + tool[i] + '&' + direction[i]
            obj += indices[ops[i]][string]
            if i != 0:
                if machine[i] != machine[i - 1]:
                    obj += mct[machine[i - 1]][machine[i]]
                if machine[i] != machine[i - 1] or tool[i] != tool[i - 1]:
                    obj += tct
                if machine[i] != machine[i - 1] or direction[i] != direction[i - 1]:
                    obj += sct
    return obj


def tournament_selection(sols, objs, tournament_size=8):
    # tournament selection
    tournament_contestants = np.random.choice(range(len(sols)), tournament_size, replace=False)
    best_contestant = min(tournament_contestants, key=lambda idx: objs[idx])
    return best_contestant


def single_point_crossover(parent1, parent2):
    # the single-point crossover for OR chromosomes
    length = len(parent1)
    if length < 2:
        return parent1, parent2
    point = np.random.randint(1, length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def two_point_crossover(parent1, parent2):
    # the two-point crossover for resource chromosomes (Table 7)
    length = len(parent1)
    point1 = np.random.randint(1, length - 1)
    point2 = np.random.randint(point1 + 1, length)
    child1 = parent1[:point1] + parent2[point1: point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1: point2] + parent2[point2:]
    return child1, child2


def operation_crossover(parent1, parent2):
    # the crossover for operation chromosomes (Table 6)
    length = len(parent1)
    point1 = np.random.randint(1, length - 2)
    point2 = np.random.randint(point1 + 1, length - 1)
    child1, child2 = parent1.copy(), parent2.copy()
    temp_parent1 = parent1[point1: point2]
    temp_parent2 = parent2[point1: point2]
    idx1 = idx2 = point1
    for i in range(length):
        if parent2[i] in temp_parent1:
            child1[idx1] = parent2[i]
            idx1 += 1
        if parent1[i] in temp_parent2:
            child2[idx2] = parent1[i]
            idx2 += 1
    return child1, child2


def single_point_mutation(parent, specifications):
    # the single-point mutation for resource and OR chromosomes
    operations = specifications['operations']
    alternatives = specifications['alternatives']
    ind2op = specifications['ind2op']

    case = np.random.randint(1, len(parent))
    child = copy.deepcopy(parent)
    length = len(parent['operation'])
    # machine chromosome mutation
    if case == 1:
        chromosome = parent['machine']
        point = np.random.randint(0, length)
        op = operations[ind2op[point]]
        filtered_elements = [e for e in op.machine if e != chromosome[point]]
        if filtered_elements:
            child['machine'][point] = np.random.choice(filtered_elements)
    # tool chromosome mutation
    elif case == 2:
        chromosome = parent['tool']
        point = np.random.randint(0, length)
        op = operations[ind2op[point]]
        filtered_elements = [e for e in op.tool if e != chromosome[point]]
        if filtered_elements:
            child['tool'][point] = np.random.choice(filtered_elements)
    # direction chromosome mutation
    elif case == 3:
        chromosome = parent['direction']
        point = np.random.randint(0, length)
        op = operations[ind2op[point]]
        filtered_elements = [e for e in op.direction if e != chromosome[point]]
        if filtered_elements:
            child['direction'][point] = np.random.choice(filtered_elements)
    # OR chromosome mutation
    else:
        chromosome = parent['or']
        if chromosome:
            point = np.random.randint(0, len(alternatives))
            filtered_elements = [e for e in range(len(alternatives[point])) if e != chromosome[point]]
            child['or'][point] = np.random.choice(filtered_elements)
    return child


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


def two_point_mutation(parent, closure_pairs):
    # the two-point mutation for operation chromosome (Table 8 may generate infeasible solutions!)
    child = copy.deepcopy(parent)
    chromosome = parent['operation']
    idx1 = np.random.randint(0, len(chromosome))
    mutation_range = find_mutation_range(chromosome, closure_pairs, idx1)
    while not mutation_range:
        idx1 = np.random.randint(0, len(chromosome))
        mutation_range = find_mutation_range(chromosome, closure_pairs, idx1)
    idx2 = np.random.choice(mutation_range)
    child['operation'][idx1], child['operation'][idx2] = parent['operation'][idx2], parent['operation'][idx1]
    return child


def SA_operator(pops, objs, temperature, closure_pairs, specifications):
    # the simulated annealing operator
    npop = len(pops)
    for i in range(npop):
        parent1 = copy.deepcopy(pops[i])
        parent2 = copy.deepcopy(np.random.choice(pops))
        new_sol = {
            'operation': operation_crossover(parent1['operation'], parent2['operation'])[0],
            'machine': two_point_crossover(parent1['machine'], parent2['machine'])[0],
            'tool': two_point_crossover(parent1['tool'], parent2['tool'])[0],
            'direction': two_point_crossover(parent1['direction'], parent2['direction'])[0],
            'or': single_point_crossover(parent1['or'], parent2['or'])[0],
        }
        new_sol = two_point_mutation(new_sol, closure_pairs)
        new_sol = single_point_mutation(new_sol, specifications)
        new_obj = cal_objective(new_sol, specifications)
        if new_obj <= objs[i] or np.random.random() < np.exp(-(new_obj - objs[i]) / temperature):
            pops[i] = new_sol
            objs[i] = new_obj
    return pops, objs


def GA_operator(pops, objs, pc, pm, closure_pairs, specifications):
    # the genetic algorithm operator
    mating_pool = []  # mating pool
    new_pops = []
    nm = int(len(pops) * pc)  # mating pool size
    nm = nm if nm % 2 == 0 else nm + 1
    for _ in range(nm):
        temp_sol = copy.deepcopy(pops[tournament_selection(pops, objs)])
        mating_pool.append(temp_sol)
    for i in range(0, nm, 2):
        parent1, parent2 = mating_pool[i], mating_pool[i + 1]
        operation1, operation2 = operation_crossover(parent1['operation'], parent2['operation'])
        machine1, machine2 = two_point_crossover(parent1['machine'], parent2['machine'])
        tool1, tool2 = two_point_crossover(parent1['tool'], parent2['tool'])
        direction1, direction2 = two_point_crossover(parent1['direction'], parent2['direction'])
        or1, or2 = single_point_crossover(parent1['or'], parent2['or'])
        new_pops.append({
            'operation': operation1,
            'machine': machine1,
            'tool': tool1,
            'direction': direction1,
            'or': or1,
        })
        new_pops.append({
            'operation': operation2,
            'machine': machine2,
            'tool': tool2,
            'direction': direction2,
            'or': or2,
        })
    for i in range(nm):
        if np.random.random() < pm:
            parent = mating_pool[i]
            child = two_point_mutation(parent, closure_pairs)
            child = single_point_mutation(child, specifications)
            new_pops[i] = child
    return new_pops, [cal_objective(sol, specifications) for sol in new_pops]


def environmental_selection(pops, objs, npop):
    # environmental selection
    paired = list(zip(pops, objs))
    sorted_paired = sorted(paired, key=lambda x: x[1])
    selected = sorted_paired[: npop]
    selected_pops, selected_objs = zip(*selected)
    return list(selected_pops), list(selected_objs)


def check_feasibility(ops, closure_pairs):
    for i in range(len(ops) - 1):
        for j in range(i + 1, len(ops)):
            if (ops[j], ops[i]) in closure_pairs:
                return False
    return True


def main(npop, maxFE, pc, pm, T0, alpha, specifications):
    """
    The main function.
    :param npop: population size (default = 400)
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
    :param pc: crossover probability (default = 0.8)
    :param pm: mutation probability (default = 0.1)
    :param T0: the initial temperature for simulated annealing (default = 1000)
    :param alpha: cooling rate (default = 0.99)
    :param specifications: the specifications of FPP
    :return:
    """
    operations = specifications['operations']
    alternatives = specifications['alternatives']
    op2ind = specifications['op2ind']
    for r in range(len(alternatives)):
        alternatives[r] = list(alternatives[r])

    # Step 1. Initialization
    closure_pairs = transitive_closure(operations)  # transitive closure pairs
    nops = len(operations)  # the number of operations
    FE = 0  # the number of function evaluations
    precedence = np.zeros((nops, nops))
    for op1 in operations:
        op1_ind = op2ind[op1]
        for op2 in operations:
            if op1 in operations[op2].prior:
                op2_ind = op2ind[op2]
                precedence[op1_ind, op2_ind] = 1
    sols = initialization_population(npop, nops, precedence, specifications)  # solutions
    objs = [cal_objective(sol, specifications) for sol in sols]  # objectives
    FE += npop
    gbest = min(objs)  # the global best
    gbest_sol = copy.deepcopy(sols[objs.index(gbest)])  # the global best solution
    conFE = FE  # the convergence function evaluation
    temperature = T0  # temperature

    # Step 2. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=npop) as pbar:
        while FE <= maxFE:
            new_sols, new_objs = SA_operator(sols, objs, temperature, closure_pairs, specifications)
            new_sols, new_objs = GA_operator(new_sols, new_objs, pc, pm, closure_pairs, specifications)
            temp_sols = sols + new_sols
            temp_objs = objs + new_objs
            sols, objs = environmental_selection(temp_sols, temp_objs, npop)
            FE += (npop + len(new_objs))
            pbar.update(int(npop + len(new_objs)))
            temperature *= alpha

            if min(objs) < gbest:
                gbest = min(objs)
                gbest_sol = copy.deepcopy(sols[objs.index(gbest)])
                conFE = FE

    # Step 3. Output
    best_sol = []
    for i in range(len(gbest_sol['operation'])):
        best_sol.append(gbest_sol['operation'][i] + '&' + gbest_sol['machine'][i] + '&' + gbest_sol['tool'][i] + '&' +
                        gbest_sol['direction'][i])
    return gbest, best_sol, conFE
