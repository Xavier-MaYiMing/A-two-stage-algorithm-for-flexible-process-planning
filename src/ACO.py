# Ant colony optimization
# Reference: Liu X, Yi H, Ni Z. Application of ant colony optimization algorithm in process planning optimization[J]. Journal of Intelligent Manufacturing, 2013, 24: 1-13.
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


def main(npop, maxFE, rho, W, alpha, beta, tau0, specifications):
    """
    The main function.
    :param npop: population size (default = 100)
    :param maxFE: the maximum function evaluations (default = 1000 * the number of operations)
    :param rho: pheromone evaporation rate (default = 0.1)
    :param W: pheromone increase (default = 100)
    :param alpha: pheromone importance (default = 1)
    :param beta: heuristic importance (default = 2)
    :param tau0: initial pheromone value (default = 100)
    :param specifications: the specifications of FPP
    :return:
    """
    objective = specifications['type']['objective']
    operations = specifications['operations']
    alternatives = specifications['alternatives']
    alternative_operations = specifications['alternative_operations']
    indices = specifications['indices']
    op2ind = specifications['op2ind']
    ind2op = specifications['ind2op']
    if objective == 'cost':
        mcc, tcc, scc = specifications['mcc'], specifications['tcc'], specifications['scc']
    else:
        mct, tct, sct = specifications['mct'], specifications['tct'], specifications['sct']

    # Step 1. Initialization
    nops_all = len(operations)  # the number of operations
    nops = nops_all  # the number of performed operations
    for alt in alternatives:
        nops -= (len(alt) - 1)
    COs = []  # candidate operations
    for op in indices:
        COs += indices[op].keys()
    CO2ind = {COs[i]: i for i in range(len(COs))}
    tau = np.ones((len(COs), len(COs))) * tau0  # pheromone matrix
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
    gbest = float('inf')  # the global best
    gbest_sol = None  # the global best solution
    conFE = 0  # convergence function evaluation

    # Step 2. Optimization
    with tqdm(total=maxFE, desc="Optimization Progress", unit="eval") as pbar:
        while FE <= maxFE:

            # Step 2.1. Generate new solutions
            sols = []  # solutions
            objs = []  # objectives
            for _ in range(npop):
                co = None  # the current operation
                temp_sol = []
                temp_p = precedence.copy()
                temp_v = v.copy()
                temp_q = q.copy()

                for k in range(nops):
                    cs = np.where(temp_q == 1)[0]  # the candidate set
                    VN = []  # the valid node
                    for op in cs:
                        VN += indices[ind2op[op]].keys()
                    if k == 0:
                        temp_sol.append(np.random.choice(VN))
                    else:
                        probability = np.zeros(len(VN))
                        o1, m1, t1, d1 = co.split('&')
                        for i in range(len(VN)):
                            o2, m2, t2, d2 = VN[i].split('&')
                            cost = indices[o2][VN[i]]
                            if objective == 'cost':
                                if m1 != m2:
                                    cost += mcc
                                if m1 != m2 or t1 != t2:
                                    cost += tcc
                                if m1 != m2 or d1 != d2:
                                    cost += scc
                            else:
                                if m1 != m2:
                                    cost += mct[m1][m2]
                                if m1 != m2 or t1 != t2:
                                    cost += tct
                                if m1 != m2 or d1 != d2:
                                    cost += sct
                            heuristic = 1 / cost
                            pheromone = tau[CO2ind[co], CO2ind[VN[i]]]
                            probability[i] = pheromone ** alpha * heuristic ** beta
                        probability /= np.sum(probability)
                        chosen_node = np.random.choice(VN, p=probability)
                        temp_sol.append(chosen_node)

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
                    co = temp_sol[-1]
                FE += 1
                pbar.update(1)
                temp_obj = cal_objective(temp_sol, specifications)
                sols.append(temp_sol)
                objs.append(temp_obj)
                if temp_obj < gbest:
                    gbest = temp_obj
                    gbest_sol = temp_sol.copy()
                    conFE = FE

            # Step 2.2. Update pheromone
            tau *= (1 - rho)
            for i in range(npop):
                temp_sol = sols[i]
                temp_obj = objs[i]
                for j in range(nops - 1):
                    node1, node2 = temp_sol[j], temp_sol[j + 1]
                    node1_ind, node2_ind = CO2ind[node1], CO2ind[node2]
                    tau[node1_ind, node2_ind] += W / temp_obj

    # Step 3. Output
    return gbest, gbest_sol, conFE
