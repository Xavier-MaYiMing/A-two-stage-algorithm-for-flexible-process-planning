# Flexible Process Planning (FPP) Algorithms

This repository contains the official code for the paper titled **"Balancing optimality and efficiency in solving flexible process planning: A parameter-free two-stage algorithm"** published in ***International Journal of Production Research***.

![](https://github.com/Xavier-MaYiMing/A-two-stage-algorithm-for-flexible-process-planning/blob/main/framework.png)

The repository includes all test cases and the metaheuristics used in the study, including:

- **Ant Colony Optimization (ACO)** [Liu et al., 2013]
- **Feasible Sequence-Oriented Discrete Particle Swarm Optimization (FSDPSO)** [Dou et al., 2018]
- **Edge Selection Genetic Algorithm (ESGA)** [Su et al., 2018]
- **Hybrid Evolutionary Algorithm (HEA)** [Liu et al., 2021]
- **Sequence Learning Harmony Search (SLHS)** [Luo, 2022]
- **Two-Stage Variable Neighborhood Search (TS-VNS)** (proposed in this paper)
- **Improved FSDPSO (IFSDPSO)** (enhanced with the second-stage algorithm proposed in this paper)
- **Improved ESGA (IESGA)** (enhanced with the second-stage algorithm proposed in this paper)
- **Improved SLHS (ISLHS)** (enhanced with the second-stage algorithm proposed in this paper)

## Introduction

The FPP problem is a complex optimization problem, where the objective is to minimize the overall cost, time, or other objectives related to manufacturing processes. This repository provides multiple optimization algorithms to solve different FPP cases.

### Table: The details of adopted cases.

| Case                            | Objective | Alternative Operations | $n_f$ | $n_o$ | $n_m$ | $n_t$ | $n_d$ |
| ------------------------------- | --------- | ---------------------- | ----- | ----- | ----- | ----- | ----- |
| case 1 [Ma et al., 2000]        | cost      | ✓                      | 9     | 17    | 5     | 15    | 6     |
| case 2 [Li et al., 2002]        | cost      | ✗                      | 14    | 20    | 4     | 10    | 8     |
| case 3 [Guo et al., 2006]       | cost      | ✗                      | 14    | 14    | 3     | 8     | 6     |
| case 4 [Li et al., 2007]        | time      | ✗                      | 15    | 16    | 4     | 12    | 6     |
| case 5 [Li et al., 2007]        | time      | ✗                      | 11    | 14    | 5     | 12    | 6     |
| case 6 [Wang et al., 2009]      | cost      | ✗                      | 7     | 9     | 5     | 8     | 6     |
| case 7 [Wang et al., 2012]      | cost      | ✗                      | 13    | 18    | 5     | 16    | 6     |
| case 8 [Huang et al., 2017]     | cost      | ✗                      | 28    | 46    | 10    | 28    | 12    |
| case 9 [Petrovic et al., 2016]  | cost      | ✓                      | 9     | 25    | 8     | 12    | 6     |
| case 10 [Petrovic et al., 2016] | time      | ✓                      | 9     | 25    | 8     | 12    | 6     |
| case 11 [Luo et al., 2023]      | cost      | ✓                      | 18    | 30    | 6     | 19    | 8     |
| case 12 [Luo et al., 2023]      | time      | ✓                      | 18    | 30    | 6     | 19    | 8     |
| case 13 (large-scale)           | cost      | ✗                      | -     | 72    | 5     | 10    | 7     |
| case 14 (large-scale)           | cost      | ✗                      | -     | 61    | 6     | 11    | 7     |
| case 15 (large-scale)           | cost      | ✗                      | -     | 72    | 10    | 12    | 7     |
| case 16 (large-scale)           | cost      | ✗                      | -     | 79    | 9     | 15    | 7     |
| case 17 (large-scale)           | cost      | ✗                      | -     | 55    | 8     | 11    | 7     |
| case 18 (large-scale)           | cost      | ✗                      | -     | 89    | 7     | 11    | 7     |
| case 19 (large-scale)           | cost      | ✗                      | -     | 85    | 9     | 10    | 7     |
| case 20 (large-scale)           | cost      | ✗                      | -     | 98    | 6     | 15    | 7     |
| case 21 (large-scale)           | cost      | ✗                      | -     | 88    | 8     | 15    | 7     |
| case 22 (large-scale)           | cost      | ✗                      | -     | 72    | 7     | 10    | 7     |
| case 23 (large-scale)           | cost      | ✓                      | -     | 67    | 7     | 14    | 7     |
| case 24 (large-scale)           | cost      | ✓                      | -     | 91    | 10    | 14    | 7     |

## Folder Structure

The folder structure of the project is as follows:

```plaintext
src/
│
├── ACO.py              # Ant Colony Optimization
├── ESGA.py             # Edge Selection Genetic Algorithm
├── FPP_cases.py        # Contains FPP test cases and case loading function
├── FSDPSO.py           # Feasible Sequence Discrete Particle Swarm Optimization
├── HEA.py              # Hybrid Evolutionary Algorithm
├── IFSDPSO.py          # Improved FSDPSO
├── IESGA.py            # Improved ESGA
├── ISLHS.py            # Improved SLHS
├── SLHS.py             # Sequence Learning Harmony Search 
├── TS_VNS.py           # Two-Stage Variable Neighborhood Search (This paper)
└── main.py             # Main script for running the algorithms
```

## How to Use

You can run any algorithm by executing `main.py` and specifying the algorithm and case index. The default algorithm is `TS-VNS` and the default case is `case 1`.

### Example Usage

To solve FPP `case 1` using `TS-VNS` algorithm:

```
python main.py --algo TS-VNS --case_idx 1
```

### Available Options

- `--algo`: Specify which algorithm to use (e.g., `ACO`, `FSDPSO`, `ESGA`, `HEA`, `SLHS`, `TS-VNS`, `IFSDPSO`, `IESGA`, `ISLHS`)
- `--case_idx`: Specify which test case to solve (e.g., 1, ..., 24)

### Example Output

When running the script, you will see output like:

```
Solving FPP case 1 using the TS-VNS algorithm.
Optimization Progress: 17036eval [00:04, 3430.79eval/s]                         
The best objective: 833
The best process plan: ['o13a&m2&t1&+z', 'o2a&m2&t1&+z', 'o1a&m2&t1&+z', 'o4&m2&t1&-z', 'o5&m2&t15&-z', 'o6&m2&t10&-z', 'o9&m2&t10&-z', 'o10&m2&t14&-z', 'o7&m2&t14&-z', 'o8&m2&t3&-z', 'o12&m2&t3&-z', 'o11&m2&t3&-z', 'o3a&m2&t4&+y']
The convergence iteration: 256
```

## References

1. Liu, X., Yi, H., & Ni, Z. (2013). Application of ant colony optimization algorithm in process planning optimization. *Journal of Intelligent Manufacturing*, 24, 1-13.
2. Dou, J., Li, J., & Su, C. (2018). A discrete particle swarm optimisation for operation sequencing in CAPP. *International Journal of Production Research*, 56(11), 3795-3814.
3. Su, Y., Chu, X., Chen, D., & Sun, X. (2018). A genetic algorithm for operation sequencing in CAPP using edge selection based encoding strategy. *Journal of Intelligent Manufacturing*, 29, 313-332.
4. Liu, Q., Li, X., & Gao, L. (2021). Mathematical modeling and a hybrid evolutionary algorithm for process planning. *Journal of Intelligent Manufacturing*, 32, 781-797. 
5. Luo, K. (2022). A sequence learning harmony search algorithm for the flexible process planning problem. *International Journal of Production Research*, 60(10), 3182-3200. [Taylor & Francis]
6. Ma, G.H., Zhang, Y.F., & Nee, A.Y.C. (2000). A simulated annealing-based optimization algorithm for process planning. *International Journal of Production Research*, 38(12), 2671-2687. 
7. Li, W.D., Ong, S.K., & Nee, A.Y.C. (2002). Hybrid genetic algorithm and simulated annealing approach for the optimization of process plans for prismatic parts. *International Journal of Production Research*, 40(8), 1899-1922.
8. Guo, Y.W., Mileham, A.R., Owen, G.W., & Li, W.D. (2006). Operation sequencing optimization using a particle swarm optimization approach. *Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering Manufacture*, 220(12), 1945-1958. 
9. Li, W.D., & McMahon, C.A. (2007). A simulated annealing-based optimization approach for integrated process planning and scheduling. *International Journal of Computer Integrated Manufacturing*, 20(1), 80-95.
10. Wang, Y.F., Zhang, Y.F., & Fuh, J.Y.H. (2009). Using hybrid particle swarm optimization for process planning problem. In *2009 International Joint Conference on Computational Sciences and Optimization* (Vol. 1, pp. 304-308).
11. Wang, Y.F., Zhang, Y.F., & Fuh, J.Y.H. (2012). A hybrid particle swarm based method for process planning optimisation. *International Journal of Production Research*, 50(1), 277-292.


13. Huang, W., Lin, W., & Xu, S. (2017). Application of graph theory and hybrid GA-SA for operation sequencing in a dynamic workshop environment. *Computer-Aided Design and Applications*, 14(2), 148-159. 
14. Petrović, M., Mitić, M., Vuković, N., & Miljković, Z. (2016). Chaotic particle swarm optimization algorithm for flexible process planning. *The International Journal of Advanced Manufacturing Technology*, 85, 2535-2555. 
15. Luo, K., Shen, G., Li, L., & Sun, J. (2023). 0-1 mathematical programming models for flexible process planning. *European Journal of Operational Research*, 308(3), 1160-1175.

---

If you use any code from this repository in your work, please cite the following article:

```bibtex
@article{ma2025balancing,
  title={Balancing optimality and efficiency in solving flexible process planning: A parameter-free two-stage algorithm},
  author={Ma, Yiming and Luo, Kaiping and Chou, Mabel C and Sun, Jianfei},
  journal={International Journal of Production Research},
  pages={1--18},
  year={2025},
  publisher={Taylor \& Francis}
}
