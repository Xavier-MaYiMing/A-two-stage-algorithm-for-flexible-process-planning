# Edge selection genetic algorithm (ESGA)
# Reference: Su Y, Chu X, Chen D, et al. A genetic algorithm for operation sequencing in CAPP using edge selection based encoding strategy[J]. Journal of Intelligent Manufacturing, 2018, 29: 313-332.
import copy
import numpy as np
from tqdm import tqdm


def cal_objective(sol, specifications):
    # calculate the objective value
    objective = specifications['type']['objective']
    indices = specifications['indices']

    obj = 0
    n = len(sol['operation'])
    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
        for i in range(n - 1):
            o1, m1, t1, d1 = sol['operation'][i], sol['machine'][i], sol['tool'][i], sol['direction'][i]
            m2, t2, d2 = sol['machine'][i + 1], sol['tool'][i + 1], sol['direction'][i + 1]
            if m1 != m2:
                obj += mcc
            if m1 != m2 or t1 != t2:
                obj += tcc
            if m1 != m2 or d1 != d2:
                obj += scc
            obj += indices[o1][o1 + '&' + m1 + '&' + t1 + '&' + d1]
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']
        for i in range(n - 1):
            o1, m1, t1, d1 = sol['operation'][i], sol['machine'][i], sol['tool'][i], sol['direction'][i]
            m2, t2, d2 = sol['machine'][i + 1], sol['tool'][i + 1], sol['direction'][i + 1]
            if m1 != m2:
                obj += mct[m1][m2]
            if m1 != m2 or t1 != t2:
                obj += tct
            if m1 != m2 or d1 != d2:
                obj += sct
            obj += indices[o1][o1 + '&' + m1 + '&' + t1 + '&' + d1]
    o2, m2, t2, d2 = sol['operation'][-1], sol['machine'][-1], sol['tool'][-1], sol['direction'][-1]
    obj += indices[o2][o2 + '&' + m2 + '&' + t2 + '&' + d2]
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


def tournament_selection(sols, objs, tournament_size=2):
    # tournament selection
    tournament_contestants = np.random.choice(range(len(sols)), tournament_size, replace=False)
    best_contestant = min(tournament_contestants, key=lambda idx: objs[idx])
    return best_contestant


def crossover(sol1, sol2):
    # crossover
    op1, op2 = sol1['operation'], sol2['operation']
    new_sol1, new_sol2 = copy.deepcopy(sol1), copy.deepcopy(sol2)
    length = len(op1)
    i1 = np.random.randint(0, length - 1)
    j1 = np.random.randint(i1 + 1, length)
    i2 = np.random.randint(0, length - 1)
    j2 = np.random.randint(i2 + 1, length)
    temp_op1 = op1[i1: j1]
    temp_op2 = op2[i2: j2]
    idx1, idx2 = i1, i2
    for i in range(length):
        if op2[i] in temp_op1:
            new_sol1['operation'][idx1] = op2[i]
            new_sol1['machine'][idx1] = sol2['machine'][i]
            new_sol1['tool'][idx1] = sol2['tool'][i]
            new_sol1['direction'][idx1] = sol2['direction'][i]
            idx1 += 1
        if op1[i] in temp_op2:
            new_sol2['operation'][idx2] = op1[i]
            new_sol2['machine'][idx2] = sol1['machine'][i]
            new_sol2['tool'][idx2] = sol1['tool'][i]
            new_sol2['direction'][idx2] = sol1['direction'][i]
            idx2 += 1
    return new_sol1, new_sol2


def mutation(sol, specifications):
    operations = specifications['operations']

    # mutation
    n = len(sol['operation'])
    new_sol = copy.deepcopy(sol)
    for i in range(n - 1):
        op1, op2 = sol['operation'][i], sol['operation'][i + 1]
        if sol['machine'][i] in operations[op2].machine:
            new_sol['machine'][i + 1] = sol['machine'][i]
        if new_sol['machine'][i] == new_sol['machine'][i + 1]:
            if sol['tool'][i] in operations[op2].tool:
                new_sol['tool'][i + 1] = sol['tool'][i]
            if sol['direction'][i] in operations[op2].direction:
                new_sol['direction'][i + 1] = sol['direction'][i]
    return new_sol


def main(npop, maxFE, pc, pm, specifications):
    """
    The main function.
    :param npop: population size (default = 150)
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
    :param pc: crossover probability (default = 0.8)
    :param pm: mutation probability (default = 0.2)
    :param specifications: the specifications of FPP
    :return:
    """
    operations = specifications['operations']
    alternatives = specifications['alternatives']
    alternative_operations = specifications['alternative_operations']
    op2ind = specifications['op2ind']
    ind2op = specifications['ind2op']
    if specifications['type']['alternative']:
        raise ValueError('ESGA cannot solve cases with alternative operations.')

    # Step 1. Initialization
    sols = []  # solutions
    objs = []  # objectives
    nops_all = len(operations)  # the number of operations
    nops = nops_all  # the number of performed operations
    for alt in alternatives:
        nops -= (len(alt) - 1)
    FE = 0  # the number of function evaluations
    precedence = np.zeros((nops_all, nops_all))
    for op1 in operations:
        op1_ind = op2ind[op1]
        for op2 in operations:
            if op1 in operations[op2].prior:
                op2_ind = op2ind[op2]
                precedence[op1_ind, op2_ind] = 1
    u = cal_precedence(precedence)  # the precedence constraint satisfaction status
    v = np.ones(nops_all)  # the selectable status
    q = u * v  # the qualification status

    # Step 2. Initial solutions
    for _ in range(npop):
        operation_chromosome = []
        machine_chromosome = []
        tool_chromosome = []
        direction_chromosome = []
        temp_p = precedence.copy()
        temp_v = v.copy()
        temp_q = q.copy()
        for k in range(nops):
            cs = np.where(temp_q == 1)[0]  # the candidate set
            temp_op_ind = np.random.choice(cs)
            temp_op = ind2op[temp_op_ind]  # the selected operation
            temp_m = np.random.choice(operations[temp_op].machine)  # the selected machine
            temp_t = np.random.choice(operations[temp_op].tool)  # the selected tool
            temp_d = np.random.choice(operations[temp_op].direction)  # the selected direction
            temp_p[temp_op_ind] = 0
            temp_v[temp_op_ind] = 0
            if temp_op in alternative_operations:
                for alt in alternative_operations[temp_op]:
                    alt_ind = op2ind[alt]
                    temp_p[alt_ind] = 0
                    temp_v[alt_ind] = 0
            temp_u = cal_precedence(temp_p)
            temp_q = temp_u * temp_v
            operation_chromosome.append(temp_op)
            machine_chromosome.append(temp_m)
            tool_chromosome.append(temp_t)
            direction_chromosome.append(temp_d)
        temp_sol = {
            'operation': operation_chromosome,
            'machine': machine_chromosome,
            'tool': tool_chromosome,
            'direction': direction_chromosome,
        }
        sols.append(temp_sol.copy())
        objs.append(cal_objective(temp_sol, specifications))
    FE += npop
    gbest = min(objs)  # the global best
    gbest_sol = sols[objs.index(gbest)].copy()  # the global best solution
    conFE = FE  # the convergence function evaluation

    # Step 3. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=npop) as pbar:
        while FE <= maxFE:

            # Step 3.1. Generate new solutions
            flag1 = flag2 = False
            idx1, idx2 = tournament_selection(sols, objs), tournament_selection(sols, objs)
            sol1, sol2 = copy.deepcopy(sols[idx1]), copy.deepcopy(sols[idx2])
            if np.random.random() < pc:
                flag1 = flag2 = True
                sol1, sol2 = crossover(sols[idx1], sols[idx2])

            if np.random.random() < pm:
                flag1 = True
                sol1 = mutation(sol1, specifications)

            if np.random.random() < pm:
                flag2 = True
                sol2 = mutation(sol2, specifications)

            # Step 3.2. Update the global best
            if flag1:
                new_obj = cal_objective(sol1, specifications)
                FE += 1
                pbar.update(1)
                if new_obj < objs[idx1]:
                    sols[idx1] = sol1
                    objs[idx1] = new_obj
                    if new_obj < gbest:
                        gbest = new_obj
                        gbest_sol = copy.deepcopy(sol1)
                        conFE = FE

            if flag2:
                new_obj = cal_objective(sol2, specifications)
                FE += 1
                pbar.update(1)
                if new_obj < objs[idx2]:
                    sols[idx2] = sol2
                    objs[idx2] = new_obj
                    if new_obj < gbest:
                        gbest = new_obj
                        gbest_sol = copy.deepcopy(sol2)
                        conFE = FE

    # Step 4. Output
    best_sol = []
    for i in range(len(gbest_sol['operation'])):
        best_sol.append(gbest_sol['operation'][i] + '&' + gbest_sol['machine'][i] + '&' + gbest_sol['tool'][i] + '&' +
                        gbest_sol['direction'][i])
    return gbest, best_sol, conFE

