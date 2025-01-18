# Improved edge selection genetic algorithm (IESGA)
import copy
import heapq
import numpy as np
from tqdm import tqdm


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


def tournament_selection(sols, objs, tournament_size=2):
    # tournament selection
    tournament_contestants = np.random.choice(range(len(sols)), tournament_size, replace=False)
    best_contestant = min(tournament_contestants, key=lambda idx: objs[idx])
    return best_contestant


def crossover(sol1, sol2):
    # crossover
    op1, op2 = sol1[1: -1], sol2[1: -1]
    new_sol1, new_sol2 = op1.copy(), op2.copy()
    length = len(new_sol1)
    i1 = np.random.randint(0, length - 1)
    j1 = np.random.randint(i1 + 1, length)
    i2 = np.random.randint(0, length - 1)
    j2 = np.random.randint(i2 + 1, length)
    temp_op1 = op1[i1: j1]
    temp_op2 = op2[i2: j2]
    idx1, idx2 = i1, i2
    for i in range(length):
        if op2[i] in temp_op1:
            new_sol1[idx1] = op2[i]
            idx1 += 1
        if op1[i] in temp_op2:
            new_sol2[idx2] = op1[i]
            idx2 += 1
    new_sol1.insert(0, 's')
    new_sol2.insert(0, 's')
    new_sol1.append('d')
    new_sol2.append('d')
    return new_sol1, new_sol2


def main(npop, maxFE, specifications):
    """
    The main function.
    :param npop: population size (default = 150)
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
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
    conFE = FE  # the convergence function evaluation
    best_obj = min(objs)  # the best objective

    # Step 4. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=npop) as pbar:
        while FE <= maxFE:

            # Step 4.1. Crossover
            idx1, idx2 = tournament_selection(sols, objs), tournament_selection(sols, objs)
            sol1, sol2 = sols[idx1].copy(), sols[idx2].copy()
            new_sol1, new_sol2 = crossover(sol1, sol2)
            new_obj1, new_plan1 = cal_objective(new_sol1, specifications)
            new_obj2, new_plan2 = cal_objective(new_sol2, specifications)
            FE += 2
            pbar.update(2)
            if new_obj1 < objs[idx1]:
                sols[idx1] = new_sol1.copy()
                objs[idx1] = new_obj1
                plans[idx1] = new_plan1.copy()
            if new_obj2 < objs[idx2]:
                sols[idx2] = new_sol2.copy()
                objs[idx2] = new_obj2
                plans[idx2] = new_plan2.copy()
            if new_obj1 < best_obj or new_obj2 < best_obj:
                best_obj = min(new_obj1, new_obj2)
                conFE = FE

    # Step 5. Output
    best_plan = plans[objs.index(best_obj)].copy()  # the best plan
    return best_obj, best_plan[1:-1], conFE
