# The two-stage variable neighbor search (TS-VNS) for the flexible process planning problem
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
    adj_matrix = [[0] * n for _ in range(n)]  # adjacent matrix: adj_matrix[i][j] = 1 indicates that i is prior to j
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


def violate_constraint_forward(path_left, added_operation, closure_pairs):
    # check if there exist precedence constraints between path_left and the added operation to path_right
    for node in path_left:
        if (node, added_operation) in closure_pairs:
            return True
    return False


def violate_constraint_backward(path_right, added_operation, closure_pairs):
    # check if there exist precedence constraints between path_right and the added operation to path_left
    for node in path_right:
        if (added_operation, node) in closure_pairs:
            return True
    return False


def f_lpp_3exchange(sol, obj, plan, closure_pairs, changing_positions, specifications):
    # forward lexicographic path preserving 3-exchange
    n = len(sol) - 1
    FE = 0  # the number of function evaluations
    best_sol = sol  # the best solution
    best_obj = obj  # the best objective
    best_plan = plan  # the best plan

    for h in range(n - 2):
        for i in range(h + 1, n - 1):
            path_left = sol[h + 1: i + 1]
            j = i + 1
            for j in range(i + 1, n):
                if violate_constraint_forward(path_left, sol[j], closure_pairs):
                    j -= 1
                    break
            path_right = sol[i + 1: j + 1]
            if path_right and [h + 1, i, i + 1, j] not in changing_positions:
                changing_positions.append([h + 1, i, i + 1, j])
                new_sol = sol[: h + 1] + path_right + path_left + sol[j + 1:]
                new_obj, new_plan = cal_objective(new_sol, specifications)
                FE += 1
                if new_obj < best_obj:
                    best_sol = new_sol
                    best_obj = new_obj
                    best_plan = new_plan
    return best_sol, best_obj, best_plan, FE, changing_positions


def b_lpp_3exchange(sol, obj, plan, closure_pairs, changing_positions, specifications):
    # backward lexicographic path preserving 3-exchange
    n = len(sol) - 1
    FE = 0  # the number of function evaluations
    best_sol = sol  # the best solution
    best_obj = obj  # the best objective
    best_plan = plan  # the best plan

    for h in range(n, 2, -1):
        for i in range(h - 1, 1, -1):
            path_right = sol[i: h]
            j = i - 1
            for j in range(i - 1, 0, -1):
                if violate_constraint_backward(path_right, sol[j], closure_pairs):
                    j += 1
                    break
            path_left = sol[j: i]
            if path_left and [j, i - 1, i, h - 1] not in changing_positions:
                changing_positions.append([j, i - 1, i, h - 1])
                new_sol = sol[: j] + path_right + path_left + sol[h:]
                new_obj, new_plan = cal_objective(new_sol, specifications)
                FE += 1
                if new_obj < best_obj:
                    best_sol = new_sol
                    best_obj = new_obj
                    best_plan = new_plan
    return best_sol, best_obj, best_plan, FE, changing_positions


def local_search(sol, obj, plan, closure_pairs, specifications):
    # local search
    if np.random.random() < 0.5:
        new_sol, new_obj, new_plan, increment_FE1, changing_positions = f_lpp_3exchange(sol, obj, plan, closure_pairs, [], specifications)
        changing_positions = [] if new_obj < obj else changing_positions
        new_sol, new_obj, new_plan, increment_FE2, _ = b_lpp_3exchange(new_sol, new_obj, new_plan, closure_pairs, changing_positions, specifications)
    else:
        new_sol, new_obj, new_plan, increment_FE1, changing_positions = b_lpp_3exchange(sol, obj, plan, closure_pairs, [], specifications)
        changing_positions = [] if new_obj < obj else changing_positions
        new_sol, new_obj, new_plan, increment_FE2, _ = f_lpp_3exchange(new_sol, new_obj, new_plan, closure_pairs, changing_positions, specifications)
    return new_sol, new_obj, new_plan, increment_FE1 + increment_FE2


def shaking(sol, k, closure_pairs, specifications):
    # shaking: apply lpp-3-exchange k times
    num = 0
    n = len(sol) - 1
    new_sol = sol.copy()
    while num < k:
        if np.random.random() <= 0.5:
            h, i = sorted(np.random.choice(range(n - 1), size=2, replace=False))
            path_left = new_sol[h + 1: i + 1]
            j = i + 1
            for j in range(i + 1, n):
                if violate_constraint_forward(path_left, new_sol[j], closure_pairs):
                    j -= 1
                    break
            path_right = new_sol[i + 1: j + 1]
            if path_right:
                new_sol = new_sol[: h + 1] + path_right + path_left + new_sol[j + 1:]
                num += 1
        else:
            i, h = sorted(np.random.choice(range(2, n + 1), size=2, replace=False))
            path_right = new_sol[i: h]
            j = i - 1
            for j in range(i - 1, 0, -1):
                if violate_constraint_backward(path_right, new_sol[j], closure_pairs):
                    j += 1
                    break
            path_left = new_sol[j: i]
            if path_left:
                new_sol = new_sol[: j] + path_right + path_left + new_sol[h:]
                num += 1
    new_obj, new_plan = cal_objective(new_sol, specifications)
    return new_sol, new_obj, new_plan


def main(maxFE, specifications):
    """
    The main function.
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
    :param specifications: the specifications of FPP
    :return:
    """
    # Step 1. Remove redundant alternative operations
    operations_to_keep = set()
    for alt in specifications['alternatives']:
        operations_to_keep.add(next(iter(alt)))
    new_operations = {}  # the operations without alternatives
    for op in specifications['operations']:
        if op in specifications['alternative_operations'] and op not in operations_to_keep:
            continue
        new_operations[op] = copy.deepcopy(specifications['operations'][op])
    new_op2ind = {}
    new_ind2op = {}
    for idx, op in enumerate(new_operations):
        new_op2ind[op] = idx
        new_ind2op[idx] = op

    # Step 2. Initialization
    nops = len(new_operations)  # the number of performed operations
    precedence = np.zeros((nops, nops))
    for op1 in new_operations:
        op1_ind = new_op2ind[op1]
        for op2 in new_operations:
            if op1 in new_operations[op2].prior:
                op2_ind = new_op2ind[op2]
                precedence[op1_ind, op2_ind] = 1
    FE = 0  # the number of function evaluations
    closure_pairs = transitive_closure(new_operations)  # transitive closure pairs

    # Step 3. Initialize the first solution
    sol = ['s']
    p = cal_precedence(precedence)  # the precedence constraint satisfaction status
    v = np.ones(nops)  # the selectable status
    q = p * v  # the qualification status
    for _ in range(nops):
        cs = np.where(q == 1)[0]  # the candidate set
        op_ind = np.random.choice(cs)
        op = new_ind2op[op_ind]  # the selected operation
        sol.append(op)
        precedence[op_ind] = 0
        v[op_ind] = 0
        p = cal_precedence(precedence)
        q = p * v
    sol.append('d')
    obj, plan = cal_objective(sol, specifications)  # the objective, process plan
    FE += 1
    best_sol = sol.copy()  # the best operation sequence
    best_obj = obj  # the best objective
    best_plan = plan.copy()  # the best plan
    conFE = FE  # the convergence function evaluation
    k = 1

    # Step 4. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=1) as pbar:
        while FE <= maxFE:
            new_sol, new_obj, new_plan = shaking(best_sol, k, closure_pairs, specifications)
            FE += k
            new_sol, new_obj, new_plan, increment_FE = local_search(new_sol, new_obj, new_plan, closure_pairs, specifications)
            FE += increment_FE
            pbar.update(k + increment_FE)
            if new_obj < best_obj:
                best_sol = new_sol.copy()
                best_obj = new_obj
                best_plan = new_plan.copy()
                conFE = FE
                k = 0
            else:
                k = 1

    # Step 5. Output
    best_plan = best_plan[1:-1]
    return best_obj, best_plan, conFE
