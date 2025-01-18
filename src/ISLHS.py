# Improved sequence learning harmony search (ISLHS)
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


def main(hms, maxFE, specifications):
    """
    The main function.
    :param hms: harmony memory size (default = 10)
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
    for _ in range(hms):
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
    gbest = min(objs)  # the global best
    gbest_plan = plans[objs.index(gbest)].copy()  # the global best plan
    gworst = max(objs)  # the global worst
    FE += hms
    conFE = FE  # the convergence function evaluation

    # Step 4. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=hms) as pbar:
        while FE <= maxFE:

            # Step 4.1. Generate a new harmony
            co = None  # the current operation
            temp_sol = ['s']
            temp_p = precedence.copy()
            temp_v = v.copy()
            temp_q = q.copy()
            hmcr = min(max(np.random.normal(nops / (1 + nops), 1 / (1 + nops)), 0), 1)  # harmony memory consideration rate

            for k in range(nops):
                cs = np.where(temp_q == 1)[0]
                tab = 0  # the learning success flag
                if np.random.rand() < hmcr:  # memory consideration
                    rs = [i for i in range(hms)]  # the sample set
                    if k == 0:
                        tab = 1
                        idx = np.random.choice(hms)
                        temp_sol.append(sols[idx][1])
                    else:
                        while rs:
                            idx = np.random.choice(rs)
                            flag = False
                            for r in range(nops - 1):
                                temp_op1 = sols[idx][r + 1]
                                temp_op2 = sols[idx][r + 2]
                                temp_op2_ind = new_op2ind[temp_op2]
                                if temp_op1 == co and temp_op2_ind in cs:
                                    temp_sol.append(temp_op2)
                                    rs = []
                                    tab = 1
                                    flag = True
                                    break
                            if not flag:
                                rs.remove(idx)

                if tab == 0:  # harmony randomization
                    temp_op_ind = np.random.choice(cs)
                    temp_op = new_ind2op[temp_op_ind]
                    temp_sol.append(temp_op)

                temp_op = temp_sol[-1]
                temp_op_ind = new_op2ind[temp_op]
                temp_p[temp_op_ind] = 0
                temp_v[temp_op_ind] = 0
                temp_u = cal_precedence(temp_p)
                temp_q = temp_u * temp_v
                co = temp_op
            temp_sol.append('d')

            # Step 4.2. Is it superior to the worst?
            temp_obj, temp_plan = cal_objective(temp_sol, specifications)
            FE += 1
            pbar.update(1)
            if temp_obj < gworst:
                gworst_ind = objs.index(gworst)
                sols[gworst_ind] = temp_sol.copy()
                objs[gworst_ind] = temp_obj
                gworst = max(objs)
            if temp_obj < gbest:
                gbest = temp_obj
                gbest_plan = temp_plan.copy()
                conFE = FE

    # Step 5. Output
    return gbest, gbest_plan[1:-1], conFE
