# Sequence learning harmony search (SLHS)
# Reference: Luo K. A sequence learning harmony search algorithm for the flexible process planning problem[J]. International Journal of Production Research, 2022, 60(10): 3182-3200.
import numpy as np
from tqdm import tqdm


def cal_objective(sol, specifications):
    # calculate the objective value
    objective = specifications['type']['objective']
    indices = specifications['indices']

    obj = 0
    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
        for i in range(len(sol) - 1):
            o1, m1, t1, d1 = sol[i].split('&')
            _, m2, t2, d2 = sol[i + 1].split('&')
            if m1 != m2:
                obj += mcc
            if m1 != m2 or t1 != t2:
                obj += tcc
            if m1 != m2 or d1 != d2:
                obj += scc
            obj += indices[o1][sol[i]]
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']
        for i in range(len(sol) - 1):
            o1, m1, t1, d1 = sol[i].split('&')
            _, m2, t2, d2 = sol[i + 1].split('&')
            if m1 != m2:
                obj += mct[m1][m2]
            if m1 != m2 or t1 != t2:
                obj += tct
            if m1 != m2 or d1 != d2:
                obj += sct
            obj += indices[o1][sol[i]]
    o2 = sol[-1].split('&')[0]
    obj += indices[o2][sol[-1]]
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
    op2ind = specifications['op2ind']
    ind2op = specifications['ind2op']

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
    for _ in range(hms):
        temp_sol = []
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
            temp_sol.append(temp_op + '&' + temp_m + '&' + temp_t + '&' + temp_d)
        sols.append(temp_sol)
        objs.append(cal_objective(temp_sol, specifications))
    gbest = min(objs)  # the global best
    gbest_sol = sols[objs.index(gbest)]  # the global best solution
    gworst = max(objs)  # the global worst
    FE += hms
    conFE = 0  # the convergence function evaluation

    # Step 3. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval", initial=hms) as pbar:
        while FE <= maxFE:

            # Step 3.1. Generate a new harmony
            co = None  # the current operation
            temp_sol = []
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
                        temp_sol.append(sols[idx][0])
                    else:
                        while rs:
                            idx = np.random.choice(rs)
                            flag = False
                            for r in range(nops - 1):
                                temp_op1 = sols[idx][r].split('&')[0]
                                temp_op2 = sols[idx][r + 1].split('&')[0]
                                temp_op2_ind = op2ind[temp_op2]
                                if temp_op1 == co and temp_op2_ind in cs:
                                    temp_sol.append(sols[idx][r + 1])
                                    rs = []
                                    tab = 1
                                    flag = True
                                    break
                            if not flag:
                                rs.remove(idx)

                if tab == 0:  # harmony randomization
                    temp_op_ind = np.random.choice(cs)
                    temp_op = ind2op[temp_op_ind]
                    temp_m = np.random.choice(operations[temp_op].machine)
                    temp_t = np.random.choice(operations[temp_op].tool)
                    temp_d = np.random.choice(operations[temp_op].direction)
                    temp_sol.append(temp_op + '&' + temp_m + '&' + temp_t + '&' + temp_d)

                temp_op = temp_sol[-1].split('&')[0]
                temp_op_ind = op2ind[temp_op]
                temp_p[temp_op_ind] = 0
                temp_v[temp_op_ind] = 0
                if temp_op in alternative_operations:
                    for alt in alternative_operations[temp_op]:
                        alt_ind = op2ind[alt]
                        temp_p[alt_ind] = 0
                        temp_v[alt_ind] = 0
                temp_u = cal_precedence(temp_p)
                temp_q = temp_u * temp_v
                co = temp_op

            for k in range(1, nops):  # pitch adjustment
                temp_op1, temp_m1, temp_t1, temp_d1 = temp_sol[k - 1].split('&')
                temp_op2, temp_m2, temp_t2, temp_d2 = temp_sol[k].split('&')
                if temp_m1 in operations[temp_op2].machine:
                    temp_m2 = temp_m1
                if temp_t1 in operations[temp_op2].tool:
                    temp_t2 = temp_t1
                if temp_d1 in operations[temp_op2].direction:
                    temp_d2 = temp_d1
                temp_sol[k] = temp_op2 + '&' + temp_m2 + '&' + temp_t2 + '&' + temp_d2

            # Step 3.2. Is it superior to the worst?
            temp_obj = cal_objective(temp_sol, specifications)
            FE += 1
            pbar.update(1)
            if temp_obj < gworst:
                gworst_ind = objs.index(gworst)
                sols[gworst_ind] = temp_sol.copy()
                objs[gworst_ind] = temp_obj
                gworst = max(objs)
            if temp_obj < gbest:
                gbest = temp_obj
                gbest_sol = temp_sol.copy()
                conFE = FE

    # Step 4. Output
    return gbest, gbest_sol, conFE
