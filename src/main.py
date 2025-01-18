import ACO
import FSDPSO
import ESGA
import HEA
import SLHS
import TS_VNS
import IFSDPSO
import IESGA
import ISLHS
import FPP_cases


def solve_FPP(algo='TS-VNS', case_idx=1):
    specifications = FPP_cases.load_case(case_idx)
    maxFE = 1000 * len(specifications['operations'])
    
    if algo == 'ACO':
        """
        Ant colony optimization
        
        Reference:
            Liu X, Yi H, Ni Z. Application of ant colony optimization algorithm in process planning optimization[J]. 
            Journal of Intelligent Manufacturing, 2013, 24: 1-13.
            
        Parameters:
            - npop: population size (default = 100)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - rho: pheromone evaporation rate (default = 0.1)
            - W: pheromone increase (default = 100)
            - alpha: pheromone importance (default = 1)
            - beta: heuristic importance (default = 2)
            - tau0: initial pheromone value (default = 100)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = ACO.main(npop=100, maxFE=maxFE, rho=0.1, W=100, alpha=1, beta=2, tau0=100, specifications=specifications)

    elif algo == 'FSDPSO':
        """
        Feasible sequence oriented discrete particle swarm optimization

        Reference:
            Dou J, Li J, Su C. A discrete particle swarm optimisation for operation sequencing in CAPP[J]. International 
            Journal of Production Research, 2018, 56(11): 3795-3814.

        Parameters:
            - npop: population size (default = 500)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - c1: personal learning factor (default = 2)
            - c2: global learning factor (default = 2)
            - w: inertia weight (default = 0.9)
            - k1: the first parameter in adaptive mutation probability (default = 0.5)
            - k2: the second parameter in adaptive mutation probability (default = 0.005)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = FSDPSO.main(npop=500, maxFE=maxFE, c1=2, c2=2, w=0.9, k1=0.5, k2=0.005, specifications=specifications)

    elif algo == 'ESGA':
        """
        Edge selection genetic algorithm

        Reference:
            Su Y, Chu X, Chen D, et al. A genetic algorithm for operation sequencing in CAPP using edge selection based 
            encoding strategy[J]. Journal of Intelligent Manufacturing, 2018, 29: 313-332.

        Parameters:
            - npop: population size (default = 150)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - pc: crossover probability (default = 0.8)
            - pm: mutation probability (default = 0.2)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = ESGA.main(npop=150, maxFE=maxFE, pc=0.8, pm=0.2, specifications=specifications)
        
    elif algo == 'HEA':
        """
        Hybrid evolutionary algorithm

        Reference:
            Liu Q, Li X, Gao L. Mathematical modeling and a hybrid evolutionary algorithm for process planning[J]. 
            Journal of Intelligent Manufacturing, 2021, 32: 781-797.

        Parameters:
            - npop: population size (default = 400)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - pc: crossover probability (default = 0.8)
            - pm: mutation probability (default = 0.1)
            - T0: the initial temperature for simulated annealing (default = 1000)
            - alpha: cooling rate (default = 0.99)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = HEA.main(npop=400, maxFE=maxFE, pc=0.8, pm=0.1, T0=1000, alpha=0.99, specifications=specifications)
    
    elif algo == 'SLHS':
        """
        Sequence learning harmony search

        Reference:
            Luo K. A sequence learning harmony search algorithm for the flexible process planning problem[J]. 
            International Journal of Production Research, 2022, 60(10): 3182-3200.

        Parameters:
            - hms: harmony memory size (default = 10)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = SLHS.main(hms=10, maxFE=maxFE, specifications=specifications)
    
    elif algo == 'TS-VNS':
        """
        Two-stage variable neighborhood search (this paper)

        Parameters:
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = TS_VNS.main(maxFE=maxFE, specifications=specifications)
    
    elif algo == 'IFSDPSO':
        """
        Improved FSDPSO by the second-stage algorithm proposed in this paper

        Parameters:
            - npop: population size (default = 500)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - c1: personal learning factor (default = 2)
            - c2: global learning factor (default = 2)
            - w: inertia weight (default = 0.9)
            - k1: the first parameter in adaptive mutation probability (default = 0.5)
            - k2: the second parameter in adaptive mutation probability (default = 0.005)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = IFSDPSO.main(npop=500, maxFE=maxFE, c1=2, c2=2, w=0.9, k1=0.5, k2=0.005, specifications=specifications)
    
    elif algo == 'IESGA':
        """
        Improved ESGA by the second-stage algorithm proposed in this paper

        Parameters:
            - npop: population size (default = 150)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = IESGA.main(npop=150, maxFE=maxFE, specifications=specifications)
        
    elif algo == 'ISLHS':
        """
        Improved SLHS by the second-stage algorithm proposed in this paper

        Parameters:
            - hms: harmony memory size (default = 10)
            - maxFE: the maximum function evaluations (default = 1000 * the number of operations)
            - specifications: the specifications of FPP
        """
        best_obj, best_sol, conFE = ISLHS.main(hms=10, maxFE=maxFE, specifications=specifications)

    else:
        raise ValueError("Invalid algorithm name.")
    
    print('The best objective: ' + str(best_obj))
    print('The best process plan: ' + str(best_sol))
    print('The convergence iteration: ' + str(conFE))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description="Solve the flexible process planning problem")
    parser.add_argument('--algo', type=str, default='TS-VNS', help='Algorithm to use')
    parser.add_argument('--case_idx', type=int, default=1, help='Case index to solve')

    args = parser.parse_args()
    print(f"Solving FPP case {args.case_idx} using the {args.algo} algorithm.")
    solve_FPP(args.algo, args.case_idx)
