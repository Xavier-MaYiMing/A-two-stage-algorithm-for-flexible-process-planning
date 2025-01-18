# Improved feasible sequence oriented discrete particle swarm optimization (IFSDPSO)
import copy
import heapq
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


def dijkstra(graph, source, target):
    # the Dijkstra's algorithm for the shortest path problem
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    distances = {vertex: float('inf') for vertex in graph}
    shortest_path_tree = {}

    while priority_queue:
        temp_distance, temp_vertex = heapq.heappop(priority_queue)
        if temp_distance > distances[temp_vertex]:
            continue
        if temp_vertex == target:
            break
        for neighbor, weight in graph[temp_vertex].items():
            distance = temp_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                shortest_path_tree[neighbor] = temp_vertex

    path = []
    step = target
    while step != source:
        path.append(step)
        step = shortest_path_tree[step]
    path.append(source)
    path.reverse()
    return distances[target], path


def construct_graph(sol, specifications):
    # construct graph based on the solution to transform the selection of alternative operations and the allocation of manufacturing resources into the shortest path problem (cost)
    graph = {'s': {}, 'd': {}}
    objective = specifications['type']['objective']
    indices = specifications['indices']
    alternative_operations = specifications['alternative_operations']

    for state in indices[sol[1]]:
        graph['s'][state] = indices[sol[1]][state]
    if sol[1] in alternative_operations:
        for op1 in alternative_operations[sol[1]]:
            for state in indices[op1]:
                graph['s'][state] = indices[op1][state]
    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
        for i in range(1, len(sol) - 2):
            op1, op2 = sol[i], sol[i + 1]
            ops1, ops2 = [op1], [op2]
            if op1 in alternative_operations:
                ops1 += list(alternative_operations[op1])
            if op2 in alternative_operations:
                ops2 += list(alternative_operations[op2])
            for op1 in ops1:
                for state1 in indices[op1]:
                    [_, m1, t1, d1] = state1.split('&')
                    graph[state1] = {}
                    for op2 in ops2:
                        for state2 in indices[op2]:
                            [_, m2, t2, d2] = state2.split('&')
                            weight = indices[op2][state2]
                            if m1 != m2:
                                weight += mcc
                            if m1 != m2 or t1 != t2:
                                weight += tcc
                            if m1 != m2 or d1 != d2:
                                weight += scc
                            graph[state1][state2] = weight
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']
        for i in range(1, len(sol) - 2):
            op1, op2 = sol[i], sol[i + 1]
            ops1, ops2 = [op1], [op2]
            if op1 in alternative_operations:
                ops1 += list(alternative_operations[op1])
            if op2 in alternative_operations:
                ops2 += list(alternative_operations[op2])
            for op1 in ops1:
                for state1 in indices[op1]:
                    [_, m1, t1, d1] = state1.split('&')
                    graph[state1] = {}
                    for op2 in ops2:
                        for state2 in indices[op2]:
                            [_, m2, t2, d2] = state2.split('&')
                            weight = indices[op2][state2]
                            if m1 != m2:
                                weight += mct[m1][m2]
                            if m1 != m2 or t1 != t2:
                                weight += tct
                            if m1 != m2 or d1 != d2:
                                weight += sct
                            graph[state1][state2] = weight
    for state in indices[sol[-2]]:
        graph[state] = {'d': 0}
    if sol[-2] in alternative_operations:
        for op1 in alternative_operations[sol[-2]]:
            for state in indices[op1]:
                graph[state] = {'d': 0}
    return graph


def cal_objective(sol, specifications):
    # calculate the objective value of a given sequence of operations
    graph = construct_graph(sol, specifications)
    return dijkstra(graph, 's', 'd')


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


def fragment_crossover(sol1, sol2):
    # fragment crossover
    op1, op2 = sol1[1: -1], sol2[1: -1]
    point1, point2 = sorted(np.random.choice(range(1, len(op1) - 1), 2, replace=False))
    temp_op = op1[point1: point2]
    idx = point1
    new_op = op1.copy()
    for i in range(len(op1)):
        if op2[i] in temp_op:
            new_op[idx] = op2[i]
            idx += 1
    new_op.insert(0, 's')
    new_op.append('d')
    return new_op


def find_mutation_range(sol, closure_pairs, idx):
    # find the mutation range
    idx1, idx2 = idx, idx
    while sol[idx1 - 1] != 's' and (sol[idx1 - 1], sol[idx]) not in closure_pairs:
        flag = False
        for i in range(idx1, idx):
            if (sol[idx1 - 1], sol[i]) in closure_pairs:
                flag = True
                break
        if flag:
            break
        idx1 -= 1
    while sol[idx2 + 1] != 'd' and (sol[idx], sol[idx2 + 1]) not in closure_pairs:
        flag = False
        for i in range(idx + 1, idx2 + 1):
            if (sol[i], sol[idx2 + 1]) in closure_pairs:
                flag = True
                break
        if flag:
            break
        idx2 += 1
    return [i for i in range(idx1, idx2 + 1) if i != idx]


def fragment_mutation(sol, closure_pairs):
    # fragment mutation
    new_sol = sol.copy()
    idx1 = np.random.randint(1, len(sol) - 1)
    mutation_range = find_mutation_range(sol, closure_pairs, idx1)
    while not mutation_range:
        idx1 = np.random.randint(1, len(sol) - 1)
        mutation_range = find_mutation_range(sol, closure_pairs, idx1)
    idx2 = np.random.choice(mutation_range)
    new_sol[idx1], new_sol[idx2] = sol[idx2], sol[idx1]
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
    alternatives = specifications['alternatives']
    alternative_operations = specifications['alternative_operations']

    # Step 1. Remove redundant alternative operations
    operations_to_keep = set()
    for alt in alternatives:
        operations_to_keep.add(next(iter(alt)))
    new_operations = {}  # the operations without alternatives
    for op in operations:
        if op in alternative_operations and op not in operations_to_keep:
            continue
        new_operations[op] = copy.deepcopy(operations[op])
    new_op2ind = {}
    new_ind2op = {}
    for idx, op in enumerate(new_operations):
        new_op2ind[op] = idx
        new_ind2op[idx] = op

    # Step 2. Initialization
    sols = []  # solutions
    objs = []  # objectives
    plans = []  # plans
    nops = len(new_operations)  # the number of performed operations
    precedence = np.zeros((nops, nops))
    for op1 in new_operations:
        op1_ind = new_op2ind[op1]
        for op2 in new_operations:
            if op1 in new_operations[op2].prior:
                op2_ind = new_op2ind[op2]
                precedence[op1_ind, op2_ind] = 1
    FE = 0  # the number of function evaluations
    closure_pairs = transitive_closure(operations)  # transitive closure pairs
    u = cal_precedence(precedence)  # the precedence constraint satisfaction status
    v = np.ones(nops)  # the selectable status
    q = u * v  # the qualification status

    # Step 3. Initial solutions
    for _ in range(npop):
        temp_sol = ['s']
        temp_p = precedence.copy()
        temp_v = v.copy()
        temp_q = q.copy()
        for k in range(nops):
            cs = np.where(temp_q == 1)[0]  # the candidate set
            op_ind = np.random.choice(cs)
            op = new_ind2op[op_ind]  # the selected operation
            temp_p[op_ind] = 0
            temp_v[op_ind] = 0
            temp_u = cal_precedence(temp_p)
            temp_q = temp_u * temp_v
            temp_sol.append(op)
        temp_sol.append('d')
        sols.append(temp_sol)
        obj, plan = cal_objective(temp_sol, specifications)
        objs.append(obj)
        plans.append(plan)
    FE += npop
    pbest = objs.copy()  # the personal best
    pbest_sol = copy.deepcopy(sols)  # the personal best solutions
    gbest = min(objs)  # the global best
    gbest_sol = sols[objs.index(gbest)].copy()  # the global best solution
    gbest_plan = plans[objs.index(gbest)].copy()  # the global best plan
    conFE = FE  # convergence function iteration

    # Step 4. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=npop) as pbar:
        while FE <= maxFE:

            # Step 4.1. Generate new solution
            for k in range(npop):
                r, r1, r2 = np.random.random(), np.random.random(), np.random.random()
                if r < w / (c1 * r1 + c2 * r2 + w):
                    new_sol = sols[k].copy()
                elif r < (w + c1 * r1) / (c1 * r1 + c2 * r2 + w):
                    new_sol = fragment_crossover(sols[k], pbest_sol[k])
                else:
                    new_sol = fragment_crossover(sols[k], gbest_sol)
                pm = k1 * (max(objs) - objs[k]) / (max(objs) - sum(objs) / len(objs)) + k2
                if np.random.random() < pm:
                    new_sol = fragment_mutation(new_sol, closure_pairs)
                sols[k] = new_sol.copy()
                new_obj, new_plan = cal_objective(new_sol, specifications)
                objs[k] = new_obj
                plans[k] = new_plan
                FE += 1
                pbar.update(1)
                if new_obj < pbest[k]:
                    pbest[k] = new_obj
                    pbest_sol[k] = new_sol.copy()
                    if new_obj < gbest:
                        gbest = new_obj
                        gbest_sol = new_sol.copy()
                        gbest_plan = new_plan.copy()
                        conFE = FE

    # Step 5. Output
    return gbest, gbest_plan[1:-1], conFE
