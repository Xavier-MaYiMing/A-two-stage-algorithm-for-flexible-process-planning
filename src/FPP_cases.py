# The cases of flexible process planning problems


class Operation:
    def __init__(self, machine, tool, direction, prior, process_time=None):
        self.machine = machine
        self.tool = tool
        self.direction = direction
        self.prior = prior
        self.time = process_time


def load_case(case_idx):
    specifications = {}

    if case_idx == 1:
        """
        Case 1: cost minimization

        Reference:
            Ma G H, Zhang Y F, Nee A Y C. (2000). A simulated annealing-based optimization algorithm for process planning.
            International Journal of Production Research, 38(12), 2671-2687.

        Details:
            - the number of operations: 17
            - the number of machines: 5
            - the number of tools: 15
            - the number of directions: 6
            - alternative operations: Y
        """
        case_type = {'objective': 'cost', 'alternative': True}

        # machine usage cost
        muc = {'m1': 70, 'm2': 35, 'm3': 10, 'm4': 40, 'm5': 85}
        # tool usage cost
        tuc = {'t1': 10, 't2': 10, 't3': 10, 't4': 12, 't5': 8, 't6': 16, 't7': 3, 't8': 3, 't9': 4, 't10': 2,
               't11': 10, 't12': 5, 't13': 6, 't14': 3, 't15': 6}
        # machine changeover cost
        mcc = 150
        # tool changeover cost
        tcc = 20
        # setup changeover cost
        scc = 90

        # operations
        o1a = Operation(['m1', 'm2'], ['t1', 't3'], ['+z'], ['o2a', 'o2b', 'o13a', 'o13b'])
        o1b = Operation(['m4', 'm5'], ['t5', 't15'], ['+z'], ['o2a', 'o2b', 'o13a', 'o13b'])
        o2a = Operation(['m1', 'm2'], ['t1', 't2', 't3', 't4'], ['+z'], [])
        o2b = Operation(['m4', 'm5'], ['t5'], ['+z'], [])
        o3a = Operation(['m1', 'm2'], ['t4'], ['+y', '-y'], [])
        o3b = Operation(['m4', 'm5'], ['t11'], ['+x', '-z'], [])
        o4 = Operation(['m1', 'm2'], ['t1', 't2', 't4'], ['-z'], [])
        o5 = Operation(['m1', 'm2'], ['t15'], ['-z'], ['o4'])
        o6 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t10'], ['-z'], ['o1a', 'o1b', 'o4'])
        o7 = Operation(['m1', 'm2', 'm3', 'm5'], ['t14'], ['-z'], ['o1a', 'o1b', 'o4', 'o6'])
        o8 = Operation(['m1', 'm2'], ['t3'], ['-z'], ['o1a', 'o1b', 'o4', 'o7'])
        o9 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t10'], ['-z'], [])
        o10 = Operation(['m1', 'm2', 'm4', 'm5'], ['t14'], ['-z'], ['o9'])
        o11 = Operation(['m1', 'm2'], ['t3'], ['-z'], ['o10'])
        o12 = Operation(['m1', 'm2'], ['t1', 't2', 't3', 't4'], ['-z'], ['o6', 'o7', 'o8'])
        o13a = Operation(['m1', 'm2'], ['t1', 't2', 't3', 't4'], ['+z'], [])
        o13b = Operation(['m4', 'm5'], ['t5'], ['+z'], [])
        operations = {'o1a': o1a, 'o1b': o1b, 'o2a': o2a, 'o2b': o2b, 'o3a': o3a, 'o3b': o3b, 'o4': o4, 'o5': o5,
                      'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10, 'o11': o11, 'o12': o12, 'o13a': o13a, 
                      'o13b': o13b}

        # alternatives
        alternative_operations = {
            'o1a': {'o1b'},
            'o1b': {'o1a'},
            'o2a': {'o2b'},
            'o2b': {'o2a'},
            'o3a': {'o3b'},
            'o3b': {'o3a'},
            'o13a': {'o13b'},
            'o13b': {'o13a'},
        }
        alternatives = [{'o1a', 'o1b'}, {'o2a', 'o2b'}, {'o3a', 'o3b'}, {'o13a', 'o13b'}]

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 2:
        """
        Case 2: cost minimization

        Reference:
            Li W D, Ong S K, Nee A Y C. Hybrid genetic algorithm and simulated annealing approach for the optimization of 
            process plans for prismatic parts[J]. International Journal of Production Research, 2002, 40(8): 1899-1922.

        Details:
            - the number of operations: 20
            - the number of machines: 14
            - the number of tools: 10
            - the number of directions: 8
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}
        
        # machine usage cost
        muc = {'m1': 10, 'm2': 40, 'm3': 100, 'm4': 60}
        # tool usage cost
        tuc = {'t1': 7, 't2': 5, 't3': 3, 't4': 8, 't5': 7, 't6': 10, 't7': 15, 't8': 30, 't9': 15, 't10': 20}
        # machine changeover cost
        mcc = 160
        # tool changeover cost
        tcc = 20
        # setup changeover cost
        scc = 100

        # operations
        o1 = Operation(['m2', 'm3'], ['t6', 't7', 't8'], ['+z'], [])
        o2 = Operation(['m2', 'm3'], ['t6', 't7', 't8'], ['-z'], ['o1'])
        o3 = Operation(['m2', 'm3'], ['t6', 't7', 't8'], ['+x'], ['o1'])
        o4 = Operation(['m1', 'm2', 'm3'], ['t2'], ['+z', '-z'], ['o1', 'o5', 'o18'])
        o5 = Operation(['m2', 'm3'], ['t6', 't7'], ['+x', '-z'], ['o1'])
        o6 = Operation(['m2', 'm3'], ['t7', 't8'], ['+y', '-z'], ['o1'])
        o7 = Operation(['m2', 'm3'], ['t7', 't8'], ['-a'], ['o1', 'o5'])
        o8 = Operation(['m1', 'm2', 'm3'], ['t2', 't3', 't4'], ['-a'], ['o1', 'o7'])
        o9 = Operation(['m1', 'm2', 'm3'], ['t9'], ['-a'], ['o1', 'o7', 'o8'])
        o10 = Operation(['m3', 'm4'], ['t10'], ['-a'], ['o1', 'o7', 'o8', 'o9'])
        o11 = Operation(['m2', 'm3'], ['t7', 't8'], ['-y', '-z'], ['o1'])
        o12 = Operation(['m1', 'm2', 'm3'], ['t2', 't3', 't4'], ['-z'], ['o1', 'o2', 'o6', 'o11'])
        o13 = Operation(['m1', 'm2', 'm3'], ['t9'], ['-z'], ['o1', 'o2', 'o6', 'o11', 'o12'])
        o14 = Operation(['m3', 'm4'], ['t10'], ['-z'], ['o1', 'o2', 'o6', 'o11', 'o12', 'o13'])
        o15 = Operation(['m1', 'm2', 'm3'], ['t1'], ['-z'], ['o1', 'o2', 'o12', 'o13', 'o14'])
        o16 = Operation(['m1', 'm2', 'm3'], ['t5'], ['-z'], ['o1', 'o2', 'o12', 'o13', 'o14', 'o15'])
        o17 = Operation(['m2', 'm3'], ['t7', 't8'], ['-x'], ['o1', 'o18'])
        o18 = Operation(['m2', 'm3'], ['t6', 't7'], ['-x', '-z'], ['o1'])
        o19 = Operation(['m1', 'm2', 'm3'], ['t9'], ['+z'], ['o1', 'o12'])
        o20 = Operation(['m3', 'm4'], ['t10'], ['+z'], ['o1', 'o12', 'o19'])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10, 'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 
                      'o18': o18, 'o19': o19, 'o20': o20}

        # alternatives
        alternative_operations = {}
        alternatives = []
        
        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 3:
        """
        Case 3: cost minimization

        Reference:
            Guo Y W, Mileham A R, Owen G W, et al. Operation sequencing optimization using a particle swarm optimization
             approach[J]. Proceedings of the Institution of Mechanical Engineers, Part B: Journal of Engineering 
             Manufacture, 2006, 220(12): 1945-1958.

        Details:
            - the number of operations: 14
            - the number of machines: 3
            - the number of tools: 8
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}
        
        # machine usage cost
        muc = {'m1': 10, 'm2': 35, 'm3': 60}
        # tool usage cost
        tuc = {'t1': 3, 't2': 3, 't3': 8, 't4': 15, 't5': 10, 't6': 15, 't7': 10, 't8': 10}
        # machine changeover cost
        mcc = 160
        # tool changeover cost
        tcc = 20
        # setup changeover cost
        scc = 120

        # operations
        o1 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z', '-z'], [])
        o2 = Operation(['m2', 'm3'], ['t8'], ['-x', '+y', '-y', '-z'], ['o1'])
        o3 = Operation(['m2', 'm3'], ['t5', 't6'], ['+y'], [])
        o4 = Operation(['m2'], ['t5', 't6'], ['+y'], ['o3'])
        o5 = Operation(['m2', 'm3'], ['t5', 't6'], ['+y', '-z'], [])
        o6 = Operation(['m1', 'm2', 'm3'], ['t2'], ['+z', '-z'], [])
        o7 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z', '-z'], ['o6'])
        o8 = Operation(['m2', 'm3'], ['t5', 't6'], ['+x'], [])
        o9 = Operation(['m1', 'm2', 'm3'], ['t1'], ['-z'], [])
        o10 = Operation(['m2', 'm3'], ['t5', 't6'], ['-y'], [])
        o11 = Operation(['m2', 'm3'], ['t5', 't7'], ['-y'], ['o10'])
        o12 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z', '-z'], [])
        o13 = Operation(['m2', 'm3'], ['t5', 't6'], ['-x', '-y'], [])
        o14 = Operation(['m1', 'm2', 'm3'], ['t1'], ['-y'], ['o13'])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10, 'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14}

        # alternatives
        alternative_operations = {}
        alternatives = []
        
        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 4:
        """
        Case 4: time minimization

        Reference:
            Li W D, McMahon C A. A simulated annealing-based optimization approach for integrated process planning and 
            scheduling[J]. International Journal of Computer Integrated Manufacturing, 2007, 20(1): 80-95.

        Details:
            - the number of operations: 16
            - the number of machines: 4
            - the number of tools: 12
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'time', 'alternative': False}
        
        # machine changeover time
        mct = {
            'm1': {'m2': 140, 'm3': 140, 'm4': 140},
            'm2': {'m1': 140, 'm3': 140, 'm4': 140},
            'm3': {'m1': 140, 'm2': 140, 'm4': 140},
            'm4': {'m1': 140, 'm2': 140, 'm3': 140},
        }
        # tool changeover time
        tct = 20
        # setup changeover time
        sct = 120

        # operations
        o1 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['+z', '-z'], ['o16'], [12, 10, 10, 7.5])
        o2 = Operation(['m2', 'm3', 'm4'], ['t12'], ['-x', '+y', '-y', '-z'], ['o1', 'o16'], [20, 20, 15])
        o3 = Operation(['m2', 'm3', 'm4'], ['t5', 't6', 't11'], ['+y'], ['o16'], [18, 18, 13.5])
        o4 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+y'], ['o3', 'o16'], [16, 16, 12])
        o5 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+y', '-z'], ['o16'], [15, 15, 11.25])
        o6 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2'], ['+z', '-z'], ['o16'], [30, 25, 25, 18.75])
        o7 = Operation(['m2', 'm3', 'm4'], ['t9'], ['+z', '-z'], ['o6', 'o16'], [25, 25, 18.75])
        o8 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['+z', '-z'], ['o6', 'o7', 'o9', 'o16'], [14.4, 12, 12, 9])
        o9 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+x'], ['o16'], [15, 15, 11.25])
        o10 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['-z'], ['o9', 'o12', 'o16'], [9.6, 8, 8, 6])
        o11 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['-y'], ['o16'], [10, 10, 7.5])
        o12 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['-y'], ['o11', 'o16'], [10, 10, 7.5])
        o13 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['+z', '-z'], ['o11', 'o16'], [9.6, 8, 8, 6])
        o14 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['-x', '-y'], ['o16'], [16, 16, 12])
        o15 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['-y'], ['o14', 'o16'], [9.6, 8, 8, 6])
        o16 = Operation(['m1', 'm2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+x', '-x', '+y', '-y', '-z'], [], [36, 30, 30, 22.5])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10, 'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16}

        # alternatives
        alternative_operations = {}
        alternatives = []
        
        specifications['type'] = case_type
        specifications['mct'] = mct
        specifications['tct'] = tct
        specifications['sct'] = sct
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 5:
        """
        Case 5: time minimization

        Reference:
            Li W D, McMahon C A. A simulated annealing-based optimization approach for integrated process planning and 
            scheduling[J]. International Journal of Computer Integrated Manufacturing, 2007, 20(1): 80-95.

        Details:
            - the number of operations: 14
            - the number of machines:  4
            - the number of tools: 12
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'time', 'alternative': False}

        # machine changeover time
        mct = {
            'm1': {'m2': 140, 'm3': 140, 'm4': 140, 'm5': 140},
            'm2': {'m1': 140, 'm3': 140, 'm4': 140, 'm5': 140},
            'm3': {'m1': 140, 'm2': 140, 'm4': 140, 'm5': 140},
            'm4': {'m1': 140, 'm2': 140, 'm3': 140, 'm5': 140},
            'm5': {'m1': 140, 'm2': 140, 'm3': 140, 'm4': 140},
        }
        # tool changeover time
        tct = 20
        # setup changeover time
        sct = 120

        # operations
        o1 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+z'], [], [20, 20, 15])
        o2 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['-z'], ['o1'], [20, 20, 15])
        o3 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+x', '-x', '+y', '-z'], ['o1', 'o2'], [15, 15, 11.25])
        o4 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2'], ['+x', '-x', '+y', '+z'], ['o1', 'o2'], [15, 15, 11.25, 18])
        o5 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8'], ['+x', '-x', '-y', '-z'], ['o1', 'o2'], [15, 15, 11.25])
        o6 = Operation(['m2', 'm3', 'm4'], ['t7', 't8'], ['+x', '-x', '-y', '+z'], ['o1', 'o2'], [15, 15, 11.25])
        o7 = Operation(['m2', 'm3', 'm4'], ['t7', 't8', 't11'], ['+x', '-x', '-z'], ['o1', 'o2', 'o9', 'o10', 'o11'], [15, 15, 11.25])
        o8 = Operation(['m2', 'm3', 'm4'], ['t6', 't7', 't8', 't11'], ['+x', '-x', '-z'], ['o1', 'o2', 'o9', 'o10', 'o11'], [25, 25, 18.75])
        o9 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2', 't3', 't4'], ['+z', '-z'], ['o1', 'o2'], [30, 25, 25, 18.75])
        o10 = Operation(['m2', 'm3', 'm4'], ['t9'], ['+z', '-z'], ['o1', 'o2', 'o9'], [20, 20, 15])
        o11 = Operation(['m2', 'm3', 'm4', 'm5'], ['t10'], ['+z', '-z'], ['o1', 'o2', 'o10'], [20, 20, 15, 24])
        o12 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1'], ['+y', '-y'], ['o1', 'o2', 'o3', 'o4', 'o5', 'o6'], [9.6, 8, 8, 6])
        o13 = Operation(['m2', 'm3', 'm4'], ['t5'], ['+y', '-y'], ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o12'], [8, 8, 6])
        o14 = Operation(['m1', 'm2', 'm3', 'm4'], ['t9'], ['+z', '-z'], ['o1', 'o2', 'o3', 'o4', 'o5', 'o6'], [6, 5, 5, 3.75])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10, 'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14}

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['mct'] = mct
        specifications['tct'] = tct
        specifications['sct'] = sct
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 6:
        """
        Case 6: cost minimization

        Reference:
            Wang Y F, Zhang Y F, Fuh J Y H. Using hybrid particle swarm optimization for process planning problem[C]
            //2009 International Joint Conference on Computational Sciences and Optimization. IEEE, 2009, 1: 304-308.

        Details:
            - the number of operations: 9
            - the number of machines: 5
            - the number of tools: 8
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 70, 'm2': 35, 'm3': 10, 'm4': 40, 'm5': 85}
        # tool usage cost
        tuc = {'t1': 5, 't2': 10, 't3': 20, 't4': 8, 't5': 10, 't6': 5, 't7': 8, 't8': 6}
        # machine changeover cost
        mcc = 200
        # tool changeover cost
        tcc = 30
        # setup changeover cost
        scc = 60

        # operations
        o1 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't4', 't5'], ['-x', '-z'], [])
        o2 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't5', 't8'], ['+y', '-z'], ['o1'])
        o3 = Operation(['m1', 'm2'], ['t1', 't3'], ['+y'], ['o1'])
        o4 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't5'], ['+x', '-x', '+z'], ['o1'])
        o5 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t7'], ['+z', '-z'], ['o1'])
        o6 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t6'], ['+z', '-z'], ['o1', 'o5'])
        o7 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t7'], ['+z', '-z'], ['o1'])
        o8 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t6'], ['+z', '-z'], ['o1', 'o7'])
        o9 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't5'], ['-x'], ['o1'])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9}

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 7:
        """
        Case 7: cost minimization

        Reference:
            Ma G H, Zhang Y F, Nee A Y C. (2000). A simulated annealing-based optimization algorithm for process planning.
            International Journal of Production Research, 38(12), 2671-2687.

        Details:
            - the number of operations:
            - the number of machines:
            - the number of tools:
            - the number of directions:
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 20, 'm2': 50, 'm3': 40, 'm4': 25, 'm5': 55}
        # tool usage cost
        tuc = {'t1': 3, 't2': 4, 't3': 5, 't4': 6, 't5': 7, 't6': 3, 't7': 3, 't8': 4, 't9': 6, 't10': 7, 't11': 8,
               't12': 8, 't13': 8, 't14': 2, 't15': 4, 't16': 5}
        # machine changeover cost
        mcc = 200
        # tool changeover cost
        tcc = 30
        # setup changeover cost
        scc = 60

        # operations
        o1 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't4', 't5'], ['+x', '-z'], [])
        o2 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't4', 't5'], ['+x', '-z'], [])
        o3 = Operation(['m1', 'm2'], ['t1', 't3'], ['-z'], ['o7', 'o13'])
        o4 = Operation(['m1', 'm2'], ['t1', 't3'], ['-z'], ['o7', 'o15'])
        o5 = Operation(['m1', 'm2'], ['t1', 't3'], ['-z'], ['o3', 'o7', 'o15'])
        o6 = Operation(['m1', 'm2'], ['t1', 't3'], ['-z'], ['o4', 'o7', 'o13'])
        o7 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t14'], ['+z', '-z'], [])
        o8 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t11'], ['+z', '-z'], ['o7'])
        o9 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t14'], ['+z', '-z'], ['o1', 'o18'])
        o10 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t6'], ['+z', '-z'], ['o9'])
        o11 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t14'], ['+z', '-z'], ['o2', 'o17'])
        o12 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t6'], ['+z', '-z'], ['o11'])
        o13 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t14'], ['+x', '-x'], ['o1', 'o2'])
        o14 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t9'], ['+x', '-x'], ['o13'])
        o15 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t14'], ['+x', '-x'], ['o1', 'o2'])
        o16 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t9'], ['+x', '-x'], ['o15'])
        o17 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't4', 't5'], ['-x', '+z'], [])
        o18 = Operation(['m1', 'm2', 'm4', 'm5'], ['t1', 't2', 't3', 't4', 't5'], ['+x', '+z'], [])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10,
                      'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18}

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 8:
        """
        Case 8: cost minimization

        Reference:
            Huang W, Lin W, Xu S. Application of graph theory and hybrid GA-SA for operation sequencing in a dynamic 
            workshop environment[J]. Computer-Aided Design and Applications, 2017, 14(2): 148-159.

        Details:
            - the number of operations: 46
            - the number of machines: 10
            - the number of tools: 28
            - the number of directions: 12
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 20, 'm2': 45, 'm3': 50, 'm4': 55, 'm5': 20, 'm6': 80, 'm7': 45, 'm8': 48, 'm9': 16, 'm10': 18}
        # tool usage cost
        tuc = {'t1': 5, 't2': 6, 't3': 7, 't4': 12, 't5': 13, 't6': 9, 't7': 8, 't8': 9, 't9': 10, 't10': 4, 't11': 4,
               't12': 3,
               't13': 4, 't14': 3, 't15': 4, 't16': 3, 't17': 4, 't18': 2, 't19': 2, 't20': 4, 't21': 3, 't22': 5,
               't23': 3,
               't24': 4, 't25': 4, 't26': 3, 't27': 4, 't28': 3}
        # machine changeover cost
        mcc = 120
        # tool changeover cost
        tcc = 15
        # setup changeover cost
        scc = 90

        # operations
        o1 = Operation(['m1', 'm2'], ['t1', 't2', 't3'], ['+z'], [])
        o2 = Operation(['m2'], ['t1', 't2', 't3'], ['+z'], ['o22'])
        o3 = Operation(['m2'], ['t1', 't2', 't3'], ['+z'], ['o2'])
        o4 = Operation(['m7', 'm8'], ['t4'], ['+y', '-y'], ['o3', 'o27'])
        o5 = Operation(['m6', 'm7', 'm8'], ['t5'], ['+y', '-y'], ['o4'])
        o6 = Operation(['m6', 'm7', 'm8'], ['t5'], ['+y', '-y'], ['o5'])
        o7 = Operation(['m5', 'm7', 'm8'], ['t7', 't8', 't9'], ['-a'], ['o3', 'o28'])
        o8 = Operation(['m3', 'm4', 'm6'], ['t7', 't8', 't9'], ['-a'], ['o7', 'o31', 'o33'])
        o9 = Operation(['m3', 'm4', 'm5'], ['t8', 't9'], ['+z'], ['o22'])
        o10 = Operation(['m3', 'm4', 'm5'], ['t8', 't9'], ['-z'], ['o1'])
        o11 = Operation(['m3', 'm4', 'm5'], ['t8', 't9'], ['-z'], ['o1'])
        o12 = Operation(['m4', 'm5'], ['t8', 't9'], ['-z'], ['o3', 'o11'])
        o13 = Operation(['m3', 'm4', 'm5'], ['t8', 't9'], ['-z'], ['o1'])
        o14 = Operation(['m3', 'm4', 'm5'], ['t8', 't9'], ['-z'], ['o1'])
        o15 = Operation(['m3', 'm4', 'm5'], ['t7', 't8'], ['-z'], ['o3'])
        o16 = Operation(['m3', 'm4', 'm5'], ['t7', 't8'], ['-z'], ['o15'])
        o17 = Operation(['m3', 'm4', 'm6', 'm7'], ['t7', 't8'], ['-b'], ['o3'])
        o18 = Operation(['m3', 'm4', 'm6', 'm7'], ['t7', 't8'], ['-b'], ['o17'])
        o19 = Operation(['m3', 'm4', 'm6', 'm7'], ['t7', 't8'], ['-b'], ['o3'])
        o20 = Operation(['m3', 'm4', 'm6', 'm7'], ['t7', 't8'], ['-b'], ['o19'])
        o21 = Operation(['m9', 'm10'], ['t10'], ['+z', '-z'], ['o9', 'o12'])
        o22 = Operation(['m4', 'm5'], ['t7', 't8', 't9'], ['-z'], ['o1'])
        o23 = Operation(['m9', 'm10'], ['t20'], ['-z'], ['o27'])
        o24 = Operation(['m9', 'm10'], ['t11'], ['+z'], ['o3'])
        o25 = Operation(['m9', 'm10'], ['t22'], ['+z'], ['o24'])
        o26 = Operation(['m9', 'm10'], ['t12'], ['+z'], ['o3'])
        o27 = Operation(['m9', 'm10'], ['t13'], ['+z'], ['o3'])
        o28 = Operation(['m9', 'm10'], ['t14'], ['+z'], ['o3'])
        o29 = Operation(['m7', 'm8'], ['t6'], ['-y'], ['o3'])
        o30 = Operation(['m6', 'm7', 'm8'], ['t6'], ['-y'], ['o29'])
        o31 = Operation(['m7', 'm8', 'm9', 'm10'], ['t15'], ['-a'], ['o7'])
        o32 = Operation(['m7', 'm8', 'm9', 'm10'], ['t16'], ['-a'], ['o7'])
        o33 = Operation(['m7', 'm8', 'm9', 'm10'], ['t23'], ['-a'], ['o32'])
        o34 = Operation(['m6', 'm7', 'm8'], ['t28'], ['-c'], ['o22'])
        o35 = Operation(['m6', 'm7', 'm8'], ['t24'], ['-c'], ['o34'])
        o36 = Operation(['m6', 'm7', 'm8'], ['t17'], ['-c'], ['o22'])
        o37 = Operation(['m6', 'm7', 'm8'], ['t25'], ['-c'], ['o36'])
        o38 = Operation(['m3', 'm4', 'm9', 'm10'], ['t21'], ['-z'], ['o25'])
        o39 = Operation(['m9', 'm10'], ['t18'], ['-b'], ['o4', 'o18'])
        o40 = Operation(['m9', 'm10'], ['t26'], ['-b'], ['o39'])
        o41 = Operation(['m9', 'm10'], ['t18'], ['-b'], ['o20', 'o29'])
        o42 = Operation(['m9', 'm10'], ['t26'], ['-b'], ['o41'])
        o43 = Operation(['m3', 'm4', 'm9', 'm10'], ['t18'], ['-z'], ['o16'])
        o44 = Operation(['m3', 'm4', 'm9', 'm10'], ['t26'], ['-z'], ['o43'])
        o45 = Operation(['m6', 'm7', 'm8'], ['t19'], ['-x'], ['o28'])
        o46 = Operation(['m6', 'm7', 'm8'], ['t27'], ['-x'], ['o45'])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9,
                      'o10': o10, 'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17,
                      'o18': o18, 'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25,
                      'o26': o26, 'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33,
                      'o34': o34, 'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41,
                      'o42': o42, 'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46}

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 9:
        """
        Case 9: cost minimization

        Reference:
            Petrović M, Mitić M, Vuković N, et al. Chaotic particle swarm optimization algorithm for flexible process 
            planning[J]. The International Journal of Advanced Manufacturing Technology, 2016, 85: 2535-2555.

        Details:
            - the number of operations: 25
            - the number of machines: 8
            - the number of tools: 12
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': True}

        # machine usage cost
        muc = {'m1': 30, 'm2': 10, 'm3': 30, 'm4': 40, 'm5': 100, 'm6': 60, 'm7': 10, 'm8': 15}
        # tool usage cost
        tuc = {'t1': 10, 't2': 10, 't3': 10, 't4': 10, 't5': 15, 't6': 5, 't7': 15, 't8': 20, 't9': 30, 't10': 12,
               't11': 30, 't12': 15}
        # machine changeover cost
        mcc = 160
        # tool changeover cost
        tcc = 20
        # setup changeover cost
        scc = 100

        # operations
        o1 = Operation(['m1', 'm2', 'm3'], ['t1', 't2'], ['+z'], [], [2.3, 3.3, 4.6, 6.5, 3.8, 5.5])
        o20 = Operation(['m4', 'm5', 'm6'], ['t9', 't10'], ['+x', '-x', '+y', '-y'], [], [2.7, 2.8, 2.9, 2.4, 2.9, 2.4])
        o21 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+z'], [], [5.7, 4.2, 2.8])
        o2 = Operation(['m1', 'm2', 'm3'], ['t3', 't4'], ['+z'], ['o1', 'o20', 'o21'], [1.2, 1.0, 1.9, 1.5, 2.0, 1.6])
        o22 = Operation(['m5', 'm6'], ['t10'], ['+z'], ['o1', 'o20', 'o21'], [3.1, 3.2])
        o3 = Operation(['m7', 'm8'], ['t6'], ['+z', '-z'], [], [5.5, 3.8])
        o6 = Operation(['m1', 'm2', 'm3'], ['t6'], ['+z', '-z'], [], [3.3, 4.8, 3.3])
        o18 = Operation(['m5', 'm6'], ['t6'], ['+z', '-z'], [], [3.3, 3.4])
        o4 = Operation(['m7', 'm8'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [54.8, 38.1])
        o7 = Operation(['m1', 'm2', 'm3'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [13.4, 26.6, 30.2])
        o19 = Operation(['m5', 'm6'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [10.7, 24.1])
        o5 = Operation(['m7', 'm8'], ['t8'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [34.3, 13.7])
        o8 = Operation(['m1', 'm2', 'm3'], ['t5'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [1.1, 1.5, 1.8])
        o23 = Operation(['m5', 'm6'], ['t8'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [30.2, 13.4])
        o9 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z'], ['o5', 'o8', 'o23'], [0.6, 0.7, 0.8])
        o24 = Operation(['m5', 'm6'], ['t12'], ['+z'], ['o5', 'o8', 'o23'], [0.4, 0.5])
        o10 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z'], ['o5', 'o8', 'o23'], [0.7, 0.8, 0.9])
        o25 = Operation(['m5', 'm6'], ['t12'], ['+z'], ['o5', 'o8', 'o23'], [0.5, 0.6])
        o11 = Operation(['m1', 'm2', 'm3'], ['t1', 't2'], ['-z'], [], [2.3, 3.3, 4.6, 6.5, 3.8, 5.5])
        o12 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+x', '-x', '+y', '-y'], [], [5.7, 4.2, 2.8])
        o15 = Operation(['m4', 'm5', 'm6'], ['t9', 't10'], ['-z'], [], [2.7, 2.8, 2.9, 2.4, 2.8, 2.5])
        o13 = Operation(['m1', 'm2', 'm3'], ['t1', 't3', 't4'], ['-z'], ['o11', 'o12', 'o15'], [0.5, 0.7, 0.4, 1.0, 1.4, 0.8, 0.8, 1.1, 0.7])
        o16 = Operation(['m5', 'm6'], ['t9'], ['-z'], ['o11', 'o12', 'o15'], [4.6, 7.2])
        o14 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+x', '-x', '+y', '-y'], ['o13', 'o16'], [10.8, 9.7, 7.4])
        o17 = Operation(['m4', 'm5', 'm6'], ['t9'], ['-z'], ['o13', 'o16'], [4.3, 3.5, 6.8])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
                      'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
                      'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25}

        # alternatives
        alternative_operations = {
            'o1': {'o20', 'o21'},
            'o20': {'o1', 'o21'},
            'o21': {'o1', 'o20'},
            'o2': {'o22'},
            'o22': {'o2'},
            'o3': {'o6', 'o18'},
            'o6': {'o3', 'o18'},
            'o18': {'o3', 'o6'},
            'o4': {'o7', 'o19'},
            'o7': {'o4', 'o19'},
            'o19': {'o4', 'o7'},
            'o5': {'o8', 'o23'},
            'o8': {'o5', 'o23'},
            'o23': {'o5', 'o8'},
            'o9': {'o24'},
            'o24': {'o9'},
            'o25': {'o10'},
            'o10': {'o25'},
            'o11': {'o12', 'o15'},
            'o12': {'o11', 'o15'},
            'o15': {'o11', 'o12'},
            'o13': {'o16'},
            'o16': {'o13'},
            'o14': {'o17'},
            'o17': {'o14'},
        }
        alternatives = [{'o1', 'o20', 'o21'}, {'o2', 'o22'}, {'o3', 'o6', 'o18'}, {'o4', 'o7', 'o19'},
                        {'o5', 'o8', 'o23'}, {'o9', 'o24'}, {'o10', 'o25'}, {'o11', 'o12', 'o15'}, {'o13', 'o16'},
                        {'o14', 'o17'}]

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 10:
        """
        Case 10: time minimization

        Reference:
            Petrović M, Mitić M, Vuković N, et al. Chaotic particle swarm optimization algorithm for flexible process 
            planning[J]. The International Journal of Advanced Manufacturing Technology, 2016, 85: 2535-2555.

        Details:
            - the number of operations: 25
            - the number of machines: 8
            - the number of tools: 12
            - the number of directions: 6
            - alternative operations: N
        """
        case_type = {'objective': 'time', 'alternative': True}

        # machine changeover time
        mct = {
            'm1': {'m2': 4, 'm3': 8, 'm4': 10, 'm5': 12, 'm6': 5, 'm7': 6, 'm8': 14},
            'm2': {'m1': 4, 'm3': 3, 'm4': 7, 'm5': 11, 'm6': 5, 'm7': 4, 'm8': 6},
            'm3': {'m1': 8, 'm2': 3, 'm4': 5, 'm5': 7, 'm6': 9, 'm7': 8, 'm8': 4},
            'm4': {'m1': 10, 'm2': 7, 'm3': 5, 'm5': 4, 'm6': 14, 'm7': 12, 'm8': 6},
            'm5': {'m1': 12, 'm2': 11, 'm3': 7, 'm4': 4, 'm6': 18, 'm7': 12, 'm8': 10},
            'm6': {'m1': 5, 'm2': 5, 'm3': 9, 'm4': 14, 'm5': 18, 'm7': 6, 'm8': 8},
            'm7': {'m1': 6, 'm2': 4, 'm3': 8, 'm4': 12, 'm5': 12, 'm6': 6, 'm8': 3},
            'm8': {'m1': 14, 'm2': 6, 'm3': 4, 'm4': 6, 'm5': 10, 'm6': 8, 'm7': 3},
        }
        # tool changeover time
        tct = 60
        # setup changeover time
        sct = 50

        # operations
        o1 = Operation(['m1', 'm2', 'm3'], ['t1', 't2'], ['+z'], [], [2.3, 3.3, 4.6, 6.5, 3.8, 5.5])
        o20 = Operation(['m4', 'm5', 'm6'], ['t9', 't10'], ['+x', '-x', '+y', '-y'], [], [2.7, 2.8, 2.9, 2.4, 2.9, 2.4])
        o21 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+z'], [], [5.7, 4.2, 2.8])
        o2 = Operation(['m1', 'm2', 'm3'], ['t3', 't4'], ['+z'], ['o1', 'o20', 'o21'], [1.2, 1.0, 1.9, 1.5, 2.0, 1.6])
        o22 = Operation(['m5', 'm6'], ['t10'], ['+z'], ['o1', 'o20', 'o21'], [3.1, 3.2])
        o3 = Operation(['m7', 'm8'], ['t6'], ['+z', '-z'], [], [5.5, 3.8])
        o6 = Operation(['m1', 'm2', 'm3'], ['t6'], ['+z', '-z'], [], [3.3, 4.8, 3.3])
        o18 = Operation(['m5', 'm6'], ['t6'], ['+z', '-z'], [], [3.3, 3.4])
        o4 = Operation(['m7', 'm8'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [54.8, 38.1])
        o7 = Operation(['m1', 'm2', 'm3'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [13.4, 26.6, 30.2])
        o19 = Operation(['m5', 'm6'], ['t7'], ['+z', '-z'], ['o3', 'o6', 'o18'], [10.7, 24.1])
        o5 = Operation(['m7', 'm8'], ['t8'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [34.3, 13.7])
        o8 = Operation(['m1', 'm2', 'm3'], ['t5'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [1.1, 1.5, 1.8])
        o23 = Operation(['m5', 'm6'], ['t8'], ['+z'], ['o1', 'o4', 'o7', 'o19', 'o20', 'o21'], [30.2, 13.4])
        o9 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z'], ['o5', 'o8', 'o23'], [0.6, 0.7, 0.8])
        o24 = Operation(['m5', 'm6'], ['t12'], ['+z'], ['o5', 'o8', 'o23'], [0.4, 0.5])
        o10 = Operation(['m1', 'm2', 'm3'], ['t1'], ['+z'], ['o5', 'o8', 'o23'], [0.7, 0.8, 0.9])
        o25 = Operation(['m5', 'm6'], ['t12'], ['+z'], ['o5', 'o8', 'o23'], [0.5, 0.6])
        o11 = Operation(['m1', 'm2', 'm3'], ['t1', 't2'], ['-z'], [], [2.3, 3.3, 4.6, 6.5, 3.8, 5.5])
        o12 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+x', '-x', '+y', '-y'], [], [5.7, 4.2, 2.8])
        o15 = Operation(['m4', 'm5', 'm6'], ['t9', 't10'], ['-z'], [], [2.7, 2.8, 2.9, 2.4, 2.8, 2.5])
        o13 = Operation(['m1', 'm2', 'm3'], ['t1', 't3', 't4'], ['-z'], ['o11', 'o12', 'o15'], [0.5, 0.7, 0.4, 1.0, 1.4, 0.8, 0.8, 1.1, 0.7])
        o16 = Operation(['m5', 'm6'], ['t9'], ['-z'], ['o11', 'o12', 'o15'], [4.6, 7.2])
        o14 = Operation(['m4', 'm5', 'm6'], ['t11'], ['+x', '-x', '+y', '-y'], ['o13', 'o16'], [10.8, 9.7, 7.4])
        o17 = Operation(['m4', 'm5', 'm6'], ['t9'], ['-z'], ['o13', 'o16'], [4.3, 3.5, 6.8])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
                      'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
                      'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25}

        # alternatives
        alternative_operations = {
            'o1': {'o20', 'o21'},
            'o20': {'o1', 'o21'},
            'o21': {'o1', 'o20'},
            'o2': {'o22'},
            'o22': {'o2'},
            'o3': {'o6', 'o18'},
            'o6': {'o3', 'o18'},
            'o18': {'o3', 'o6'},
            'o4': {'o7', 'o19'},
            'o7': {'o4', 'o19'},
            'o19': {'o4', 'o7'},
            'o5': {'o8', 'o23'},
            'o8': {'o5', 'o23'},
            'o23': {'o5', 'o8'},
            'o9': {'o24'},
            'o24': {'o9'},
            'o25': {'o10'},
            'o10': {'o25'},
            'o11': {'o12', 'o15'},
            'o12': {'o11', 'o15'},
            'o15': {'o11', 'o12'},
            'o13': {'o16'},
            'o16': {'o13'},
            'o14': {'o17'},
            'o17': {'o14'},
        }
        alternatives = [{'o1', 'o20', 'o21'}, {'o2', 'o22'}, {'o3', 'o6', 'o18'}, {'o4', 'o7', 'o19'},
                        {'o5', 'o8', 'o23'}, {'o9', 'o24'}, {'o10', 'o25'}, {'o11', 'o12', 'o15'}, {'o13', 'o16'},
                        {'o14', 'o17'}]

        specifications['type'] = case_type
        specifications['mct'] = mct
        specifications['tct'] = tct
        specifications['sct'] = sct
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 11:
        """
        Case 11: cost minimization

        Reference:
            Luo K, Shen G, Li L, et al. 0-1 mathematical programming models for flexible process planning[J]. European 
            Journal of Operational Research, 2023, 308(3): 1160-1175.

        Details:
            - the number of operations: 30
            - the number of machines: 6
            - the number of tools: 19
            - the number of directions: 8
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': True}

        # machine usage cost
        muc = {'m1': 70, 'm2': 35, 'm3': 10, 'm4': 40, 'm5': 85, 'm6': 60}
        # tool usage cost
        tuc = {'t1': 5, 't2': 10, 't3': 20, 't4': 8, 't5': 10, 't6': 5, 't7': 8, 't8': 6, 't9': 6.5, 't10': 8,
               't11': 12, 't12': 20, 't13': 10, 't14': 6, 't15': 8, 't16': 12, 't17': 7.5, 't18': 14, 't19': 5}
        # machine changeover cost
        mcc = 150
        # tool changeover cost
        tcc = 20
        # setup changeover cost
        scc = 90

        # operations
        o1 = Operation(['m4', 'm5'], ['t1'], ['-z'], [], [40, 40])
        o2 = Operation(['m1', 'm2'], ['t2'], ['-z'], [], [60, 65])
        o3 = Operation(['m4', 'm5'], ['t1'], ['+y', '-y'], ['o1', 'o2'], [50, 40])
        o4 = Operation(['m1', 'm2'], ['t3'], ['+y', '-y'], ['o1', 'o2'], [40, 60])
        o5 = Operation(['m4', 'm5'], ['t1'], ['+x', '-x'], ['o1', 'o2'], [50, 40])
        o6 = Operation(['m1', 'm2'], ['t3'], ['+x', '-x'], ['o1', 'o2'], [40, 60])
        o7 = Operation(['m1'], ['t3', 't6'], ['+a', '-a'], ['o3', 'o4', 'o5', 'o6'], [35, 20])
        o8 = Operation(['m1'], ['t3', 't6'], ['+a', '-a'], ['o3', 'o4', 'o5', 'o6'], [20, 15])
        o9 = Operation(['m4', 'm5'], ['t1'], ['+z'], ['o1', 'o2'], [40, 40])
        o10 = Operation(['m1', 'm2'], ['t2'], ['+z'], ['o1', 'o2'], [60, 65])
        o11 = Operation(['m1', 'm2'], ['t4'], ['+y', '-y'], ['o9', 'o10'], [80, 70])
        o12 = Operation(['m1', 'm2'], ['t4'], ['+x', '-x'], ['o9', 'o10'], [80, 70])
        o13 = Operation(['m4', 'm5'], ['t2'], ['+y', '-y'], ['o9', 'o10'], [50, 40])
        o14 = Operation(['m1', 'm2'], ['t2'], ['+y', '-y'], ['o9', 'o10'], [40, 60])
        o15 = Operation(['m1', 'm2'], ['t5'], ['-y'], ['o13', 'o14'], [180, 150])
        o16 = Operation(['m1', 'm2'], ['t7'], ['+x'], ['o9', 'o10'], [15, 20])
        o17 = Operation(['m1', 'm2'], ['t7'], ['+x'], ['o9', 'o10'], [45, 60])
        o18 = Operation(['m1', 'm3', 'm5'], ['t8', 't9'], ['-z'], ['o15'], [50, 45, 40, 35, 35, 30])
        o19 = Operation(['m1', 'm5'], ['t7'], ['-z'], ['o18'], [100, 80])
        o20 = Operation(['m1', 'm5'], ['t5'], ['-y'], ['o16'], [75, 60])
        o21 = Operation(['m1', 'm3', 'm5'], ['t10', 't11'], ['-z'], ['o20'], [100, 90, 80, 70, 70, 60])
        o22 = Operation(['m1', 'm5'], ['t3'], ['-z'], ['o21'], [100, 80])
        o23 = Operation(['m1', 'm5'], ['t12', 't13'], ['+x'], ['o9', 'o10'], [70, 55, 60, 45])
        o24 = Operation(['m1', 'm3', 'm5'], ['t14'], ['-z'], ['o17'], [60, 40, 50])
        o25 = Operation(['m1', 'm5'], ['t15'], ['+a', '-a'], ['o24'], [42.5, 40])
        o26 = Operation(['m6'], ['t16'], ['+a', '-a'], ['o24'], [35])
        o27 = Operation(['m1', 'm5'], ['t17'], ['+a', '-a'], ['o25', 'o26'], [50, 45])
        o28 = Operation(['m6'], ['t18'], ['+a', '-a'], ['o25', 'o26'], [37.5])
        o29 = Operation(['m1', 'm5'], ['t19'], ['+z', '-z'], ['o13', 'o14'], [20, 30])
        o30 = Operation(['m1', 'm5'], ['t19'], ['+y', '-y'], ['o3', 'o4', 'o5', 'o6', 'o7', 'o8'], [20, 30])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
                      'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
                      'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
                      'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30}

        # alternatives
        alternative_operations = {
            'o1': {'o2'},
            'o2': {'o1'},
            'o3': {'o4'},
            'o4': {'o3'},
            'o5': {'o6'},
            'o6': {'o5'},
            'o9': {'o10'},
            'o10': {'o9'},
            'o13': {'o14'},
            'o14': {'o13'},
            'o25': {'o26'},
            'o26': {'o25'},
            'o27': {'o28'},
            'o28': {'o27'},
        }
        alternatives = [{'o1', 'o2'}, {'o3', 'o4'}, {'o5', 'o6'}, {'o9', 'o10'}, {'o13', 'o14'}, {'o25', 'o26'},
                        {'o27', 'o28'}]

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 12:
        """
        Case 12: time minimization

        Reference:
            Luo K, Shen G, Li L, et al. 0-1 mathematical programming models for flexible process planning[J]. European 
            Journal of Operational Research, 2023, 308(3): 1160-1175.

        Details:
            - the number of operations: 30
            - the number of machines: 6
            - the number of tools: 19
            - the number of directions: 8
            - alternative operations: N
        """
        case_type = {'objective': 'time', 'alternative': True}

        # machine changeover time
        mct = {
            'm1': {'m2': 140, 'm3': 140, 'm4': 140, 'm5': 140, 'm6': 140},
            'm2': {'m1': 140, 'm3': 140, 'm4': 140, 'm5': 140, 'm6': 140},
            'm3': {'m1': 140, 'm2': 140, 'm4': 140, 'm5': 140, 'm6': 140},
            'm4': {'m1': 140, 'm2': 140, 'm3': 140, 'm5': 140, 'm6': 140},
            'm5': {'m1': 140, 'm2': 140, 'm3': 140, 'm4': 140, 'm6': 140},
            'm6': {'m1': 140, 'm2': 140, 'm3': 140, 'm4': 140, 'm5': 140},
        }
        # tool changeover time
        tct = 15
        # setup changeover time
        sct = 60

        # operations
        o1 = Operation(['m4', 'm5'], ['t1'], ['-z'], [], [40, 40])
        o2 = Operation(['m1', 'm2'], ['t2'], ['-z'], [], [60, 65])
        o3 = Operation(['m4', 'm5'], ['t1'], ['+y', '-y'], ['o1', 'o2'], [50, 40])
        o4 = Operation(['m1', 'm2'], ['t3'], ['+y', '-y'], ['o1', 'o2'], [40, 60])
        o5 = Operation(['m4', 'm5'], ['t1'], ['+x', '-x'], ['o1', 'o2'], [50, 40])
        o6 = Operation(['m1', 'm2'], ['t3'], ['+x', '-x'], ['o1', 'o2'], [40, 60])
        o7 = Operation(['m1'], ['t3', 't6'], ['+a', '-a'], ['o3', 'o4', 'o5', 'o6'], [35, 20])
        o8 = Operation(['m1'], ['t3', 't6'], ['+a', '-a'], ['o3', 'o4', 'o5', 'o6'], [20, 15])
        o9 = Operation(['m4', 'm5'], ['t1'], ['+z'], ['o1', 'o2'], [40, 40])
        o10 = Operation(['m1', 'm2'], ['t2'], ['+z'], ['o1', 'o2'], [60, 65])
        o11 = Operation(['m1', 'm2'], ['t4'], ['+y', '-y'], ['o9', 'o10'], [80, 70])
        o12 = Operation(['m1', 'm2'], ['t4'], ['+x', '-x'], ['o9', 'o10'], [80, 70])
        o13 = Operation(['m4', 'm5'], ['t2'], ['+y', '-y'], ['o9', 'o10'], [50, 40])
        o14 = Operation(['m1', 'm2'], ['t2'], ['+y', '-y'], ['o9', 'o10'], [40, 60])
        o15 = Operation(['m1', 'm2'], ['t5'], ['-y'], ['o13', 'o14'], [180, 150])
        o16 = Operation(['m1', 'm2'], ['t7'], ['+x'], ['o9', 'o10'], [15, 20])
        o17 = Operation(['m1', 'm2'], ['t7'], ['+x'], ['o9', 'o10'], [45, 60])
        o18 = Operation(['m1', 'm3', 'm5'], ['t8', 't9'], ['-z'], ['o15'], [50, 45, 40, 35, 35, 30])
        o19 = Operation(['m1', 'm5'], ['t7'], ['-z'], ['o18'], [100, 80])
        o20 = Operation(['m1', 'm5'], ['t5'], ['-y'], ['o16'], [75, 60])
        o21 = Operation(['m1', 'm3', 'm5'], ['t10', 't11'], ['-z'], ['o20'], [100, 90, 80, 70, 70, 60])
        o22 = Operation(['m1', 'm5'], ['t3'], ['-z'], ['o21'], [100, 80])
        o23 = Operation(['m1', 'm5'], ['t12', 't13'], ['+x'], ['o9', 'o10'], [70, 55, 60, 45])
        o24 = Operation(['m1', 'm3', 'm5'], ['t14'], ['-z'], ['o17'], [60, 40, 50])
        o25 = Operation(['m1', 'm5'], ['t15'], ['+a', '-a'], ['o24'], [42.5, 40])
        o26 = Operation(['m6'], ['t16'], ['+a', '-a'], ['o24'], [35])
        o27 = Operation(['m1', 'm5'], ['t17'], ['+a', '-a'], ['o25', 'o26'], [50, 45])
        o28 = Operation(['m6'], ['t18'], ['+a', '-a'], ['o25', 'o26'], [37.5])
        o29 = Operation(['m1', 'm5'], ['t19'], ['+z', '-z'], ['o13', 'o14'], [20, 30])
        o30 = Operation(['m1', 'm5'], ['t19'], ['+y', '-y'], ['o3', 'o4', 'o5', 'o6', 'o7', 'o8'], [20, 30])
        operations = {'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
                      'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
                      'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
                      'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30}

        # alternatives
        alternative_operations = {
            'o1': {'o2'},
            'o2': {'o1'},
            'o3': {'o4'},
            'o4': {'o3'},
            'o5': {'o6'},
            'o6': {'o5'},
            'o9': {'o10'},
            'o10': {'o9'},
            'o13': {'o14'},
            'o14': {'o13'},
            'o25': {'o26'},
            'o26': {'o25'},
            'o27': {'o28'},
            'o28': {'o27'},
        }
        alternatives = [{'o1', 'o2'}, {'o3', 'o4'}, {'o5', 'o6'}, {'o9', 'o10'}, {'o13', 'o14'}, {'o25', 'o26'},
                        {'o27', 'o28'}]

        specifications['type'] = case_type
        specifications['mct'] = mct
        specifications['tct'] = tct
        specifications['sct'] = sct
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 13:
        """
        Case 13: cost minimization

        Details:
            - the number of operations: 72
            - the number of machines: 5
            - the number of tools: 10
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 19, 'm2': 30, 'm3': 53, 'm4': 13, 'm5': 82}
        # tool usage cost
        tuc = {'t1': 8, 't2': 5, 't3': 13, 't4': 16, 't5': 7, 't6': 19, 't7': 10, 't8': 14, 't9': 9, 't10': 20}
        # machine changeover cost
        mcc = 424
        # tool changeover cost
        tcc = 19
        # setup changeover cost
        scc = 86

        # operations
        o1 = Operation(['m2', 'm3'], ['t1', 't3', 't5'], ['-2'], ['o6'])
        o2 = Operation(['m5'], ['t3', 't7', 't8'], ['-3', '-1', '0'], ['o39'])
        o3 = Operation(['m4'], ['t4'], ['3'], [])
        o4 = Operation(['m1', 'm2'], ['t2', 't8'], ['-3', '-1', '2'], ['o25', 'o58'])
        o5 = Operation(['m3'], ['t8'], ['-3'], [])
        o6 = Operation(['m1'], ['t1', 't2'], ['-3', '-1', '2'], [])
        o7 = Operation(['m1', 'm2', 'm3', 'm4'], ['t1', 't2', 't3', 't8', 't10'], ['3'], ['o62'])
        o8 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t5', 't6', 't9'], ['-2', '-1', '0', '1'], ['o20'])
        o9 = Operation(['m1', 'm2', 'm5'], ['t10'], ['0', '1'], [])
        o10 = Operation(['m2', 'm3', 'm4', 'm5'], ['t6', 't9'], ['-3', '-1'], ['o37'])
        o11 = Operation(['m1', 'm3'], ['t3', 't6'], ['-3', '-1', '2', '3'], [])
        o12 = Operation(['m3', 'm4', 'm5'], ['t3', 't4', 't7', 't8'], ['-3', '-2'], [])
        o13 = Operation(['m1', 'm2', 'm4'], ['t5', 't7'], ['-3', '0', '3'], ['o65'])
        o14 = Operation(['m3', 'm5'], ['t5', 't8'], ['-2', '-1', '2'], ['o19', 'o55', 'o56'])
        o15 = Operation(['m2', 'm5'], ['t1', 't10'], ['0', '2', '3'], ['o39'])
        o16 = Operation(['m1', 'm5'], ['t3', 't8', 't9'], ['-2'], ['o19', 'o26', 'o62'])
        o17 = Operation(['m4', 'm5'], ['t9'], ['-3'], ['o25'])
        o18 = Operation(['m4'], ['t10'], ['-1', '0', '3'], [])
        o19 = Operation(['m1', 'm2', 'm5'], ['t1', 't3', 't5'], ['0', '1'], ['o37'])
        o20 = Operation(['m2', 'm4'], ['t2', 't4', 't6'], ['-1', '2', '3'], ['o67'])
        o21 = Operation(['m4'], ['t3', 't7', 't10'], ['-1', '1', '2'], ['o7'])
        o22 = Operation(['m1', 'm3', 'm5'], ['t6'], ['0', '2'], [])
        o23 = Operation(['m5'], ['t4', 't6', 't10'], ['-3', '1', '3'], ['o29'])
        o24 = Operation(['m1'], ['t1', 't5', 't8'], ['2'], [])
        o25 = Operation(['m4'], ['t4', 't6', 't9', 't10'], ['1'], [])
        o26 = Operation(['m4'], ['t7'], ['-3', '0'], [])
        o27 = Operation(['m5'], ['t8', 't9'], ['-1', '0', '3'], ['o39'])
        o28 = Operation(['m4'], ['t4'], ['0', '1'], ['o46'])
        o29 = Operation(['m3', 'm4'], ['t3', 't8'], ['-3', '1', '2'], [])
        o30 = Operation(['m1', 'm2', 'm5'], ['t4', 't6', 't8', 't9'], ['-1', '0', '1'], [])
        o31 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2', 't8', 't9'], ['-1', '0'], [])
        o32 = Operation(['m1', 'm5'], ['t1', 't3', 't7', 't10'], ['0', '1'], [])
        o33 = Operation(['m1'], ['t1', 't6', 't10'], ['-2', '-1', '1', '2'], [])
        o34 = Operation(['m5'], ['t6'], ['-3'], [])
        o35 = Operation(['m2', 'm3', 'm5'], ['t3', 't6', 't7', 't8'], ['-3', '1', '3'], [])
        o36 = Operation(['m1', 'm3', 'm4'], ['t5', 't7', 't9'], ['1'], ['o52'])
        o37 = Operation(['m1', 'm2', 'm4'], ['t3', 't5', 't6', 't7', 't9'], ['-1'], ['o27'])
        o38 = Operation(['m1', 'm2', 'm4'], ['t10'], ['2', '3'], [])
        o39 = Operation(['m1', 'm4', 'm5'], ['t2', 't4', 't7'], ['-3', '-1'], ['o54', 'o62'])
        o40 = Operation(['m5'], ['t5', 't9'], ['-2', '1'], ['o34'])
        o41 = Operation(['m1', 'm2', 'm4'], ['t3', 't5', 't6', 't9'], ['0', '1'], [])
        o42 = Operation(['m2', 'm3', 'm5'], ['t1'], ['-1'], ['o68'])
        o43 = Operation(['m1'], ['t1', 't3', 't5', 't10'], ['-2', '3'], ['o6', 'o49'])
        o44 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2', 't8', 't9'], ['2'], [])
        o45 = Operation(['m3', 'm4'], ['t9'], ['0', '1', '2', '3'], ['o3'])
        o46 = Operation(['m3', 'm4', 'm5'], ['t1', 't2', 't9', 't10'], ['-2', '3'], [])
        o47 = Operation(['m1', 'm2', 'm4'], ['t3', 't10'], ['-3'], ['o16'])
        o48 = Operation(['m1', 'm3'], ['t1', 't2', 't7'], ['-2'], [])
        o49 = Operation(['m1', 'm3', 'm5'], ['t1', 't3', 't5'], ['-2'], ['o29', 'o33'])
        o50 = Operation(['m1', 'm3', 'm5'], ['t7', 't8'], ['-3', '0', '2'], ['o7'])
        o51 = Operation(['m1', 'm2', 'm3', 'm4'], ['t9'], ['0'], ['o11', 'o58'])
        o52 = Operation(['m1', 'm3'], ['t3', 't4', 't6'], ['-3', '-1', '0', '3'], [])
        o53 = Operation(['m2', 'm3'], ['t2', 't4', 't6', 't10'], ['1', '3'], [])
        o54 = Operation(['m1', 'm2'], ['t3', 't8'], ['-3'], [])
        o55 = Operation(['m1', 'm2'], ['t3', 't4', 't10'], ['3'], ['o15', 'o24'])
        o56 = Operation(['m3', 'm4', 'm5'], ['t1', 't2'], ['-3'], [])
        o57 = Operation(['m2', 'm3', 'm4'], ['t6'], ['-3', '-1', '2'], [])
        o58 = Operation(['m2', 'm4', 'm5'], ['t5', 't9', 't10'], ['-2', '-1'], ['o31'])
        o59 = Operation(['m5'], ['t1', 't3', 't4', 't5', 't10'], ['-2', '0', '2'], ['o47'])
        o60 = Operation(['m1', 'm2', 'm4', 'm5'], ['t5', 't6', 't7'], ['-3', '-1', '0'], [])
        o61 = Operation(['m1', 'm5'], ['t4', 't7'], ['-3', '-2'], ['o62'])
        o62 = Operation(['m2', 'm3', 'm4', 'm5'], ['t3', 't5'], ['-2', '0', '1', '2'], [])
        o63 = Operation(['m5'], ['t5', 't6', 't9'], ['-2', '0'], ['o31'])
        o64 = Operation(['m1', 'm2', 'm4', 'm5'], ['t2', 't3'], ['-1'], ['o15'])
        o65 = Operation(['m1', 'm4', 'm5'], ['t3', 't5', 't10'], ['0', '2'], [])
        o66 = Operation(['m1', 'm2', 'm3', 'm4'], ['t3', 't8'], ['-2', '0', '1'], ['o59'])
        o67 = Operation(['m5'], ['t10'], ['1', '2', '3'], [])
        o68 = Operation(['m2'], ['t2', 't4', 't7'], ['0'], [])
        o69 = Operation(['m2', 'm4'], ['t3', 't5'], ['0'], [])
        o70 = Operation(['m1', 'm3', 'm4'], ['t4', 't6'], ['-2', '-1', '2', '3'], ['o42'])
        o71 = Operation(['m5'], ['t4', 't8'], ['0', '1', '2'], [])
        o72 = Operation(['m1', 'm5'], ['t7', 't8'], ['-3', '2'], ['o34'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 14:
        """
        Case 14: cost minimization

        Details:
            - the number of operations: 61
            - the number of machines: 6
            - the number of tools: 11
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 20, 'm2': 11, 'm3': 59, 'm4': 77, 'm5': 79, 'm6': 83}
        # tool usage cost
        tuc = {'t1': 15, 't2': 20, 't3': 17, 't4': 8, 't5': 19, 't6': 8, 't7': 15, 't8': 13, 't9': 8, 't10': 17,
               't11': 11}
        # machine changeover cost
        mcc = 471
        # tool changeover cost
        tcc = 10
        # setup changeover cost
        scc = 86

        # operations
        o1 = Operation(['m1', 'm5'], ['t1', 't4'], ['0'], [])
        o2 = Operation(['m2', 'm3', 'm5'], ['t4', 't5', 't10'], ['-3'], [])
        o3 = Operation(['m1', 'm3', 'm5'], ['t6', 't10'], ['-2', '3'], [])
        o4 = Operation(['m3', 'm4', 'm5', 'm6'], ['t9'], ['-1', '2'], ['o7'])
        o5 = Operation(['m2', 'm6'], ['t1', 't7', 't8', 't9'], ['0'], ['o13'])
        o6 = Operation(['m2', 'm5', 'm6'], ['t3', 't4', 't5'], ['-3'], [])
        o7 = Operation(['m1', 'm2'], ['t2', 't3', 't4'], ['-2', '3'], [])
        o8 = Operation(['m6'], ['t8', 't9', 't11'], ['-2', '-1', '0', '3'], [])
        o9 = Operation(['m1', 'm4', 'm6'], ['t9', 't10'], ['3'], ['o14'])
        o10 = Operation(['m1', 'm6'], ['t2', 't3', 't4', 't10'], ['-2', '-1', '3'], ['o26', 'o28', 'o30', 'o47'])
        o11 = Operation(['m5'], ['t1', 't2', 't4', 't6', 't11'], ['-2'], [])
        o12 = Operation(['m3'], ['t3', 't9', 't11'], ['0', '1', '3'], ['o49'])
        o13 = Operation(['m4', 'm6'], ['t4', 't5', 't6', 't10'], ['-3', '3'], [])
        o14 = Operation(['m3', 'm6'], ['t1'], ['-1', '3'], [])
        o15 = Operation(['m1', 'm2', 'm5'], ['t4'], ['-1'], ['o60'])
        o16 = Operation(['m1', 'm2', 'm3', 'm6'], ['t1', 't2', 't6', 't8'], ['-3', '-2', '0', '1'], [])
        o17 = Operation(['m4', 'm5'], ['t1', 't3', 't5'], ['-3', '-2', '1', '3'], ['o14'])
        o18 = Operation(['m1', 'm2', 'm6'], ['t3', 't6', 't9', 't10', 't11'], ['2'], [])
        o19 = Operation(['m1', 'm2'], ['t1', 't3', 't9', 't10'], ['-2', '0'], ['o52'])
        o20 = Operation(['m3', 'm4'], ['t2', 't4', 't5'], ['-3', '-1'], [])
        o21 = Operation(['m6'], ['t9', 't10', 't11'], ['-3', '0', '3'], [])
        o22 = Operation(['m1', 'm2', 'm6'], ['t3', 't5'], ['-3', '-1', '0', '3'], ['o37'])
        o23 = Operation(['m3', 'm6'], ['t5'], ['-3', '1', '3'], [])
        o24 = Operation(['m1', 'm6'], ['t1', 't6', 't8', 't9'], ['-2', '2'], ['o50'])
        o25 = Operation(['m1', 'm5'], ['t8'], ['-3', '3'], ['o48', 'o60'])
        o26 = Operation(['m1', 'm3'], ['t2', 't3', 't8'], ['-3', '1'], [])
        o27 = Operation(['m3'], ['t8'], ['-3', '-2', '1'], ['o49'])
        o28 = Operation(['m2', 'm3', 'm4', 'm6'], ['t2', 't7', 't11'], ['3'], [])
        o29 = Operation(['m1', 'm2', 'm6'], ['t7'], ['-3', '1', '2'], [])
        o30 = Operation(['m3', 'm5', 'm6'], ['t7', 't9', 't10'], ['0', '2'], [])
        o31 = Operation(['m1', 'm2'], ['t9', 't10'], ['-2'], ['o1', 'o56'])
        o32 = Operation(['m2', 'm3', 'm4', 'm6'], ['t8'], ['1', '2', '3'], [])
        o33 = Operation(['m2', 'm3', 'm6'], ['t9', 't10'], ['-3', '-2', '3'], ['o3'])
        o34 = Operation(['m1', 'm2', 'm3', 'm4', 'm6'], ['t5', 't8', 't10'], ['-1', '0'], ['o9'])
        o35 = Operation(['m4'], ['t3', 't5', 't10'], ['-2', '-1'], ['o33'])
        o36 = Operation(['m1', 'm2', 'm4', 'm6'], ['t2', 't3', 't5', 't7', 't9'], ['-1'], ['o50'])
        o37 = Operation(['m1', 'm2', 'm3', 'm4'], ['t11'], ['0', '3'], ['o40'])
        o38 = Operation(['m3', 'm4', 'm5'], ['t7', 't9', 't10', 't11'], ['1'], ['o35'])
        o39 = Operation(['m2', 'm3'], ['t1', 't2', 't4', 't6'], ['-1', '0', '2'], [])
        o40 = Operation(['m1', 'm4', 'm5'], ['t2', 't4', 't5', 't7'], ['-1', '0'], ['o13', 'o16'])
        o41 = Operation(['m2', 'm6'], ['t4', 't8', 't10', 't11'], ['-2', '-1', '3'], ['o10'])
        o42 = Operation(['m1', 'm3', 'm5', 'm6'], ['t2', 't8'], ['-3'], [])
        o43 = Operation(['m2', 'm3', 'm4'], ['t7'], ['-3', '0'], [])
        o44 = Operation(['m4'], ['t2', 't6'], ['1', '2', '3'], ['o37'])
        o45 = Operation(['m1', 'm2', 'm6'], ['t9'], ['1', '3'], [])
        o46 = Operation(['m1'], ['t4', 't7', 't8', 't11'], ['-3', '0', '3'], [])
        o47 = Operation(['m5'], ['t1', 't6'], ['-3', '-2', '1', '3'], ['o14'])
        o48 = Operation(['m2', 'm4'], ['t5', 't6', 't8', 't10'], ['-2', '2'], [])
        o49 = Operation(['m1', 'm3', 'm4', 'm5'], ['t1', 't4', 't7', 't8', 't9'], ['-1', '1', '3'], [])
        o50 = Operation(['m6'], ['t3', 't8'], ['-1', '0', '3'], ['o4', 'o41'])
        o51 = Operation(['m1', 'm4'], ['t4'], ['1'], ['o50'])
        o52 = Operation(['m1', 'm4', 'm5'], ['t4', 't5', 't8', 't9'], ['-3', '0', '1'], [])
        o53 = Operation(['m3', 'm6'], ['t4', 't8', 't9', 't10'], ['0', '1', '2', '3'], [])
        o54 = Operation(['m5', 'm6'], ['t2', 't4', 't6', 't9'], ['-2'], ['o19'])
        o55 = Operation(['m3', 'm5', 'm6'], ['t11'], ['-1', '0', '1'], ['o22'])
        o56 = Operation(['m1', 'm4', 'm6'], ['t3', 't6'], ['-3', '0'], ['o14', 'o51'])
        o57 = Operation(['m2', 'm3', 'm6'], ['t1', 't4', 't5', 't6'], ['-2', '-1'], [])
        o58 = Operation(['m2', 'm5', 'm6'], ['t4', 't6'], ['-2', '0'], [])
        o59 = Operation(['m3', 'm5'], ['t9', 't10'], ['-3'], ['o61'])
        o60 = Operation(['m5'], ['t3', 't6', 't8'], ['-3', '1'], [])
        o61 = Operation(['m2', 'm3', 'm4'], ['t2', 't11'], ['-2', '-1'], ['o38'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 15:
        """
        Case 15: cost minimization

        Details:
            - the number of operations: 72
            - the number of machines: 10
            - the number of tools: 12
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 31, 'm2': 28, 'm3': 87, 'm4': 44, 'm5': 80, 'm6': 48, 'm7': 14, 'm8': 26, 'm9': 57, 'm10': 37}
        # tool usage cost
        tuc = {'t1': 14, 't2': 15, 't3': 13, 't4': 17, 't5': 10, 't6': 9, 't7': 19, 't8': 17, 't9': 13, 't10': 12,
               't11': 15, 't12': 6}
        # machine changeover cost
        mcc = 388
        # tool changeover cost
        tcc = 14
        # setup changeover cost
        scc = 58

        # operations
        o1 = Operation(['m2', 'm4', 'm5', 'm6', 'm10'], ['t2', 't4', 't5', 't6', 't11'], ['-2', '2'], [])
        o2 = Operation(['m9'], ['t6', 't7', 't11', 't12'], ['-2'], ['o13', 'o26'])
        o3 = Operation(['m1', 'm9', 'm10'], ['t3', 't5'], ['-1', '1'], ['o6'])
        o4 = Operation(['m3', 'm5', 'm6'], ['t1', 't5', 't7'], ['-2'], [])
        o5 = Operation(['m3', 'm5', 'm7', 'm8', 'm10'], ['t2', 't12'], ['1', '3'], [])
        o6 = Operation(['m1', 'm2', 'm5', 'm7'], ['t2', 't6'], ['-2', '-1', '1', '3'], [])
        o7 = Operation(['m7', 'm8'], ['t3', 't7', 't9', 't10'], ['0', '2'], [])
        o8 = Operation(['m8'], ['t3', 't5', 't10', 't12'], ['0', '3'], [])
        o9 = Operation(['m2', 'm9', 'm10'], ['t1', 't6', 't7'], ['-1', '0', '1'], [])
        o10 = Operation(['m5', 'm8', 'm10'], ['t2', 't7', 't10', 't11'], ['0', '3'], [])
        o11 = Operation(['m3'], ['t2', 't4', 't5', 't7', 't9'], ['-1', '0'], [])
        o12 = Operation(['m3', 'm8'], ['t4', 't5', 't7', 't8'], ['2'], ['o62'])
        o13 = Operation(['m5', 'm10'], ['t4', 't12'], ['-2', '1', '3'], [])
        o14 = Operation(['m4', 'm8', 'm10'], ['t1', 't8'], ['-2', '0', '2'], ['o1', 'o7', 'o33'])
        o15 = Operation(['m6', 'm7', 'm8', 'm10'], ['t4', 't6', 't8', 't10'], ['-3', '-2', '3'], ['o56'])
        o16 = Operation(['m9'], ['t2', 't4', 't5', 't6', 't11'], ['-2', '2', '3'], ['o14'])
        o17 = Operation(['m2', 'm4', 'm9'], ['t8'], ['0'], ['o5'])
        o18 = Operation(['m7', 'm9'], ['t2', 't4', 't5', 't12'], ['3'], [])
        o19 = Operation(['m2', 'm3', 'm10'], ['t10', 't11'], ['-2'], [])
        o20 = Operation(['m3', 'm9'], ['t1', 't3', 't7', 't8'], ['-3'], ['o42'])
        o21 = Operation(['m4', 'm9'], ['t8'], ['-3'], [])
        o22 = Operation(['m6'], ['t8', 't9', 't12'], ['0'], ['o27', 'o46'])
        o23 = Operation(['m1', 'm2', 'm3', 'm8'], ['t6', 't11', 't12'], ['-2', '2'], ['o47', 'o48'])
        o24 = Operation(['m3'], ['t2', 't3', 't7', 't10'], ['1', '3'], [])
        o25 = Operation(['m7', 'm9'], ['t6', 't11'], ['-3', '0', '2'], ['o5'])
        o26 = Operation(['m1', 'm2', 'm6', 'm7'], ['t7'], ['-3', '0', '3'], ['o19', 'o53'])
        o27 = Operation(['m3'], ['t1', 't5'], ['-2', '3'], [])
        o28 = Operation(['m1', 'm4', 'm5'], ['t8', 't10'], ['-2', '1', '2'], [])
        o29 = Operation(['m1', 'm7', 'm8'], ['t2', 't3', 't9'], ['-3', '1'], ['o24'])
        o30 = Operation(['m5', 'm6', 'm8'], ['t3', 't8'], ['-1'], [])
        o31 = Operation(['m3', 'm6', 'm7'], ['t1', 't2', 't4', 't8', 't12'], ['0'], ['o55'])
        o32 = Operation(['m1', 'm2', 'm6', 'm8'], ['t2', 't5', 't6', 't8'], ['-1', '1'], ['o31'])
        o33 = Operation(['m10'], ['t5', 't10'], ['-1', '1', '3'], ['o11', 'o32', 'o47'])
        o34 = Operation(['m1', 'm7'], ['t4', 't6'], ['1', '2'], [])
        o35 = Operation(['m3', 'm5', 'm10'], ['t2', 't7', 't8', 't9', 't12'], ['-1', '3'], ['o53'])
        o36 = Operation(['m3'], ['t7', 't9'], ['-3', '-1', '0', '1'], ['o70'])
        o37 = Operation(['m7'], ['t1', 't10', 't12'], ['-3', '0', '1'], ['o58'])
        o38 = Operation(['m2', 'm3', 'm5', 'm7'], ['t2', 't11'], ['0'], ['o11'])
        o39 = Operation(['m2', 'm6', 'm7', 'm9'], ['t6', 't7'], ['-3', '0', '1', '3'], [])
        o40 = Operation(['m1', 'm9'], ['t5', 't10', 't11'], ['1', '3'], ['o13', 'o23', 'o34'])
        o41 = Operation(['m7'], ['t3', 't4', 't7', 't8', 't12'], ['0', '1', '3'], ['o17', 'o24', 'o31'])
        o42 = Operation(['m4', 'm6', 'm9', 'm10'], ['t4'], ['-3', '1'], ['o45'])
        o43 = Operation(['m1', 'm10'], ['t2', 't3', 't8', 't12'], ['-3'], ['o8'])
        o44 = Operation(['m1', 'm5', 'm6', 'm7'], ['t1', 't3'], ['-1', '2'], ['o56'])
        o45 = Operation(['m2', 'm3', 'm6'], ['t2'], ['-2', '1', '2', '3'], [])
        o46 = Operation(['m3', 'm5', 'm7'], ['t2', 't11'], ['-1', '2'], [])
        o47 = Operation(['m6', 'm7', 'm9'], ['t1'], ['-1'], ['o65'])
        o48 = Operation(['m3', 'm5'], ['t4', 't11'], ['1'], ['o18'])
        o49 = Operation(['m1', 'm6', 'm8', 'm10'], ['t3', 't5'], ['0', '1'], ['o7'])
        o50 = Operation(['m5', 'm6', 'm7', 'm9'], ['t3', 't4', 't10'], ['-2', '2'], [])
        o51 = Operation(['m3'], ['t4', 't6', 't9', 't12'], ['1'], [])
        o52 = Operation(['m10'], ['t3', 't6', 't9', 't12'], ['-3', '-1', '0'], [])
        o53 = Operation(['m2', 'm9'], ['t1', 't8', 't9', 't11'], ['-3', '-1'], ['o61'])
        o54 = Operation(['m3', 'm5', 'm6'], ['t4', 't12'], ['-3', '0', '1'], ['o35', 'o65'])
        o55 = Operation(['m4'], ['t10'], ['-3'], [])
        o56 = Operation(['m4', 'm8', 'm9'], ['t5', 't6', 't8', 't10', 't12'], ['-3', '3'], [])
        o57 = Operation(['m1', 'm4', 'm6', 'm7'], ['t5', 't8', 't9', 't11'], ['-2', '2', '3'], ['o29'])
        o58 = Operation(['m3', 'm4', 'm6', 'm7'], ['t12'], ['-3', '1'], ['o14', 'o47'])
        o59 = Operation(['m2', 'm3', 'm6', 'm7'], ['t3', 't4', 't7', 't8'], ['0', '2'], [])
        o60 = Operation(['m1', 'm3', 'm5', 'm6', 'm7'], ['t1', 't2', 't4', 't8', 't11'], ['2'], ['o21', 'o26'])
        o61 = Operation(['m1', 'm2', 'm6'], ['t2', 't4', 't8'], ['-2', '3'], [])
        o62 = Operation(['m3', 'm8', 'm10'], ['t12'], ['0', '1'], ['o31'])
        o63 = Operation(['m1', 'm3', 'm7', 'm9'], ['t10'], ['-3', '-2'], [])
        o64 = Operation(['m1', 'm5'], ['t1', 't3'], ['-3', '-1', '0'], [])
        o65 = Operation(['m3', 'm7', 'm10'], ['t5', 't6', 't10', 't11'], ['1'], [])
        o66 = Operation(['m1', 'm2', 'm3', 'm4'], ['t3', 't5', 't6', 't8'], ['-1', '2'], ['o38'])
        o67 = Operation(['m2', 'm3', 'm7', 'm9'], ['t3', 't6', 't10', 't12'], ['3'], ['o14'])
        o68 = Operation(['m3', 'm10'], ['t5'], ['0', '3'], [])
        o69 = Operation(['m2', 'm4', 'm5'], ['t1', 't2', 't11'], ['-3', '-1', '2'], ['o65'])
        o70 = Operation(['m2', 'm4', 'm6'], ['t6', 't7', 't8', 't9', 't12'], ['-1', '1'], ['o45', 'o55'])
        o71 = Operation(['m2', 'm6', 'm7', 'm8'], ['t1', 't5'], ['-2', '0'], ['o39'])
        o72 = Operation(['m3', 'm6', 'm10'], ['t6', 't8', 't9'], ['-1', '0', '2'], [])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 16:
        """
        Case 16: cost minimization

        Details:
            - the number of operations: 79
            - the number of machines: 9
            - the number of tools: 15
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 44, 'm2': 90, 'm3': 94, 'm4': 41, 'm5': 49, 'm6': 49, 'm7': 52, 'm8': 27, 'm9': 56}
        # tool usage cost
        tuc = {'t1': 9, 't2': 20, 't3': 13, 't4': 16, 't5': 14, 't6': 10, 't7': 8, 't8': 13, 't9': 8, 't10': 7,
               't11': 7, 't12': 6, 't13': 8, 't14': 16, 't15': 9}
        # machine changeover cost
        mcc = 132
        # tool changeover cost
        tcc = 28
        # setup changeover cost
        scc = 79

        # operations
        o1 = Operation(['m3', 'm4', 'm6', 'm7'], ['t5', 't12'], ['0', '1', '3'], ['o65'])
        o2 = Operation(['m1', 'm9'], ['t3', 't9', 't10', 't15'], ['0', '3'], ['o48'])
        o3 = Operation(['m4', 'm6', 'm9'], ['t2', 't5', 't7', 't10'], ['-1', '0', '2', '3'], [])
        o4 = Operation(['m1', 'm7'], ['t12'], ['2', '3'], [])
        o5 = Operation(['m4', 'm5', 'm6', 'm8', 'm9'], ['t12'], ['-3', '-2', '-1', '0'], [])
        o6 = Operation(['m4', 'm5', 'm6'], ['t6', 't8', 't12'], ['-3', '-1', '0'], [])
        o7 = Operation(['m9'], ['t8', 't9'], ['-3', '1'], ['o40'])
        o8 = Operation(['m1', 'm3', 'm7'], ['t9'], ['3'], ['o48'])
        o9 = Operation(['m1', 'm6', 'm9'], ['t9', 't13'], ['-3', '1', '3'], [])
        o10 = Operation(['m4'], ['t1', 't7', 't14'], ['-3', '-2', '2', '3'], ['o3'])
        o11 = Operation(['m1'], ['t8', 't14'], ['-2', '2'], ['o40'])
        o12 = Operation(['m4', 'm6'], ['t11'], ['0', '1', '3'], [])
        o13 = Operation(['m1', 'm5', 'm7', 'm8'], ['t2', 't5', 't13'], ['-2', '2'], [])
        o14 = Operation(['m1', 'm2', 'm3', 'm6'], ['t15'], ['0'], ['o9'])
        o15 = Operation(['m1', 'm2'], ['t14'], ['-3', '2', '3'], [])
        o16 = Operation(['m4'], ['t1', 't4'], ['-2'], ['o3', 'o13'])
        o17 = Operation(['m6', 'm8', 'm9'], ['t4', 't6', 't9', 't12'], ['1'], [])
        o18 = Operation(['m3', 'm4', 'm6'], ['t4', 't7', 't10', 't12', 't13'], ['2'], ['o38', 'o70'])
        o19 = Operation(['m3', 'm4', 'm6', 'm7', 'm9'], ['t7', 't11'], ['-2', '-1'], ['o51'])
        o20 = Operation(['m3', 'm6'], ['t6', 't9', 't10', 't11'], ['2', '3'], [])
        o21 = Operation(['m1', 'm2', 'm3', 'm6', 'm7'], ['t7', 't12'], ['0'], ['o65'])
        o22 = Operation(['m1', 'm6', 'm7'], ['t1', 't2', 't4', 't8', 't9'], ['-2'], [])
        o23 = Operation(['m9'], ['t6', 't13'], ['1', '3'], [])
        o24 = Operation(['m1', 'm3', 'm4', 'm6'], ['t7', 't13'], ['-2', '2'], ['o13'])
        o25 = Operation(['m3'], ['t9'], ['-2', '1', '2', '3'], ['o55', 'o61'])
        o26 = Operation(['m2'], ['t4', 't9'], ['-3', '0'], [])
        o27 = Operation(['m8'], ['t2', 't5', 't10', 't13'], ['-2'], [])
        o28 = Operation(['m1', 'm4', 'm8'], ['t11', 't12', 't13', 't15'], ['1'], [])
        o29 = Operation(['m2', 'm4'], ['t12'], ['-2', '-1'], ['o36'])
        o30 = Operation(['m1', 'm6', 'm7'], ['t2', 't5', 't11'], ['-2', '2', '3'], ['o26'])
        o31 = Operation(['m2', 'm4', 'm8'], ['t13'], ['-1', '1', '3'], ['o40'])
        o32 = Operation(['m8'], ['t13'], ['-3', '-1'], [])
        o33 = Operation(['m1', 'm2', 'm4', 'm5'], ['t4', 't11', 't14'], ['-3'], [])
        o34 = Operation(['m2'], ['t1', 't14', 't15'], ['0', '1', '2'], [])
        o35 = Operation(['m2', 'm3', 'm5', 'm6'], ['t4', 't7', 't9', 't13'], ['0', '2', '3'], ['o64'])
        o36 = Operation(['m2', 'm6'], ['t3', 't5', 't7', 't14'], ['-2', '0', '2'], ['o69'])
        o37 = Operation(['m1', 'm4', 'm8'], ['t6', 't9', 't13'], ['-3', '1', '2', '3'], [])
        o38 = Operation(['m1', 'm5'], ['t13'], ['-3', '-2', '3'], [])
        o39 = Operation(['m2', 'm3', 'm8'], ['t2'], ['3'], [])
        o40 = Operation(['m5', 'm6', 'm8'], ['t7', 't10'], ['3'], [])
        o41 = Operation(['m1', 'm7'], ['t6', 't9'], ['2'], [])
        o42 = Operation(['m3', 'm5', 'm7', 'm8', 'm9'], ['t2', 't4', 't5', 't11', 't12'], ['-1'], ['o52', 'o71'])
        o43 = Operation(['m3', 'm9'], ['t2', 't12'], ['-3'], ['o68'])
        o44 = Operation(['m3', 'm7', 'm9'], ['t6', 't9', 't11', 't12'], ['-1', '1'], [])
        o45 = Operation(['m1', 'm2', 'm4', 'm7'], ['t9'], ['-1', '1', '3'], ['o15', 'o61', 'o66'])
        o46 = Operation(['m4'], ['t2', 't9', 't11', 't13', 't14'], ['0'], ['o26'])
        o47 = Operation(['m6'], ['t12'], ['3'], [])
        o48 = Operation(['m5'], ['t2', 't7', 't11', 't12'], ['-1'], [])
        o49 = Operation(['m2', 'm7'], ['t2', 't11', 't12', 't13'], ['-2'], [])
        o50 = Operation(['m6'], ['t6'], ['-3', '3'], ['o75'])
        o51 = Operation(['m3', 'm4', 'm5', 'm7'], ['t1', 't3', 't12'], ['-2', '-1', '0', '1'], [])
        o52 = Operation(['m1', 'm2', 'm3', 'm4', 'm9'], ['t4'], ['-2', '0', '2'], ['o8', 'o71'])
        o53 = Operation(['m1', 'm2', 'm6', 'm9'], ['t3', 't6', 't7', 't15'], ['-1', '1', '3'], ['o7'])
        o54 = Operation(['m2', 'm3', 'm5'], ['t1', 't2'], ['-1'], [])
        o55 = Operation(['m4'], ['t1', 't2', 't5', 't11'], ['-2', '1', '2'], ['o17', 'o22'])
        o56 = Operation(['m3', 'm4', 'm5', 'm8'], ['t4', 't7', 't8', 't12'], ['-2'], ['o7'])
        o57 = Operation(['m5'], ['t2', 't8', 't9', 't11'], ['-3', '-1', '0'], [])
        o58 = Operation(['m3', 'm4'], ['t5'], ['1', '3'], ['o61', 'o79'])
        o59 = Operation(['m1', 'm3', 'm5', 'm9'], ['t2', 't6', 't10', 't12'], ['2'], [])
        o60 = Operation(['m3'], ['t10', 't11', 't12', 't15'], ['0', '1', '2'], [])
        o61 = Operation(['m4', 'm9'], ['t5', 't8', 't15'], ['3'], ['o60'])
        o62 = Operation(['m1', 'm3', 'm5', 'm7', 'm8'], ['t3', 't7', 't13', 't14', 't15'], ['-2', '0', '1', '2'],
                        ['o6', 'o11', 'o28'])
        o63 = Operation(['m1', 'm6', 'm7', 'm8', 'm9'], ['t3', 't5'], ['-1', '2'], ['o16'])
        o64 = Operation(['m6'], ['t2', 't5', 't8', 't9', 't11'], ['0', '2'], [])
        o65 = Operation(['m1', 'm2'], ['t1', 't6', 't11', 't15'], ['1', '3'], ['o48'])
        o66 = Operation(['m7', 'm8'], ['t1', 't13'], ['0'], ['o3', 'o8'])
        o67 = Operation(['m2', 'm5', 'm8'], ['t7', 't14'], ['-3', '3'], [])
        o68 = Operation(['m7'], ['t1', 't13'], ['-3', '-2', '0', '2'], [])
        o69 = Operation(['m6'], ['t5', 't9', 't11', 't12'], ['0'], [])
        o70 = Operation(['m4', 'm5', 'm7'], ['t2', 't3', 't6', 't10'], ['-2'], ['o49'])
        o71 = Operation(['m8'], ['t1', 't2', 't3', 't6', 't12'], ['1'], ['o26'])
        o72 = Operation(['m8'], ['t3', 't9', 't13'], ['3'], ['o36', 'o71'])
        o73 = Operation(['m2', 'm3', 'm5', 'm9'], ['t8', 't12'], ['3'], ['o12', 'o28'])
        o74 = Operation(['m1', 'm4'], ['t1'], ['-2', '-1', '0', '1'], ['o7', 'o61', 'o64'])
        o75 = Operation(['m4', 'm7', 'm9'], ['t9', 't11'], ['-3', '-1', '1'], ['o35'])
        o76 = Operation(['m1', 'm2', 'm3'], ['t7', 't9', 't11'], ['1'], ['o14'])
        o77 = Operation(['m5', 'm6', 'm8'], ['t1', 't3', 't9', 't10'], ['-3'], ['o58', 'o66'])
        o78 = Operation(['m3', 'm4', 'm5'], ['t7', 't11', 't14'], ['-3', '-1', '2'], [])
        o79 = Operation(['m1', 'm2'], ['t1', 't5', 't8', 't14'], ['-3', '1'], ['o12', 'o16'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 17:
        """
        Case 17: cost minimization

        Details:
            - the number of operations: 55
            - the number of machines: 8
            - the number of tools: 11
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 78, 'm2': 43, 'm3': 92, 'm4': 99, 'm5': 16, 'm6': 85, 'm7': 85, 'm8': 72}
        # tool usage cost
        tuc = {'t1': 20, 't2': 19, 't3': 13, 't4': 11, 't5': 5, 't6': 16, 't7': 16, 't8': 18, 't9': 17, 't10': 13,
               't11': 17}
        # machine changeover cost
        mcc = 122
        # tool changeover cost
        tcc = 26
        # setup changeover cost
        scc = 118

        # operations
        o1 = Operation(['m2', 'm3', 'm5', 'm7'], ['t2', 't5'], ['-2', '0', '3'], [])
        o2 = Operation(['m3', 'm8'], ['t1', 't4', 't6'], ['-2', '-1', '1', '2'], [])
        o3 = Operation(['m1'], ['t1', 't3', 't6', 't7'], ['-3', '-1', '3'], [])
        o4 = Operation(['m1'], ['t5'], ['0', '1', '3'], [])
        o5 = Operation(['m7'], ['t3'], ['-3', '-2', '2', '3'], [])
        o6 = Operation(['m3', 'm8'], ['t6', 't10'], ['-1', '3'], [])
        o7 = Operation(['m1', 'm3', 'm6', 'm7', 'm8'], ['t1', 't3', 't7', 't9'], ['0'], [])
        o8 = Operation(['m2', 'm3', 'm5'], ['t11'], ['-1', '0', '2'], ['o1'])
        o9 = Operation(['m5'], ['t1', 't2', 't7', 't10'], ['-2', '0', '3'], ['o10'])
        o10 = Operation(['m1', 'm5'], ['t4', 't6', 't7', 't11'], ['-2', '-1', '3'], ['o22'])
        o11 = Operation(['m1', 'm2', 'm4', 'm5'], ['t4', 't5', 't9', 't10', 't11'], ['-1', '3'], ['o54'])
        o12 = Operation(['m1', 'm8'], ['t1'], ['0'], ['o34'])
        o13 = Operation(['m2', 'm5'], ['t4', 't7', 't10'], ['-2', '-1', '1'], ['o54'])
        o14 = Operation(['m3'], ['t1', 't7', 't9'], ['-3', '-2', '-1', '2'], [])
        o15 = Operation(['m2', 'm4', 'm6'], ['t4'], ['-1'], [])
        o16 = Operation(['m3', 'm5'], ['t3'], ['1', '3'], [])
        o17 = Operation(['m7'], ['t5', 't9'], ['0'], [])
        o18 = Operation(['m1', 'm6'], ['t6', 't10'], ['-1', '0', '1', '3'], [])
        o19 = Operation(['m1', 'm3', 'm5'], ['t2', 't4', 't6', 't7'], ['-2', '-1', '1'], [])
        o20 = Operation(['m4', 'm5', 'm6', 'm7'], ['t8', 't10'], ['-3', '-2', '1', '2'], ['o29', 'o54'])
        o21 = Operation(['m1', 'm2', 'm7'], ['t4', 't7', 't8'], ['-3', '2', '3'], [])
        o22 = Operation(['m1', 'm2'], ['t1', 't5', 't8'], ['-2', '-1'], ['o6'])
        o23 = Operation(['m2', 'm4', 'm8'], ['t3', 't5', 't7', 't11'], ['1'], ['o48'])
        o24 = Operation(['m1', 'm3', 'm4', 'm8'], ['t1', 't10'], ['0', '1', '3'], ['o13'])
        o25 = Operation(['m1', 'm7', 'm8'], ['t4', 't8'], ['-3', '3'], ['o27'])
        o26 = Operation(['m7'], ['t1', 't3', 't5', 't11'], ['-3'], [])
        o27 = Operation(['m1', 'm5'], ['t1', 't2', 't3', 't7', 't11'], ['-3', '-2', '3'], [])
        o28 = Operation(['m6', 'm8'], ['t4', 't6', 't7', 't9'], ['0'], [])
        o29 = Operation(['m4'], ['t10'], ['-2', '-1'], [])
        o30 = Operation(['m2', 'm3', 'm5', 'm7'], ['t5', 't6', 't7', 't11'], ['1', '3'], ['o19', 'o46'])
        o31 = Operation(['m3', 'm6'], ['t7', 't9', 't11'], ['2'], [])
        o32 = Operation(['m4', 'm5', 'm8'], ['t4', 't5', 't7', 't9'], ['-3', '-2', '3'], [])
        o33 = Operation(['m1'], ['t10', 't11'], ['0'], [])
        o34 = Operation(['m2'], ['t11'], ['-3', '2'], [])
        o35 = Operation(['m4', 'm8'], ['t3', 't4', 't6', 't9', 't10'], ['-3', '1'], [])
        o36 = Operation(['m1', 'm6', 'm8'], ['t2', 't11'], ['0', '1', '2'], [])
        o37 = Operation(['m2', 'm8'], ['t1', 't3'], ['2'], [])
        o38 = Operation(['m6', 'm8'], ['t5', 't8', 't11'], ['-1', '0'], [])
        o39 = Operation(['m4', 'm8'], ['t1', 't3', 't7'], ['0'], [])
        o40 = Operation(['m2', 'm5', 'm6', 'm7'], ['t1', 't10'], ['-3', '1'], [])
        o41 = Operation(['m3'], ['t9'], ['-1', '1', '3'], ['o7'])
        o42 = Operation(['m8'], ['t3', 't5', 't6', 't9'], ['-3', '0', '1'], ['o49'])
        o43 = Operation(['m5', 'm7'], ['t1', 't3', 't7', 't10'], ['-3', '-1'], ['o3'])
        o44 = Operation(['m3', 'm7', 'm8'], ['t1', 't3', 't6', 't8', 't11'], ['-2', '-1', '1', '2'], ['o24'])
        o45 = Operation(['m5', 'm7'], ['t2', 't4', 't5'], ['1', '3'], [])
        o46 = Operation(['m1', 'm7'], ['t1', 't10', 't11'], ['-3'], ['o34'])
        o47 = Operation(['m2'], ['t4', 't7', 't11'], ['0', '2', '3'], ['o29', 'o33', 'o49', 'o50'])
        o48 = Operation(['m1', 'm2'], ['t1', 't3', 't7'], ['-1', '0', '2'], ['o47'])
        o49 = Operation(['m1'], ['t4', 't8', 't10'], ['0', '1', '2'], [])
        o50 = Operation(['m6'], ['t1'], ['-1'], ['o16'])
        o51 = Operation(['m1', 'm4', 'm5', 'm7'], ['t4', 't8', 't9', 't10', 't11'], ['1', '3'], [])
        o52 = Operation(['m2', 'm3', 'm6'], ['t3', 't5'], ['-3', '0', '1'], ['o6'])
        o53 = Operation(['m3', 'm4', 'm6', 'm8'], ['t4', 't5', 't11'], ['-2', '-1', '1', '2'], [])
        o54 = Operation(['m5'], ['t1', 't3', 't4', 't6'], ['-2', '0', '2'], ['o27'])
        o55 = Operation(['m1', 'm2', 'm5', 'm6'], ['t5'], ['-3', '1'], [])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 18:
        """
        Case 18: cost minimization

        Details:
            - the number of operations: 89
            - the number of machines: 7
            - the number of tools: 11
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 55, 'm2': 69, 'm3': 14, 'm4': 21, 'm5': 98, 'm6': 86, 'm7': 42}
        # tool usage cost
        tuc = {'t1': 18, 't2': 6, 't3': 5, 't4': 16, 't5': 7, 't6': 15, 't7': 11, 't8': 16, 't9': 7, 't10': 9,
               't11': 17}
        # machine changeover cost
        mcc = 444
        # tool changeover cost
        tcc = 28
        # setup changeover cost
        scc = 92

        # operations
        o1 = Operation(['m2', 'm5', 'm7'], ['t10'], ['2'], [])
        o2 = Operation(['m4', 'm5'], ['t1', 't3', 't4'], ['-2', '0', '2'], ['o71'])
        o3 = Operation(['m1'], ['t6', 't8', 't10'], ['-2', '2', '3'], [])
        o4 = Operation(['m1', 'm6', 'm7'], ['t2', 't5'], ['-3', '1'], ['o58', 'o78'])
        o5 = Operation(['m1', 'm3', 'm6', 'm7'], ['t3'], ['-3', '-1', '3'], ['o18', 'o53'])
        o6 = Operation(['m1', 'm4', 'm5', 'm6'], ['t3', 't5'], ['-3', '0', '1'], ['o84'])
        o7 = Operation(['m4'], ['t6', 't7', 't11'], ['-3', '-1', '1', '2'], [])
        o8 = Operation(['m1'], ['t2', 't6'], ['1', '2', '3'], [])
        o9 = Operation(['m1'], ['t10'], ['3'], [])
        o10 = Operation(['m1', 'm4', 'm6', 'm7'], ['t1', 't5', 't10'], ['-2', '3'], [])
        o11 = Operation(['m1', 'm4', 'm5', 'm7'], ['t7'], ['-3', '-1', '1'], ['o26'])
        o12 = Operation(['m2', 'm3', 'm4', 'm5', 'm7'], ['t3', 't10', 't11'], ['-2', '1'], [])
        o13 = Operation(['m2'], ['t1', 't7', 't8'], ['-3', '0', '1'], [])
        o14 = Operation(['m1', 'm3', 'm5', 'm6'], ['t2', 't3'], ['-1', '0'], ['o69'])
        o15 = Operation(['m3', 'm5', 'm6', 'm7'], ['t4', 't8'], ['-3', '-2', '-1', '0'], ['o70', 'o86'])
        o16 = Operation(['m4', 'm5'], ['t4', 't6', 't8'], ['-3', '0', '2'], ['o48', 'o72'])
        o17 = Operation(['m3'], ['t2', 't6', 't8', 't9'], ['-2', '3'], ['o14', 'o28'])
        o18 = Operation(['m1', 'm2', 'm5'], ['t1', 't9', 't10'], ['1', '3'], ['o50'])
        o19 = Operation(['m1', 'm3', 'm5', 'm6'], ['t1', 't6', 't9'], ['1'], [])
        o20 = Operation(['m2', 'm3', 'm6'], ['t3', 't9', 't10'], ['-3', '1', '2', '3'], [])
        o21 = Operation(['m3', 'm5'], ['t6', 't8', 't10'], ['1', '2', '3'], [])
        o22 = Operation(['m3', 'm6', 'm7'], ['t3', 't6', 't9'], ['-1', '0', '1', '3'], ['o59'])
        o23 = Operation(['m6', 'm7'], ['t10'], ['-2', '0', '1', '3'], [])
        o24 = Operation(['m1', 'm2'], ['t8', 't9'], ['-3', '2'], [])
        o25 = Operation(['m5'], ['t2', 't5'], ['-2'], ['o37', 'o75'])
        o26 = Operation(['m1', 'm2', 'm4', 'm5'], ['t4', 't5', 't10'], ['1', '2'], [])
        o27 = Operation(['m4'], ['t1', 't3', 't5', 't10', 't11'], ['-3', '-2', '-1'], [])
        o28 = Operation(['m1', 'm2', 'm4', 'm6'], ['t1', 't2', 't5', 't8'], ['-1', '2'], ['o57', 'o60'])
        o29 = Operation(['m7'], ['t3', 't5', 't10', 't11'], ['1'], ['o6', 'o52'])
        o30 = Operation(['m4', 'm5', 'm7'], ['t5', 't11'], ['-3', '0', '2'], [])
        o31 = Operation(['m4', 'm5'], ['t3', 't5', 't7', 't10'], ['0', '2'], ['o2', 'o10'])
        o32 = Operation(['m5'], ['t9'], ['-3', '-1', '0'], [])
        o33 = Operation(['m1', 'm3', 'm5', 'm7'], ['t10'], ['1'], ['o9'])
        o34 = Operation(['m2', 'm5', 'm6'], ['t1'], ['-3'], ['o8'])
        o35 = Operation(['m2', 'm3'], ['t2', 't3', 't7'], ['-3', '1'], [])
        o36 = Operation(['m6'], ['t2', 't3', 't8'], ['1', '3'], ['o13', 'o29'])
        o37 = Operation(['m1', 'm2', 'm3', 'm5', 'm7'], ['t3', 't5', 't6'], ['-1'], [])
        o38 = Operation(['m5', 'm7'], ['t5', 't6'], ['-3', '1', '2'], [])
        o39 = Operation(['m3'], ['t2', 't4', 't5', 't6'], ['-2', '1', '2'], [])
        o40 = Operation(['m1', 'm2', 'm4', 'm5', 'm6'], ['t1', 't5', 't6', 't11'], ['-2', '1', '3'], ['o45'])
        o41 = Operation(['m1'], ['t5', 't8', 't11'], ['-3', '-2', '0', '3'], ['o52'])
        o42 = Operation(['m1', 'm4', 'm5', 'm6'], ['t2', 't4', 't10', 't11'], ['1', '2'], [])
        o43 = Operation(['m2'], ['t3', 't4', 't6'], ['-3', '-2', '1'], ['o27'])
        o44 = Operation(['m4', 'm6'], ['t1', 't8', 't10'], ['-3', '-2', '0', '2'], ['o51'])
        o45 = Operation(['m1', 'm2', 'm6', 'm7'], ['t7', 't9'], ['-2'], ['o1'])
        o46 = Operation(['m2', 'm4', 'm5', 'm7'], ['t10'], ['-2', '-1'], [])
        o47 = Operation(['m3', 'm4', 'm6'], ['t2', 't3', 't6'], ['-2', '-1', '2'], ['o29', 'o58'])
        o48 = Operation(['m5', 'm7'], ['t1', 't4', 't7', 't10'], ['0', '1'], [])
        o49 = Operation(['m1', 'm2', 'm3', 'm4', 'm5'], ['t5', 't10'], ['2'], ['o51', 'o62'])
        o50 = Operation(['m2', 'm3'], ['t6'], ['-2', '0'], ['o41', 'o70'])
        o51 = Operation(['m5', 'm6'], ['t7', 't8'], ['1'], ['o3'])
        o52 = Operation(['m2', 'm3', 'm5'], ['t9'], ['-2', '0'], [])
        o53 = Operation(['m1', 'm3', 'm5'], ['t1', 't8', 't11'], ['-1'], [])
        o54 = Operation(['m3', 'm4', 'm6'], ['t3', 't10', 't11'], ['-2', '1', '2'], ['o18', 'o44', 'o66'])
        o55 = Operation(['m3'], ['t3'], ['0', '1', '3'], ['o41'])
        o56 = Operation(['m7'], ['t7', 't10'], ['1', '2'], ['o86'])
        o57 = Operation(['m3'], ['t2'], ['-2', '-1', '2'], [])
        o58 = Operation(['m1', 'm6'], ['t2', 't9'], ['-3', '-2'], ['o19'])
        o59 = Operation(['m4', 'm5', 'm6', 'm7'], ['t4', 't6', 't7', 't11'], ['-2'], [])
        o60 = Operation(['m5', 'm6'], ['t2', 't6', 't10'], ['1', '3'], ['o40', 'o43'])
        o61 = Operation(['m4', 'm5'], ['t2', 't6', 't10'], ['2'], [])
        o62 = Operation(['m1', 'm3', 'm4', 'm5', 'm7'], ['t3', 't9', 't10'], ['-1', '2'], ['o84'])
        o63 = Operation(['m2', 'm6'], ['t4', 't5', 't7'], ['-3', '-2', '-1', '3'], [])
        o64 = Operation(['m3', 'm6', 'm7'], ['t2', 't4', 't6'], ['-1'], [])
        o65 = Operation(['m2', 'm4'], ['t3', 't5'], ['-2', '2', '3'], ['o20', 'o85'])
        o66 = Operation(['m1', 'm6'], ['t7'], ['0'], ['o27'])
        o67 = Operation(['m2', 'm3', 'm5', 'm6'], ['t7'], ['-3', '-2', '3'], [])
        o68 = Operation(['m1', 'm4', 'm5'], ['t4', 't5', 't8'], ['0', '3'], [])
        o69 = Operation(['m4', 'm7'], ['t1'], ['3'], ['o60'])
        o70 = Operation(['m1', 'm3', 'm6'], ['t4', 't8'], ['2'], [])
        o71 = Operation(['m3', 'm6'], ['t1', 't2', 't8', 't10'], ['-2', '3'], ['o8', 'o14', 'o51'])
        o72 = Operation(['m4'], ['t4'], ['3'], ['o44'])
        o73 = Operation(['m4', 'm5'], ['t4', 't6', 't9'], ['-1', '2', '3'], ['o14', 'o33', 'o34', 'o68'])
        o74 = Operation(['m2', 'm3', 'm4', 'm5', 'm6'], ['t3', 't5', 't10', 't11'], ['-3'], [])
        o75 = Operation(['m6'], ['t1', 't3'], ['-3', '-1', '0', '3'], ['o77'])
        o76 = Operation(['m2', 'm5'], ['t1', 't6', 't7', 't11'], ['2'], ['o82'])
        o77 = Operation(['m1', 'm5', 'm6'], ['t3', 't4', 't11'], ['-3', '1'], [])
        o78 = Operation(['m1', 'm5', 'm6'], ['t8', 't10'], ['-2', '-1'], ['o11', 'o61', 'o79'])
        o79 = Operation(['m1', 'm3', 'm4'], ['t2'], ['-1', '0', '1'], ['o8'])
        o80 = Operation(['m4'], ['t7', 't9', 't10', 't11'], ['-3', '-2', '1'], ['o67'])
        o81 = Operation(['m1', 'm2', 'm4', 'm6'], ['t4', 't6', 't9'], ['-3', '0', '2'], ['o78'])
        o82 = Operation(['m1', 'm4'], ['t2', 't3'], ['-1', '2', '3'], ['o81'])
        o83 = Operation(['m1', 'm4', 'm6', 'm7'], ['t6', 't8', 't10', 't11'], ['-2'], ['o66'])
        o84 = Operation(['m1', 'm3'], ['t3', 't5'], ['2'], ['o17'])
        o85 = Operation(['m1', 'm3', 'm5'], ['t9'], ['-1', '2', '3'], ['o33'])
        o86 = Operation(['m3', 'm4'], ['t4', 't5', 't7'], ['3'], ['o2'])
        o87 = Operation(['m6'], ['t2', 't5'], ['-1', '1'], ['o41'])
        o88 = Operation(['m3', 'm7'], ['t1', 't3', 't7', 't10'], ['-2', '0', '1'], ['o42', 'o57'])
        o89 = Operation(['m1', 'm2', 'm3', 'm6'], ['t3', 't9'], ['0', '1', '3'], ['o80'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79, 'o80': o80, 'o81': o81, 'o82': o82,
            'o83': o83, 'o84': o84, 'o85': o85, 'o86': o86, 'o87': o87, 'o88': o88, 'o89': o89,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 19:
        """
        Case 19: cost minimization

        Details:
            - the number of operations: 85
            - the number of machines: 9
            - the number of tools: 10
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 50, 'm2': 30, 'm3': 68, 'm4': 96, 'm5': 52, 'm6': 94, 'm7': 18, 'm8': 92, 'm9': 31}
        # tool usage cost
        tuc = {'t1': 6, 't2': 13, 't3': 14, 't4': 12, 't5': 20, 't6': 8, 't7': 12, 't8': 20, 't9': 5, 't10': 20}
        # machine changeover cost
        mcc = 196
        # tool changeover cost
        tcc = 12
        # setup changeover cost
        scc = 52

        # operations
        o1 = Operation(['m7'], ['t1', 't7', 't9'], ['-2', '3'], ['o25'])
        o2 = Operation(['m1', 'm5', 'm7'], ['t2'], ['-1', '1', '3'], [])
        o3 = Operation(['m3', 'm5', 'm7', 'm9'], ['t3', 't7', 't8', 't10'], ['-2', '2'], [])
        o4 = Operation(['m1', 'm2', 'm3'], ['t6', 't9'], ['-1', '1', '3'], ['o71', 'o81'])
        o5 = Operation(['m1', 'm7'], ['t2', 't8'], ['-3', '-2', '-1'], ['o78'])
        o6 = Operation(['m2', 'm4', 'm5'], ['t2', 't9', 't10'], ['-2', '-1'], ['o1', 'o50'])
        o7 = Operation(['m1', 'm6'], ['t7'], ['t2'], ['o42'])
        o8 = Operation(['m3', 'm4', 'm8', 'm9'], ['t2', 't3', 't4', 't8'], ['-2', '0', '2'], ['o1'])
        o9 = Operation(['m2', 'm5'], ['t6', 't7', 't10'], ['-2'], ['o43', 'o77'])
        o10 = Operation(['m1', 'm3', 'm4', 'm7'], ['t1', 't3', 't8', 't10'], ['-3', '-2', '1', '2'], [])
        o11 = Operation(['m2', 'm5', 'm6'], ['t4', 't9', 't10'], ['-1'], [])
        o12 = Operation(['m1', 'm5'], ['t3', 't5', 't8'], ['-1', '2', '3'], [])
        o13 = Operation(['m7'], ['t2', 't3', 't4', 't9', 't10'], ['-3', '3'], [])
        o14 = Operation(['m6'], ['t6'], ['0', '3'], ['o2'])
        o15 = Operation(['m7'], ['t3', 't5', 't8'], ['-3', '-1'], [])
        o16 = Operation(['m2', 'm3'], ['t10'], ['0', '2', '3'], [])
        o17 = Operation(['m6'], ['t4'], ['-3', '2'], [])
        o18 = Operation(['m5'], ['t4', 't6'], ['-3', '1', '3'], ['o15', 'o26'])
        o19 = Operation(['m1', 'm2', 'm5', 'm9'], ['t7', 't8'], ['-3', '0', '1', '2'], [])
        o20 = Operation(['m3', 'm8'], ['t1', 't5'], ['-1', '2', '3'], [])
        o21 = Operation(['m4', 'm6', 'm7'], ['t8', 't9', 't10'], ['-3', '-2'], [])
        o22 = Operation(['m5', 'm6'], ['t3'], ['-3', '1', '2'], ['o59'])
        o23 = Operation(['m3', 'm4', 'm5', 'm7'], ['t4', 't10'], ['-2', '0', '2'], [])
        o24 = Operation(['m1', 'm3', 'm6'], ['t1', 't3', 't7'], ['-2', '-1', '1'], ['o17', 'o41'])
        o25 = Operation(['m3', 'm9'], ['t4', 't6', 't7', 't8', 't10'], ['-3', '1', '3'], ['o32'])
        o26 = Operation(['m9'], ['t3', 't9'], ['-2', '2', '3'], [])
        o27 = Operation(['m1', 'm8'], ['t3', 't4', 't8', 't10'], ['-3', '-2', '-1', '2'], ['o1', 'o44'])
        o28 = Operation(['m5', 'm6', 'm8'], ['t4', 't6', 't9'], ['0', '2', '3'], [])
        o29 = Operation(['m4', 'm5', 'm8'], ['t2', 't7', 't9'], ['-2', '-1'], [])
        o30 = Operation(['m3', 'm5'], ['t2', 't5', 't8'], ['0', '1', '3'], ['o9'])
        o31 = Operation(['m2', 'm3', 'm5', 'm6'], ['t1', 't3', 't7', 't10'], ['0'], ['o78'])
        o32 = Operation(['m5', 'm8', 'm9'], ['t1', 't7', 't9'], ['-3'], [])
        o33 = Operation(['m4', 'm5', 'm6'], ['t2', 't5', 't7'], ['0'], ['o2', 'o11', 'o67', 'o71'])
        o34 = Operation(['m3', 'm4', 'm5', 'm8'], ['t4', 't9'], ['-2', '0', '2'], [])
        o35 = Operation(['m2', 'm4', 'm7', 'm8'], ['t6'], ['-3'], [])
        o36 = Operation(['m7'], ['t1', 't2', 't3', 't6'], ['-2', '-1', '2'], ['o23', 'o25', 'o37', 'o55'])
        o37 = Operation(['m5', 'm6'], ['t4', 't6'], ['-3', '-2'], ['o41'])
        o38 = Operation(['m1', 'm8'], ['t1', 't5'], ['0'], ['o6'])
        o39 = Operation(['m2', 'm3', 'm9'], ['t6'], ['-2', '-1', '2'], ['o26'])
        o40 = Operation(['m2', 'm4', 'm5', 'm7'], ['t4', 't9'], ['0'], [])
        o41 = Operation(['m3', 'm6', 'm7'], ['t3', 't9'], ['-3', '-2', '0', '1'], [])
        o42 = Operation(['m2', 'm6', 'm8'], ['t6'], ['-2', '0', '3'], ['o18'])
        o43 = Operation(['m2', 'm5', 'm6', 'm8'], ['t6', 't7'], ['-2', '2'], ['o11'])
        o44 = Operation(['m2', 'm6', 'm7', 'm8', 'm9'], ['t2', 't8'], ['-3', '0', '2'], [])
        o45 = Operation(['m3'], ['t4'], ['-2', '0', '1'], ['o14', 'o72'])
        o46 = Operation(['m1', 'm2'], ['t3', 't6'], ['0', '1'], ['o80'])
        o47 = Operation(['m1', 'm4', 'm8'], ['t1', 't5', 't6', 't10'], ['-1', '0', '2'], ['o57', 'o75'])
        o48 = Operation(['m5'], ['t4', 't7'], ['-3', '-1'], ['o42'])
        o49 = Operation(['m3', 'm4', 'm5', 'm6', 'm7'], ['t4', 't5'], ['0'], [])
        o50 = Operation(['m1', 'm7', 'm8'], ['t4', 't9'], ['-1'], [])
        o51 = Operation(['m5', 'm9'], ['t4', 't7', 't10'], ['-3', '0'], [])
        o52 = Operation(['m2', 'm7', 'm9'], ['t4', 't7', 't10'], ['-3', '-2', '1', '2'], ['o7'])
        o53 = Operation(['m3'], ['t8'], ['-3', '-2'], ['o32', 'o37'])
        o54 = Operation(['m1', 'm2', 'm3', 'm7'], ['t7'], ['0', '1'], [])
        o55 = Operation(['m3', 'm4', 'm6'], ['t3', 't4', 't5', 't10'], ['-3', '-2', '2', '3'], [])
        o56 = Operation(['m1', 'm3', 'm7'], ['t8'], ['-2', '-1', '2'], ['o53'])
        o57 = Operation(['m1', 'm2', 'm3', 'm5'], ['t5', 't6', 't9'], ['-1'], ['o13'])
        o58 = Operation(['m8'], ['t1', 't3', 't4'], ['-2', '1'], ['o51'])
        o59 = Operation(['m7'], ['t2'], ['-3'], [])
        o60 = Operation(['m4', 'm6', 'm7'], ['t6'], ['1'], ['o36', 'o80'])
        o61 = Operation(['m4'], ['t3', 't5', 't8'], ['-1'], [])
        o62 = Operation(['m1', 'm4', 'm7'], ['t2', 't9', 't10'], ['-2', '2', '3'], ['o45', 'o48'])
        o63 = Operation(['m3', 'm4', 'm8'], ['t4'], ['-2', '-1', '1'], ['o70'])
        o64 = Operation(['m1', 'm2', 'm8'], ['t1', 't4', 't10'], ['0'], [])
        o65 = Operation(['m2', 'm5', 'm6'], ['t1', 't6', 't7', 't9'], ['-3', '-2', '1'], ['o57', 'o74'])
        o66 = Operation(['m4', 'm8', 'm9'], ['t2', 't4', 't5', 't9', 't10'], ['1'], [])
        o67 = Operation(['m4', 'm7'], ['t3', 't9'], ['-2', '1'], ['o37'])
        o68 = Operation(['m3', 'm5', 'm8', 'm9'], ['t2', 't7'], ['-1'], [])
        o69 = Operation(['m3', 'm4', 'm5', 'm8'], ['t1', 't5', 't6'], ['-1'], ['o42'])
        o70 = Operation(['m3', 'm6', 'm8'], ['t3', 't8'], ['-3'], [])
        o71 = Operation(['m1', 'm2', 'm6'], ['t1', 't4', 't7', 't10'], ['-3'], ['o3'])
        o72 = Operation(['m9'], ['t2', 't7'], ['-1', '0', '2'], ['o58'])
        o73 = Operation(['m1', 'm2', 'm6'], ['t1', 't2'], ['-3'], [])
        o74 = Operation(['m2', 'm4', 'm9'], ['t9', 't10'], ['0', '2'], ['o62'])
        o75 = Operation(['m2', 'm3', 'm4', 'm5'], ['t5', 't6', 't10'], ['-2', '0'], ['o2'])
        o76 = Operation(['m8'], ['t4', 't6', 't9'], ['-3', '-1'], [])
        o77 = Operation(['m6'], ['t5'], ['-3'], ['o46', 'o84'])
        o78 = Operation(['m2'], ['t1', 't2', 't5', 't7'], ['-3', '2'], [])
        o79 = Operation(['m2', 'm4', 'm5', 'm6'], ['t6', 't7', 't9', 't10'], ['0'], [])
        o80 = Operation(['m2', 'm4', 'm5', 'm6', 'm9'], ['t1', 't3'], ['-2'], [])
        o81 = Operation(['m2', 'm7', 'm9'], ['t2'], ['-1', '0', '3'], ['o76'])
        o82 = Operation(['m2', 'm4', 'm6'], ['t7', 't8'], ['-1', '1', '3'], [])
        o83 = Operation(['m1', 'm2'], ['t4', 't5', 't8', 't10'], ['-3', '-1'], [])
        o84 = Operation(['m2', 'm3', 'm5'], ['t3', 't9'], ['-3', '-1', '1'], [])
        o85 = Operation(['m4'], ['t3', 't7'], ['-1', '0', '2'], [])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79, 'o80': o80, 'o81': o81, 'o82': o82,
            'o83': o83, 'o84': o84, 'o85': o85,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 20:
        """
        Case 20: cost minimization

        Details:
            - the number of operations: 98
            - the number of machines: 6
            - the number of tools: 15
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 68, 'm2': 31, 'm3': 68, 'm4': 63, 'm5': 83, 'm6': 43}
        # tool usage cost
        tuc = {'t1': 10, 't2': 15, 't3': 15, 't4': 6, 't5': 11, 't6': 18, 't7': 17, 't8': 20, 't9': 20, 't10': 20,
               't11': 9, 't12': 20, 't13': 16, 't14': 17, 't15': 20}
        # machine changeover cost
        mcc = 213
        # tool changeover cost
        tcc = 24
        # setup changeover cost
        scc = 98

        # operations
        o1 = Operation(['m1', 'm4', 'm5'], ['t2', 't6'], ['2'], [])
        o2 = Operation(['m6'], ['t6', 't9', 't11'], ['-3'], ['o76'])
        o3 = Operation(['m1', 'm6'], ['t14'], ['-2', '-1', '2'], ['o47', 'o91'])
        o4 = Operation(['m2'], ['t3', 't9'], ['-1', '0'], [])
        o5 = Operation(['m1', 'm5', 'm6'], ['t4', 't11'], ['0'], ['o87'])
        o6 = Operation(['m1', 'm3', 'm5'], ['t1', 't5', 't10', 't13', 't15'], ['-1', '3'], ['o36', 'o72', 'o73'])
        o7 = Operation(['m3', 'm4', 'm6'], ['t8', 't14'], ['-1', '0', '1'], [])
        o8 = Operation(['m1', 'm2', 'm3'], ['t9', 't10', 't12'], ['-3', '1', '2'], ['o81'])
        o9 = Operation(['m1', 'm2', 'm6'], ['t8', 't10', 't14'], ['-2', '1', '3'], ['o88', 'o93'])
        o10 = Operation(['m6'], ['t1', 't2', 't3', 't13', 't14'], ['-3', '3'], ['o43'])
        o11 = Operation(['m2', 'm3', 'm5'], ['t4', 't13'], ['1'], [])
        o12 = Operation(['m1', 'm5', 'm6'], ['t2', 't6', 't8', 't13'], ['0', '1'], [])
        o13 = Operation(['m1', 'm4'], ['t3', 't6'], ['3'], [])
        o14 = Operation(['m2'], ['t2', 't5', 't12', 't15'], ['-1', '0', '3'], [])
        o15 = Operation(['m4'], ['t2', 't6'], ['-2', '2', '3'], [])
        o16 = Operation(['m2', 'm4', 'm5'], ['t1', 't6', 't11', 't13', 't14'], ['1'], ['o47'])
        o17 = Operation(['m1', 'm5', 'm6'], ['t1', 't5', 't12'], ['-3', '0', '3'], [])
        o18 = Operation(['m1', 'm3', 'm5'], ['t4', 't6', 't10'], ['-3', '1'], [])
        o19 = Operation(['m1', 'm3', 'm5', 'm6'], ['t2', 't4', 't6', 't8'], ['-3', '1'], ['o92'])
        o20 = Operation(['m1', 'm2', 'm3', 'm4'], ['t5', 't12', 't14'], ['1'], ['o24'])
        o21 = Operation(['m1', 'm2', 'm5'], ['t6', 't9', 't12', 't15'], ['2'], ['o88'])
        o22 = Operation(['m3', 'm4', 'm6'], ['t1', 't8'], ['0'], ['o57', 'o79'])
        o23 = Operation(['m4'], ['t10', 't14'], ['-1'], ['o70'])
        o24 = Operation(['m1', 'm3', 'm5', 'm6'], ['t8', 't15'], ['-2', '0'], ['o84'])
        o25 = Operation(['m4'], ['t4', 't6', 't11', 't15'], ['2'], [])
        o26 = Operation(['m1', 'm3'], ['t5', 't6', 't14'], ['0', '3'], [])
        o27 = Operation(['m3'], ['t8', 't9', 't10', 't15'], ['-2', '2'], [])
        o28 = Operation(['m1', 'm2', 'm3', 'm4', 'm6'], ['t2', 't13'], ['1'], [])
        o29 = Operation(['m1', 'm2', 'm6'], ['t2', 't9', 't12'], ['-1', '1'], ['o18', 'o54', 'o87'])
        o30 = Operation(['m3', 'm4'], ['t5', 't7', 't8', 't11'], ['-2', '0', '1'], [])
        o31 = Operation(['m5', 'm6'], ['t8'], ['-3', '-2', '0'], [])
        o32 = Operation(['m3', 'm4', 'm5'], ['t3', 't5', 't8', 't10', 't14'], ['-3', '-1'], ['o80'])
        o33 = Operation(['m2', 'm3', 'm6'], ['t1', 't2', 't5', 't7'], ['-2', '-1'], ['o42'])
        o34 = Operation(['m2', 'm6'], ['t2', 't5', 't8', 't13'], ['-1'], [])
        o35 = Operation(['m1', 'm5'], ['t1', 't3', 't8', 't12'], ['-3', '-2'], [])
        o36 = Operation(['m1', 'm3', 'm4', 'm5'], ['t1', 't3', 't4', 't9', 't11'], ['-1'], ['o8'])
        o37 = Operation(['m4', 'm5'], ['t1', 't6', 't11', 't13', 't14'], ['-1', '0', '3'], [])
        o38 = Operation(['m1', 'm2', 'm6'], ['t1', 't6', 't9'], ['0', '3'], [])
        o39 = Operation(['m2', 'm4'], ['t8', 't12', 't13'], ['-1'], ['o2', 'o47', 'o48', 'o51', 'o58', 'o75'])
        o40 = Operation(['m1', 'm3', 'm5'], ['t9'], ['-2', '-1'], ['o16'])
        o41 = Operation(['m1', 'm2', 'm3', 'm5'], ['t8'], ['-3', '-1', '1'], ['o10'])
        o42 = Operation(['m1', 'm2', 'm3'], ['t3', 't5', 't8'], ['1'], ['o2', 'o4'])
        o43 = Operation(['m1'], ['t2'], ['3'], ['o56', 'o67'])
        o44 = Operation(['m2', 'm4'], ['t2', 't7'], ['0', '2'], ['o1', 'o54', 'o92'])
        o45 = Operation(['m1', 'm2', 'm3', 'm4'], ['t2', 't3', 't7', 't14'], ['0'], [])
        o46 = Operation(['m2', 'm3'], ['t1', 't3', 't7', 't9'], ['-2', '0', '1', '2'], ['o8'])
        o47 = Operation(['m1', 'm3', 'm5'], ['t3', 't13', 't14', 't15'], ['0', '2'], ['o60'])
        o48 = Operation(['m5'], ['t1', 't2', 't13', 't15'], ['-3', '0', '2', '3'], ['o37', 'o54'])
        o49 = Operation(['m2', 'm3', 'm4', 'm6'], ['t5', 't8', 't15'], ['-3', '1'], ['o62', 'o67'])
        o50 = Operation(['m2', 'm5'], ['t1', 't4', 't11', 't14'], ['1'], [])
        o51 = Operation(['m1', 'm2', 'm4', 'm6'], ['t3', 't6', 't7'], ['-1', '0', '2'], ['o73'])
        o52 = Operation(['m3'], ['t6', 't7', 't8', 't9'], ['1', '2', '3'], ['o30'])
        o53 = Operation(['m4'], ['t3', 't5', 't6', 't8'], ['-2', '2', '3'], ['o6', 'o72'])
        o54 = Operation(['m1', 'm4'], ['t9', 't10', 't11', 't14'], ['-3', '0', '3'], ['o8'])
        o55 = Operation(['m4'], ['t1', 't9', 't14'], ['-3', '-2', '0'], ['o41'])
        o56 = Operation(['m1', 'm5'], ['t13', 't15'], ['2'], ['o48'])
        o57 = Operation(['m2', 'm3', 'm6'], ['t2'], ['-1', '1', '2'], ['o14'])
        o58 = Operation(['m3'], ['t8', 't9', 't11', 't14'], ['-2', '3'], ['o5', 'o13', 'o66'])
        o59 = Operation(['m2'], ['t1', 't3', 't5', 't8'], ['-1', '1'], [])
        o60 = Operation(['m3', 'm5'], ['t7'], ['-1'], [])
        o61 = Operation(['m1', 'm3'], ['t2', 't9'], ['-3', '-2', '1'], [])
        o62 = Operation(['m4'], ['t4', 't6', 't7'], ['-2', '-1', '0', '1'], ['o51', 'o67'])
        o63 = Operation(['m6'], ['t4', 't9', 't12', 't13', 't14'], ['0'], ['o31', 'o81'])
        o64 = Operation(['m1', 'm5', 'm6'], ['t8', 't11', 't15'], ['1'], [])
        o65 = Operation(['m4'], ['t2', 't9', 't12'], ['-3', '-2', '-1', '1'], [])
        o66 = Operation(['m2', 'm3', 'm6'], ['t9', 't11', 't12'], ['-2', '3'], ['o53', 'o71'])
        o67 = Operation(['m2', 'm5', 'm6'], ['t4', 't8', 't10', 't12'], ['-1', '1', '3'], [])
        o68 = Operation(['m5', 'm6'], ['t1', 't4', 't10', 't15'], ['0'], ['o50'])
        o69 = Operation(['m6'], ['t1', 't8', 't9', 't14', 't15'], ['-1'], [])
        o70 = Operation(['m1', 'm3', 'm5'], ['t9', 't13'], ['-3', '-2', '0', '3'], ['o46'])
        o71 = Operation(['m1', 'm3', 'm4', 'm5'], ['t2', 't11'], ['-3', '-1'], ['o36'])
        o72 = Operation(['m3'], ['t5', 't12', 't15'], ['-3'], ['o35'])
        o73 = Operation(['m4', 'm5'], ['t1', 't3', 't5', 't8', 't10'], ['-1', '3'], ['o25'])
        o74 = Operation(['m3', 'm5'], ['t1', 't8'], ['-2'], [])
        o75 = Operation(['m5'], ['t5', 't8'], ['-3', '2'], ['o11'])
        o76 = Operation(['m2', 'm3', 'm6'], ['t1', 't5', 't14', 't15'], ['-2', '1'], [])
        o77 = Operation(['m3', 'm4', 'm5'], ['t7', 't8', 't12', 't15'], ['-2', '2', '3'], ['o45'])
        o78 = Operation(['m1', 'm2', 'm6'], ['t5', 't6', 't11', 't15'], ['3'], ['o65'])
        o79 = Operation(['m3', 'm5'], ['t15'], ['1', '2'], ['o72'])
        o80 = Operation(['m1', 'm4'], ['t1', 't5'], ['-1'], ['o3', 'o46', 'o86'])
        o81 = Operation(['m6'], ['t1', 't5', 't8'], ['-3', '2'], [])
        o82 = Operation(['m2', 'm3'], ['t4', 't8'], ['-3', '1', '3'], ['o53', 'o84'])
        o83 = Operation(['m3', 'm4'], ['t5'], ['-3', '1', '3'], [])
        o84 = Operation(['m2', 'm3'], ['t4', 't9'], ['-2'], ['o69'])
        o85 = Operation(['m2', 'm4'], ['t2', 't6', 't7', 't8', 't10'], ['-3', '-1', '1'], ['o23'])
        o86 = Operation(['m4'], ['t6'], ['-2', '-1', '2'], ['o90'])
        o87 = Operation(['m1', 'm5'], ['t3', 't7', 't10'], ['-3'], ['o34', 'o83'])
        o88 = Operation(['m4'], ['t1', 't5', 't10'], ['-2'], ['o36', 'o74'])
        o89 = Operation(['m1', 'm4', 'm6'], ['t1', 't9', 't14', 't15'], ['-1'], ['o14', 'o57', 'o64'])
        o90 = Operation(['m3'], ['t3', 't4', 't10'], ['2'], ['o3'])
        o91 = Operation(['m3', 'm4', 'm5'], ['t6', 't7', 't15'], ['-1'], ['o58'])
        o92 = Operation(['m1', 'm4', 'm5', 'm6'], ['t6', 't8', 't10', 't11'], ['-2', '1', '3'], ['o76'])
        o93 = Operation(['m2', 'm3', 'm6'], ['t3', 't13', 't14', 't15'], ['-2', '-1', '1'], ['o41'])
        o94 = Operation(['m5'], ['t3', 't4', 't10', 't14', 't15'], ['-2', '0'], ['o62'])
        o95 = Operation(['m2', 'm6'], ['t2', 't6', 't10', 't12'], ['-3', '1', '2'], [])
        o96 = Operation(['m1', 'm6'], ['t4', 't12'], ['-2', '1', '3'], [])
        o97 = Operation(['m2', 'm4'], ['t6', 't11', 't13', 't15'], ['-3'], ['o68', 'o74', 'o75'])
        o98 = Operation(['m3', 'm5'], ['t15'], ['-2', '-1', '2', '3'], ['o44'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79, 'o80': o80, 'o81': o81, 'o82': o82,
            'o83': o83, 'o84': o84, 'o85': o85, 'o86': o86, 'o87': o87, 'o88': o88, 'o89': o89, 'o90': o90,
            'o91': o91, 'o92': o92, 'o93': o93, 'o94': o94, 'o95': o95, 'o96': o96, 'o97': o97, 'o98': o98,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 21:
        """
        Case 21: cost minimization

        Details:
            - the number of operations: 88
            - the number of machines: 8
            - the number of tools: 15
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 48, 'm2': 31, 'm3': 35, 'm4': 97, 'm5': 77, 'm6': 11, 'm7': 43, 'm8': 45}
        # tool usage cost
        tuc = {'t1': 19, 't2': 18, 't3': 12, 't4': 15, 't5': 7, 't6': 16, 't7': 12, 't8': 17, 't9': 6, 't10': 8,
               't11': 19, 't12': 18, 't13': 5, 't14': 9, 't15': 7}
        # machine changeover cost
        mcc = 329
        # tool changeover cost
        tcc = 24
        # setup changeover cost
        scc = 86

        # operations
        o1 = Operation(['m8'], ['t3', 't15'], ['-3', '-1', '1'], [])
        o2 = Operation(['m2', 'm3', 'm4', 'm7'], ['t1', 't8', 't9', 't12'], ['2'], [])
        o3 = Operation(['m1', 'm7'], ['t3', 't5'], ['-3'], [])
        o4 = Operation(['m3'], ['t2', 't6', 't10', 't11'], ['-2', '0'], [])
        o5 = Operation(['m6'], ['t12'], ['-1', '0', '2'], ['o83'])
        o6 = Operation(['m1', 'm4', 'm8'], ['t7', 't8', 't11'], ['-2', '0'], ['o34', 'o37', 'o85'])
        o7 = Operation(['m4', 'm6', 'm7'], ['t8', 't10'], ['-3', '-2', '2'], [])
        o8 = Operation(['m2', 'm6'], ['t2', 't4', 't5', 't6', 't10'], ['-2'], ['o25'])
        o9 = Operation(['m6', 'm7', 'm8'], ['t2', 't9'], ['-1', '1'], ['o75'])
        o10 = Operation(['m2', 'm4', 'm6', 'm8'], ['t5', 't7', 't10'], ['3'], ['o37'])
        o11 = Operation(['m1', 'm8'], ['t3', 't5', 't7', 't14', 't15'], ['-1'], [])
        o12 = Operation(['m3', 'm7'], ['t3', 't6', 't14', 't15'], ['-1', '1'], ['o17', 'o73'])
        o13 = Operation(['m4', 'm6', 'm7'], ['t1', 't5', 't10', 't13'], ['-2', '0'], [])
        o14 = Operation(['m6'], ['t10'], ['-2', '-1'], [])
        o15 = Operation(['m6'], ['t2', 't12', 't13'], ['3'], [])
        o16 = Operation(['m8'], ['t3'], ['-3', '-2', '-1', '1'], [])
        o17 = Operation(['m3', 'm5'], ['t4', 't5', 't6', 't14'], ['-1'], [])
        o18 = Operation(['m2', 'm6', 'm7'], ['t15'], ['-2', '-1', '3'], ['o1', 'o22'])
        o19 = Operation(['m1', 'm2', 'm4', 'm5', 'm8'], ['t2', 't6', 't7'], ['-3', '-2', '1'], [])
        o20 = Operation(['m3', 'm6'], ['t4', 't8', 't12', 't15'], ['0', '2', '3'], [])
        o21 = Operation(['m3', 'm5', 'm7'], ['t1', 't5'], ['3'], [])
        o22 = Operation(['m5', 'm6'], ['t15'], ['-3', '-1', '2', '3'], [])
        o23 = Operation(['m5', 'm8'], ['t11', 't14'], ['-1', '0', '3'], ['o60', 'o65'])
        o24 = Operation(['m1', 'm2', 'm4', 'm6', 'm7'], ['t1', 't6', 't10', 't13'], ['-3', '-1'],
                        ['o14', 'o22', 'o28', 'o37'])
        o25 = Operation(['m8'], ['t7', 't14', 't15'], ['-3', '2', '3'], ['o81'])
        o26 = Operation(['m7'], ['t7', 't14'], ['-2', '-1', '3'], [])
        o27 = Operation(['m1', 'm3', 'm7'], ['t4'], ['1', '3'], [])
        o28 = Operation(['m1', 'm2'], ['t9', 't10', 't13'], ['1', '2'], [])
        o29 = Operation(['m5', 'm6'], ['t11', 't13'], ['-3', '-2', '1', '3'], [])
        o30 = Operation(['m2', 'm7', 'm8'], ['t5', 't13'], ['2'], ['o56', 'o75'])
        o31 = Operation(['m4', 'm5'], ['t4', 't10', 't12', 't14', 't15'], ['-1', '0'], ['o32', 'o75'])
        o32 = Operation(['m5'], ['t6', 't7', 't13'], ['0'], ['o12', 'o86'])
        o33 = Operation(['m7'], ['t10', 't15'], ['2', '3'], [])
        o34 = Operation(['m3', 'm6'], ['t7'], ['-3', '2'], [])
        o35 = Operation(['m3'], ['t13'], ['-2', '-1', '0', '3'], [])
        o36 = Operation(['m2', 'm7'], ['t8', 't14'], ['-1', '1', '3'], [])
        o37 = Operation(['m8'], ['t3', 't4', 't9', 't12', 't13'], ['3'], [])
        o38 = Operation(['m2', 'm4', 'm8'], ['t13'], ['-1', '1', '2'], ['o10', 'o68'])
        o39 = Operation(['m4', 'm5'], ['t1', 't12'], ['-2'], ['o19', 'o77'])
        o40 = Operation(['m6', 'm8'], ['t14'], ['-3'], ['o64'])
        o41 = Operation(['m1', 'm3', 'm4', 'm6'], ['t2'], ['-1', '1'], [])
        o42 = Operation(['m4', 'm5', 'm6', 'm7'], ['t6'], ['-1', '3'], ['o44'])
        o43 = Operation(['m2', 'm6', 'm7'], ['t4', 't6', 't10', 't12'], ['2', '3'], ['o40', 'o50', 'o88'])
        o44 = Operation(['m4'], ['t12'], ['-2', '-1'], ['o56', 'o87'])
        o45 = Operation(['m2', 'm6'], ['t14'], ['1'], ['o6'])
        o46 = Operation(['m2', 'm4', 'm6', 'm7', 'm8'], ['t8', 't9', 't10'], ['-2', '-1', '3'], ['o47', 'o65'])
        o47 = Operation(['m2'], ['t5', 't8', 't9', 't12'], ['-3', '-1', '2'], [])
        o48 = Operation(['m6'], ['t4', 't5', 't15'], ['-3', '0', '2'], [])
        o49 = Operation(['m3', 'm6'], ['t3', 't7', 't9', 't14'], ['-2', '3'], ['o14', 'o54'])
        o50 = Operation(['m2', 'm3', 'm4'], ['t1', 't7', 't8'], ['-2', '-1', '0'], ['o5'])
        o51 = Operation(['m1', 'm5', 'm6'], ['t1', 't7'], ['2'], ['o6', 'o35', 'o60'])
        o52 = Operation(['m2', 'm3', 'm5', 'm8'], ['t3', 't7', 't9', 't13'], ['-3', '1', '3'], ['o29', 'o63'])
        o53 = Operation(['m3', 'm6', 'm7'], ['t1', 't2', 't15'], ['-1', '2'], [])
        o54 = Operation(['m4', 'm6', 'm7'], ['t6', 't8', 't11'], ['-3', '-1', '1', '3'], ['o8'])
        o55 = Operation(['m1', 'm4', 'm5', 'm8'], ['t1', 't5', 't8', 't10'], ['-2', '0'], ['o49'])
        o56 = Operation(['m5', 'm6', 'm8'], ['t8', 't11', 't12', 't14'], ['2', '3'], ['o3'])
        o57 = Operation(['m2', 'm4', 'm7'], ['t1', 't4', 't7', 't10'], ['-1'], ['o15'])
        o58 = Operation(['m4', 'm5', 'm7'], ['t1', 't6', 't9'], ['0'], ['o70'])
        o59 = Operation(['m2', 'm5', 'm6', 'm8'], ['t6'], ['0', '2', '3'], ['o87'])
        o60 = Operation(['m1', 'm2'], ['t10', 't11', 't13'], ['1'], ['o20', 'o49'])
        o61 = Operation(['m1', 'm4'], ['t1', 't5', 't6', 't13'], ['-3'], ['o11', 'o33', 'o56'])
        o62 = Operation(['m1', 'm2', 'm3', 'm6'], ['t7', 't11', 't12', 't14'], ['0'], ['o70'])
        o63 = Operation(['m3', 'm6', 'm7', 'm8'], ['t1', 't3'], ['1', '2'], [])
        o64 = Operation(['m5'], ['t12'], ['0', '3'], ['o88'])
        o65 = Operation(['m2', 'm7'], ['t2', 't9', 't10'], ['-2', '3'], ['o39'])
        o66 = Operation(['m7'], ['t4', 't5', 't8', 't9'], ['0', '2'], ['o8', 'o52'])
        o67 = Operation(['m1', 'm5', 'm6', 'm8'], ['t5', 't10', 't15'], ['-3', '-1'], ['o76'])
        o68 = Operation(['m2', 'm3', 'm4', 'm8'], ['t3', 't10', 't11', 't14'], ['-1', '0'], [])
        o69 = Operation(['m1'], ['t8', 't12', 't14'], ['-2', '0'], ['o3'])
        o70 = Operation(['m3', 'm4', 'm7', 'm8'], ['t6', 't7', 't14', 't15'], ['0'], [])
        o71 = Operation(['m1', 'm3', 'm5', 'm6'], ['t1', 't3', 't5', 't15'], ['0', '1', '2'], ['o49'])
        o72 = Operation(['m4', 'm7', 'm8'], ['t5'], ['3'], [])
        o73 = Operation(['m3', 'm6'], ['t1', 't6', 't8'], ['-2', '0'], ['o7', 'o8'])
        o74 = Operation(['m1', 'm4', 'm7', 'm8'], ['t1', 't6', 't13', 't14'], ['-1', '3'], [])
        o75 = Operation(['m2', 'm4', 'm5', 'm6', 'm7'], ['t15'], ['0', '1'], [])
        o76 = Operation(['m1', 'm8'], ['t5', 't10'], ['0', '1', '2'], [])
        o77 = Operation(['m5', 'm8'], ['t1', 't5', 't10', 't12'], ['-1'], ['o66'])
        o78 = Operation(['m1', 'm5'], ['t5'], ['1', '3'], ['o77'])
        o79 = Operation(['m1', 'm2', 'm4'], ['t1', 't12', 't13'], ['-3', '-2', '3'], ['o17', 'o25'])
        o80 = Operation(['m2', 'm3', 'm4', 'm5'], ['t1', 't6'], ['-2', '-1', '1'], [])
        o81 = Operation(['m3', 'm7', 'm8'], ['t5', 't11', 't14'], ['-2', '1'], ['o27', 'o29'])
        o82 = Operation(['m3'], ['t6', 't13', 't14'], ['0', '2', '3'], [])
        o83 = Operation(['m3', 'm4', 'm7'], ['t3', 't13'], ['0'], ['o76', 'o86'])
        o84 = Operation(['m5', 'm6'], ['t2'], ['-3', '-1', '2', '3'], ['o85'])
        o85 = Operation(['m5', 'm6', 'm7'], ['t2', 't3', 't7', 't9', 't10'], ['-3', '0', '1'], [])
        o86 = Operation(['m1'], ['t2', 't6'], ['-3', '-2', '0'], ['o88'])
        o87 = Operation(['m7'], ['t2', 't14'], ['-3', '-1', '1', '3'], ['o9'])
        o88 = Operation(['m2', 'm4', 'm7'], ['t6', 't12'], ['-2', '0', '1', '3'], ['o61'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79, 'o80': o80, 'o81': o81, 'o82': o82,
            'o83': o83, 'o84': o84, 'o85': o85, 'o86': o86, 'o87': o87, 'o88': o88,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 22:
        """
        Case 22: cost minimization

        Details:
            - the number of operations: 72
            - the number of machines: 7
            - the number of tools: 10
            - the number of directions: 7
            - alternative operations: N
        """
        case_type = {'objective': 'cost', 'alternative': False}

        # machine usage cost
        muc = {'m1': 46, 'm2': 26, 'm3': 33, 'm4': 24, 'm5': 59, 'm6': 82, 'm7': 99}
        # tool usage cost
        tuc = {'t1': 6, 't2': 18, 't3': 17, 't4': 14, 't5': 11, 't6': 15, 't7': 11, 't8': 12, 't9': 9, 't10': 5}
        # machine changeover cost
        mcc = 309
        # tool changeover cost
        tcc = 24
        # setup changeover cost
        scc = 81

        # operations
        o1 = Operation(['m2', 'm7'], ['t2', 't5', 't8', 't10'], ['2'], ['o25'])
        o2 = Operation(['m1', 'm3', 'm4'], ['t5'], ['-1', '1'], ['o37'])
        o3 = Operation(['m1', 'm2', 'm6'], ['t1', 't3', 't10'], ['-1', '1', '3'], ['o72'])
        o4 = Operation(['m2', 'm5'], ['t3', 't7'], ['-3', '1', '2'], [])
        o5 = Operation(['m3', 'm6'], ['t1', 't5', 't9'], ['-1', '2'], [])
        o6 = Operation(['m2'], ['t3'], ['0'], ['o72'])
        o7 = Operation(['m1', 'm4', 'm5'], ['t2', 't4', 't7', 't10'], ['-3', '0', '2'], ['o14'])
        o8 = Operation(['m1', 'm3', 'm4'], ['t2'], ['-1', '0'], ['o44'])
        o9 = Operation(['m4', 'm5'], ['t7', 't8'], ['3'], [])
        o10 = Operation(['m1', 'm2', 'm5', 'm7'], ['t2', 't5', 't8', 't10'], ['-3'], ['o19'])
        o11 = Operation(['m1', 'm4', 'm5'], ['t3', 't4', 't10'], ['-3', '-1', '2', '3'], ['o59'])
        o12 = Operation(['m2', 'm3', 'm4', 'm7'], ['t7', 't8'], ['-2', '-1', '1', '2'], ['o9', 'o43'])
        o13 = Operation(['m6'], ['t6', 't7', 't9', 't10'], ['2'], ['o5'])
        o14 = Operation(['m1', 'm2', 'm4'], ['t2', 't4', 't5', 't7'], ['-1', '0'], [])
        o15 = Operation(['m1', 'm2', 'm3'], ['t4', 't5', 't9'], ['0', '2', '3'], [])
        o16 = Operation(['m1'], ['t3', 't6', 't9'], ['-2'], [])
        o17 = Operation(['m6'], ['t2', 't3', 't9'], ['3'], [])
        o18 = Operation(['m2', 'm7'], ['t2'], ['-1'], ['o28'])
        o19 = Operation(['m4', 'm7'], ['t2'], ['-3', '2'], [])
        o20 = Operation(['m2', 'm3', 'm6', 'm7'], ['t4', 't5', 't7', 't8'], ['-1', '1', '2'], ['o54'])
        o21 = Operation(['m1', 'm5', 'm6'], ['t9'], ['0', '1'], ['o42'])
        o22 = Operation(['m1', 'm2', 'm6'], ['t3', 't4', 't8', 't10'], ['-1', '0'], ['o13'])
        o23 = Operation(['m1', 'm4'], ['t3', 't8', 't9', 't10'], ['1'], ['o53'])
        o24 = Operation(['m2', 'm6', 'm7'], ['t5'], ['-1', '1'], [])
        o25 = Operation(['m5'], ['t1', 't2', 't4'], ['-3'], ['o29'])
        o26 = Operation(['m2', 'm6', 'm7'], ['t7'], ['0'], [])
        o27 = Operation(['m2', 'm5', 'm7'], ['t4', 't5', 't6', 't10'], ['0', '3'], ['o40'])
        o28 = Operation(['m7'], ['t8', 't10'], ['-2', '3'], [])
        o29 = Operation(['m3', 'm4', 'm7'], ['t1', 't3', 't5', 't6'], ['-3', '0', '3'], [])
        o30 = Operation(['m2', 'm4', 'm5', 'm7'], ['t1'], ['-3', '0', '3'], [])
        o31 = Operation(['m1', 'm5', 'm6'], ['t4', 't7', 't10'], ['-2', '0', '1'], [])
        o32 = Operation(['m1', 'm4', 'm7'], ['t1', 't10'], ['-3', '-2', '0'], ['o23', 'o53'])
        o33 = Operation(['m7'], ['t5', 't7', 't10'], ['2'], ['o55'])
        o34 = Operation(['m2', 'm5', 'm6', 'm7'], ['t6', 't10'], ['1'], ['o61'])
        o35 = Operation(['m1', 'm2', 'm6', 'm7'], ['t1', 't3', 't4', 't7'], ['1', '2'], [])
        o36 = Operation(['m1', 'm2', 'm4', 'm6'], ['t2', 't4'], ['-1', '3'], ['o21', 'o43', 'o60'])
        o37 = Operation(['m5'], ['t2', 't6', 't9', 't10'], ['-3', '0'], ['o44', 'o51'])
        o38 = Operation(['m7'], ['t7', 't8'], ['-2', '2'], [])
        o39 = Operation(['m1', 'm2', 'm3'], ['t1'], ['1', '2'], ['o22'])
        o40 = Operation(['m4'], ['t1', 't4', 't6', 't9'], ['-3', '-2', '3'], ['o20'])
        o41 = Operation(['m2', 'm5'], ['t3', 't4', 't6', 't10'], ['2'], ['o13', 'o39'])
        o42 = Operation(['m4', 'm5'], ['t1', 't3', 't7', 't10'], ['-3', '0', '3'], ['o4', 'o25'])
        o43 = Operation(['m2', 'm5', 'm6'], ['t1', 't5', 't6', 't7', 't8'], ['-3', '2'], [])
        o44 = Operation(['m4', 'm5'], ['t8', 't9'], ['-2', '1', '2'], ['o5', 'o45'])
        o45 = Operation(['m1'], ['t10'], ['0', '2'], [])
        o46 = Operation(['m1', 'm2'], ['t6'], ['1'], ['o52'])
        o47 = Operation(['m2', 'm4', 'm5', 'm6'], ['t6', 't8'], ['3'], [])
        o48 = Operation(['m4', 'm5', 'm6', 'm7'], ['t1', 't6'], ['-3', '3'], [])
        o49 = Operation(['m4', 'm5', 'm6'], ['t4', 't9'], ['-1', '0', '3'], ['o52', 'o67'])
        o50 = Operation(['m1', 'm5', 'm6'], ['t5'], ['-3'], [])
        o51 = Operation(['m4', 'm5'], ['t8'], ['-2', '0'], ['o68'])
        o52 = Operation(['m2', 'm5', 'm6', 'm7'], ['t2', 't5', 't6', 't8'], ['-1', '1'], ['o71'])
        o53 = Operation(['m2', 'm5', 'm6'], ['t1', 't10'], ['-3', '0', '1'], ['o64'])
        o54 = Operation(['m1', 'm5', 'm6'], ['t3', 't5', 't6', 't7', 't9'], ['-2', '-1'], ['o2'])
        o55 = Operation(['m3', 'm5', 'm6', 'm7'], ['t3', 't5'], ['-3', '-2', '-1', '0'], ['o21', 'o31'])
        o56 = Operation(['m1'], ['t1', 't4', 't5'], ['-1', '3'], ['o31'])
        o57 = Operation(['m2', 'm5', 'm6', 'm7'], ['t6', 't7', 't10'], ['-2', '-1'], [])
        o58 = Operation(['m2'], ['t2', 't4', 't5', 't9'], ['0', '2'], ['o40', 'o54', 'o56'])
        o59 = Operation(['m2', 'm4'], ['t2', 't4', 't8', 't9'], ['-1'], [])
        o60 = Operation(['m3', 'm4'], ['t3', 't6', 't7', 't8', 't9'], ['-3', '2'], ['o14'])
        o61 = Operation(['m2', 'm6', 'm7'], ['t3'], ['-3'], ['o3'])
        o62 = Operation(['m3', 'm4', 'm6'], ['t1'], ['-2', '0', '1', '3'], ['o16'])
        o63 = Operation(['m1'], ['t2', 't9'], ['1', '2'], [])
        o64 = Operation(['m1', 'm2', 'm3', 'm5', 'm6'], ['t3', 't4', 't5'], ['-2', '0', '2', '3'], [])
        o65 = Operation(['m4', 'm5', 'm6'], ['t3', 't6'], ['-2', '-1', '1'], ['o49'])
        o66 = Operation(['m3', 'm6', 'm7'], ['t6'], ['3'], ['o32'])
        o67 = Operation(['m6'], ['t7', 't10'], ['-1'], [])
        o68 = Operation(['m2', 'm5'], ['t2', 't7'], ['0'], [])
        o69 = Operation(['m6'], ['t7', 't8', 't10'], ['-3'], [])
        o70 = Operation(['m2'], ['t3', 't5', 't6', 't9', 't10'], ['0', '1'], ['o21'])
        o71 = Operation(['m2', 'm3', 'm5'], ['t5'], ['-2', '-1'], [])
        o72 = Operation(['m2', 'm3', 'm6'], ['t4', 't5', 't6', 't10'], ['1'], ['o49', 'o62'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72,
        }

        # alternatives
        alternative_operations = {}
        alternatives = []

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 23:
        """
        Case 23: cost minimization

        Details:
            - the number of operations: 67
            - the number of machines: 7
            - the number of tools: 14
            - the number of directions: 7
            - alternative operations: Y
        """
        case_type = {'objective': 'cost', 'alternative': True}

        # machine usage cost
        muc = {'m1': 36, 'm2': 90, 'm3': 33, 'm4': 24, 'm5': 61, 'm6': 36, 'm7': 39}
        # tool usage cost
        tuc = {'t1': 14, 't2': 10, 't3': 6, 't4': 19, 't5': 13, 't6': 12, 't7': 19, 't8': 6, 't9': 19, 't10': 5,
               't11': 9, 't12': 8, 't13': 16, 't14': 5}
        # machine changeover cost
        mcc = 471
        # tool changeover cost
        tcc = 29
        # setup changeover cost
        scc = 108

        # operations
        o1 = Operation(['m1', 'm3', 'm7'], ['t1', 't8', 't10', 't12'], ['-1', '0', '2'], ['o16'])
        o2 = Operation(['m1', 'm2', 'm4'], ['t4', 't6', 't12'], ['-3', '-1'], [])
        o3 = Operation(['m4', 'm6'], ['t3', 't5', 't6'], ['-1', '0', '3'], [])
        o4 = Operation(['m1', 'm5'], ['t9', 't14'], ['-2'], [])
        o5 = Operation(['m2'], ['t5', 't8', 't10'], ['-1'], ['o20', 'o59'])
        o6 = Operation(['m1', 'm3'], ['t6', 't8'], ['0', '3'], [])
        o7 = Operation(['m2', 'm3', 'm5'], ['t3', 't9', 't12', 't14'], ['-2', '-1'], [])
        o8 = Operation(['m1', 'm5', 'm6'], ['t1', 't9', 't11'], ['-2', '-1', '2'], ['o42'])
        o9 = Operation(['m3', 'm4', 'm5', 'm6'], ['t9', 't10', 't11', 't14'], ['-2'], ['o53'])
        o10 = Operation(['m1', 'm4', 'm6', 'm7'], ['t2', 't5', 't8', 't12'], ['-1', '0'], ['o12', 'o65'])
        o11 = Operation(['m3'], ['t7', 't11'], ['-2', '0'], [])
        o12 = Operation(['m3'], ['t8', 't10', 't11'], ['-3', '-2', '-1', '0'], [])
        o13 = Operation(['m2', 'm3', 'm6'], ['t6', 't7', 't8', 't11'], ['-1', '1', '3'], ['o63'])
        o14 = Operation(['m1', 'm5', 'm7'], ['t1'], ['0', '1', '2'], [])
        o15 = Operation(['m2', 'm4', 'm7'], ['t3', 't9'], ['-3', '-1', '0'], ['o12'])
        o16 = Operation(['m4'], ['t10'], ['-3', '-1', '3'], ['o4'])
        o17 = Operation(['m1', 'm3', 'm5'], ['t8', 't10', 't11'], ['-2', '2'], [])
        o18 = Operation(['m7'], ['t8', 't9', 't14'], ['2'], ['o54'])
        o19 = Operation(['m1', 'm2', 'm3', 'm5', 'm7'], ['t7'], ['-2', '2'], ['o22'])
        o20 = Operation(['m7'], ['t6', 't7'], ['-1', '1'], ['o16'])
        o21 = Operation(['m3', 'm5', 'm6'], ['t2', 't6', 't14'], ['-2', '-1', '3'], [])
        o22 = Operation(['m1', 'm2', 'm4', 'm5', 'm6'], ['t2', 't7', 't10', 't11'], ['0', '2'], [])
        o23 = Operation(['m1', 'm3'], ['t2', 't4', 't12'], ['-1', '2'], ['o5', 'o59'])
        o24 = Operation(['m2', 'm4'], ['t2'], ['-3', '-2'], [])
        o25 = Operation(['m3', 'm5', 'm6'], ['t3', 't12'], ['-1', '2'], ['o23'])
        o26 = Operation(['m1'], ['t1', 't7', 't9', 't10'], ['-2', '0', '2'], [])
        o27 = Operation(['m5', 'm6', 'm7'], ['t1', 't5'], ['-2'], ['o5', 'o45'])
        o28 = Operation(['m1', 'm2', 'm5', 'm7'], ['t1', 't5', 't10', 't11', 't14'], ['3'], ['o3', 'o47'])
        o29 = Operation(['m3', 'm5', 'm7'], ['t1', 't3', 't9', 't11'], ['-2', '1', '2'], [])
        o30 = Operation(['m1', 'm6', 'm7'], ['t12', 't13', 't14'], ['0', '1', '2'], [])
        o31 = Operation(['m3', 'm4', 'm6'], ['t13'], ['-2', '-1', '0'], [])
        o32 = Operation(['m1', 'm4'], ['t3', 't8', 't12', 't13'], ['-3'], [])
        o33 = Operation(['m1', 'm2', 'm4'], ['t3', 't5', 't13', 't14'], ['0'], ['o16'])
        o34 = Operation(['m2', 'm6'], ['t4', 't10', 't12'], ['-3', '-2', '1', '2'], [])
        o35 = Operation(['m4', 'm5', 'm7'], ['t5'], ['0', '1'], [])
        o36 = Operation(['m2', 'm3', 'm7'], ['t4', 't12', 't14'], ['-3', '-1', '3'], ['o7', 'o44'])
        o37 = Operation(['m1', 'm2', 'm7'], ['t8', 't14'], ['-2'], [])
        o38 = Operation(['m3', 'm5'], ['t13', 't14'], ['-1', '0'], ['o7', 'o48'])
        o39 = Operation(['m4', 'm5', 'm6', 'm7'], ['t1'], ['-3'], [])
        o40 = Operation(['m1', 'm2', 'm7'], ['t2', 't5', 't13'], ['-3', '-2'], [])
        o41 = Operation(['m2', 'm3', 'm5', 'm6', 'm7'], ['t7', 't9', 't10'], ['-3', '-2', '-1', '0'], [])
        o42 = Operation(['m1'], ['t13', 't14'], ['-3'], [])
        o43 = Operation(['m3'], ['t5'], ['-3'], ['o61'])
        o44 = Operation(['m5', 'm7'], ['t4', 't5', 't7', 't12', 't13'], ['-2', '1', '3'], ['o60'])
        o45 = Operation(['m2', 'm5', 'm7'], ['t3'], ['1'], ['o3', 'o35'])
        o46 = Operation(['m1', 'm3', 'm4', 'm5', 'm6'], ['t14'], ['-3'], [])
        o47 = Operation(['m5', 'm7'], ['t1', 't9', 't13'], ['-3', '1', '2'], ['o50'])
        o48 = Operation(['m5'], ['t8', 't9'], ['-2', '-1', '0', '3'], ['o23'])
        o49 = Operation(['m1', 'm5', 'm6'], ['t1', 't11'], ['1', '2'], ['o5'])
        o50 = Operation(['m2'], ['t5', 't10'], ['2', '3'], ['o43', 'o55'])
        o51 = Operation(['m5', 'm7'], ['t3', 't5'], ['1', '3'], ['o12', 'o60'])
        o52 = Operation(['m2', 'm5'], ['t10'], ['-1', '2'], [])
        o53 = Operation(['m2', 'm3', 'm7'], ['t1', 't12'], ['-2', '0'], ['o30'])
        o54 = Operation(['m1', 'm3', 'm6', 'm7'], ['t14'], ['2', '3'], [])
        o55 = Operation(['m1', 'm2', 'm6'], ['t1', 't7', 't10', 't11', 't12'], ['-2'], ['o16', 'o18'])
        o56 = Operation(['m4', 'm7'], ['t5', 't12'], ['-3', '2'], [])
        o57 = Operation(['m3', 'm4', 'm6'], ['t1', 't3', 't10'], ['0', '3'], ['o39', 'o53'])
        o58 = Operation(['m7'], ['t7'], ['1', '2'], ['o54'])
        o59 = Operation(['m3'], ['t2', 't7'], ['0', '1', '2'], [])
        o60 = Operation(['m3', 'm4', 'm7'], ['t4', 't5', 't6', 't11'], ['0'], ['o23', 'o31'])
        o61 = Operation(['m1'], ['t2', 't5', 't11'], ['-2'], ['o16', 'o49'])
        o62 = Operation(['m6'], ['t5', 't6', 't8'], ['2'], ['o66'])
        o63 = Operation(['m5'], ['t2', 't4', 't5', 't8', 't9'], ['-3', '-2'], ['o16', 'o62'])
        o64 = Operation(['m7'], ['t5', 't9', 't11'], ['-3', '-2', '-1', '0'], ['o8'])
        o65 = Operation(['m1', 'm2', 'm3', 'm4'], ['t3', 't5', 't6', 't7'], ['-1'], ['o53'])
        o66 = Operation(['m1'], ['t4', 't6', 't9', 't14'], ['-3', '-1', '3'], ['o25'])
        o67 = Operation(['m2', 'm3', 'm6'], ['t2', 't10'], ['-1', '1'], ['o28'])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67,
        }

        # alternatives
        alternative_operations = {
            'o1': {'o15'},
            'o2': {'o36'},
            'o3': {'o14'},
            'o5': {'o44', 'o54'},
            'o7': {'o30', 'o58'},
            'o8': {'o45', 'o63'},
            'o9': {'o10', 'o59'},
            'o10': {'o9', 'o59'},
            'o11': {'o16', 'o23'},
            'o14': {'o3'},
            'o15': {'o1'},
            'o16': {'o11', 'o23'},
            'o17': {'o49', 'o65'},
            'o18': {'o37', 'o62'},
            'o19': {'o39', 'o52'},
            'o20': {'o48', 'o64'},
            'o21': {'o56', 'o66'},
            'o22': {'o50'},
            'o23': {'o11', 'o16'},
            'o24': {'o57'},
            'o26': {'o55'},
            'o27': {'o38'},
            'o29': {'o34', 'o67'},
            'o30': {'o7', 'o58'},
            'o31': {'o35', 'o60'},
            'o34': {'o29', 'o67'},
            'o35': {'o31', 'o60'},
            'o36': {'o2'},
            'o37': {'o18', 'o62'},
            'o38': {'o27'},
            'o39': {'o19', 'o52'},
            'o44': {'o5', 'o54'},
            'o45': {'o8', 'o63'},
            'o47': {'o61'},
            'o48': {'o20', 'o64'},
            'o49': {'o17', 'o65'},
            'o50': {'o22'},
            'o52': {'o19', 'o39'},
            'o54': {'o5', 'o44'},
            'o55': {'o26'},
            'o56': {'o21', 'o66'},
            'o57': {'o24'},
            'o58': {'o7', 'o30'},
            'o59': {'o9', 'o10'},
            'o60': {'o31', 'o35'},
            'o61': {'o47'},
            'o62': {'o18', 'o37'},
            'o63': {'o8', 'o45'},
            'o64': {'o20', 'o48'},
            'o65': {'o17', 'o49'},
            'o66': {'o21', 'o56'},
            'o67': {'o29', 'o34'},
        }
        alternatives = [
            {'o1', 'o15'},
            {'o2', 'o36'},
            {'o3', 'o14'},
            {'o5', 'o44', 'o54'},
            {'o7', 'o30', 'o58'},
            {'o8', 'o45', 'o63'},
            {'o9', 'o10', 'o59'},
            {'o11', 'o16', 'o23'},
            {'o17', 'o49', 'o65'},
            {'o18', 'o37', 'o62'},
            {'o19', 'o39', 'o52'},
            {'o20', 'o48', 'o64'},
            {'o21', 'o56', 'o66'},
            {'o22', 'o50'},
            {'o24', 'o57'},
            {'o26', 'o55'},
            {'o27', 'o38'},
            {'o29', 'o34', 'o67'},
            {'o31', 'o35', 'o60'},
            {'o47', 'o61'},
        ]

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    elif case_idx == 24:
        """
        Case 24: cost minimization

        Details:
            - the number of operations: 91
            - the number of machines: 10
            - the number of tools: 14
            - the number of directions: 7
            - alternative operations: Y
        """
        case_type = {'objective': 'cost', 'alternative': True}

        # machine usage cost
        muc = {'m1': 42, 'm2': 66, 'm3': 11, 'm4': 79, 'm5': 21, 'm6': 16, 'm7': 44, 'm8': 87, 'm9': 62, 'm10': 12}
        # tool usage cost
        tuc = {'t1': 9, 't2': 18, 't3': 10, 't4': 19, 't5': 14, 't6': 5, 't7': 12, 't8': 18, 't9': 11, 't10': 6,
               't11': 12, 't12': 12, 't13': 15, 't14': 9}
        # machine changeover cost
        mcc = 476
        # tool changeover cost
        tcc = 11
        # setup changeover cost
        scc = 86

        # operations
        o1 = Operation(['m4', 'm5', 'm6', 'm7', 'm10'], ['t6', 't11'], ['-2', '0'], ['o61', 'o79'])
        o2 = Operation(['m8'], ['t1', 't6', 't13'], ['1', '2'], [])
        o3 = Operation(['m1', 'm3', 'm6', 'm8'], ['t3', 't12', 't13'], ['-2', '0', '3'], [])
        o4 = Operation(['m6'], ['t1', 't9', 't14'], ['-2', '2', '3'], [])
        o5 = Operation(['m7'], ['t12'], ['-3', '-1', '0'], ['o42', 'o51', 'o60', 'o71'])
        o6 = Operation(['m5', 'm6'], ['t6', 't7'], ['0', '2'], [])
        o7 = Operation(['m1', 'm7', 'm8', 'm10'], ['t11', 't14'], ['0', '1', '3'], [])
        o8 = Operation(['m3'], ['t2', 't3', 't13'], ['-3', '0'], ['o61'])
        o9 = Operation(['m2', 'm4'], ['t1', 't3', 't4', 't6'], ['-3', '-2', '1'], ['o4', 'o73'])
        o10 = Operation(['m2', 'm6', 'm7'], ['t7'], ['-2', '-1', '3'], [])
        o11 = Operation(['m6'], ['t2', 't11'], ['-2', '1', '3'], [])
        o12 = Operation(['m5'], ['t1', 't2', 't13'], ['-2', '0', '3'], ['o23'])
        o13 = Operation(['m1', 'm3', 'm5'], ['t4', 't5', 't9', 't11', 't13'], ['-2', '-1'], ['o57'])
        o14 = Operation(['m2', 'm4', 'm7', 'm9'], ['t2', 't9', 't12'], ['0', '2'], ['o64'])
        o15 = Operation(['m1', 'm5', 'm7', 'm10'], ['t1', 't9'], ['-2', '-1', '1', '2'], [])
        o16 = Operation(['m1', 'm6', 'm9'], ['t10', 't11'], ['0', '1'], [])
        o17 = Operation(['m5', 'm6'], ['t1', 't12', 't14'], ['-3', '-2', '2', '3'], [])
        o18 = Operation(['m1', 'm5', 'm7', 'm8', 'm10'], ['t3'], ['-2', '3'], ['o70'])
        o19 = Operation(['m2', 'm4', 'm6', 'm9'], ['t2', 't3', 't8', 't10'], ['-3', '-1', '0', '3'], [])
        o20 = Operation(['m1', 'm3', 'm8'], ['t8', 't12'], ['-2', '1'], [])
        o21 = Operation(['m4'], ['t1', 't4', 't7', 't14'], ['2'], ['o80'])
        o22 = Operation(['m3', 'm6', 'm8', 'm10'], ['t6', 't9'], ['0', '1', '2'], [])
        o23 = Operation(['m2', 'm5', 'm8'], ['t1'], ['-3', '-1', '1', '3'], ['o30', 'o85'])
        o24 = Operation(['m2', 'm5'], ['t7', 't12'], ['-3', '1'], [])
        o25 = Operation(['m4', 'm6'], ['t3', 't10', 't14'], ['0', '2', '3'], ['o75'])
        o26 = Operation(['m1', 'm2', 'm5', 'm7', 'm10'], ['t4', 't8', 't10', 't11'], ['-2', '3'], ['o8'])
        o27 = Operation(['m5'], ['t5', 't6', 't11', 't13'], ['0', '2'], ['o39'])
        o28 = Operation(['m2', 'm4', 'm8'], ['t14'], ['-1'], [])
        o29 = Operation(['m7'], ['t1', 't3', 't4', 't5', 't14'], ['-2', '0'], ['o69'])
        o30 = Operation(['m3', 'm6', 'm8'], ['t1', 't3', 't6', 't7', 't12'], ['-2', '3'], ['o58'])
        o31 = Operation(['m1', 'm8', 'm9'], ['t2', 't4'], ['2', '3'], ['o1', 'o55'])
        o32 = Operation(['m3'], ['t6', 't12'], ['-2', '1'], ['o26', 'o31', 'o37', 'o62'])
        o33 = Operation(['m1', 'm4'], ['t1', 't5', 't6', 't9', 't11'], ['-2', '1', '2'], ['o70'])
        o34 = Operation(['m2', 'm8'], ['t5', 't8', 't13'], ['-3', '2'], ['o2'])
        o35 = Operation(['m9', 'm10'], ['t4'], ['2'], [])
        o36 = Operation(['m5', 'm9', 'm10'], ['t6', 't9', 't11'], ['-3', '-1', '2'], [])
        o37 = Operation(['m3', 'm4', 'm10'], ['t8', 't10'], ['3'], ['o7'])
        o38 = Operation(['m4'], ['t8'], ['2'], ['o30'])
        o39 = Operation(['m4', 'm10'], ['t3', 't4', 't11', 't14'], ['-2', '-1', '2'], ['o35'])
        o40 = Operation(['m3', 'm10'], ['t6', 't10', 't11'], ['-3', '-2', '1', '3'], ['o90'])
        o41 = Operation(['m1', 'm2', 'm10'], ['t14'], ['-1', '2'], ['o85'])
        o42 = Operation(['m2'], ['t12'], ['-2', '1'], [])
        o43 = Operation(['m6', 'm10'], ['t3', 't5', 't6', 't11'], ['-3', '-1', '2', '3'], [])
        o44 = Operation(['m1'], ['t4', 't12'], ['-1', '2'], [])
        o45 = Operation(['m4', 'm7'], ['t5', 't7'], ['-3'], ['o24'])
        o46 = Operation(['m8', 'm10'], ['t1', 't6', 't10'], ['-2', '-1', '0'], ['o69'])
        o47 = Operation(['m3', 'm5'], ['t3', 't12'], ['-1', '1', '2'], ['o55'])
        o48 = Operation(['m4', 'm10'], ['t2', 't14'], ['-2', '-1'], ['o85'])
        o49 = Operation(['m6'], ['t1', 't5', 't9'], ['-2', '-1', '3'], [])
        o50 = Operation(['m4', 'm6', 'm7', 'm10'], ['t5', 't6', 't11'], ['-2', '-1', '1'], ['o35'])
        o51 = Operation(['m3', 'm4', 'm9', 'm10'], ['t4', 't10'], ['2'], ['o87'])
        o52 = Operation(['m1', 'm2', 'm4', 'm5', 'm10'], ['t6'], ['2', '3'], ['o76'])
        o53 = Operation(['m2', 'm7'], ['t4', 't7', 't8', 't10'], ['-2'], ['o39'])
        o54 = Operation(['m3', 'm6', 'm8'], ['t4', 't5', 't14'], ['-3', '-2', '3'], [])
        o55 = Operation(['m1', 'm2', 'm6', 'm10'], ['t8'], ['-2', '-1', '2', '3'], ['o64'])
        o56 = Operation(['m5', 'm7', 'm8', 'm9', 'm10'], ['t3', 't4'], ['-1', '2'], [])
        o57 = Operation(['m7', 'm8', 'm10'], ['t7', 't8', 't12'], ['0', '1'], [])
        o58 = Operation(['m3', 'm5', 'm6', 'm8'], ['t4', 't5'], ['-3', '0'], ['o6'])
        o59 = Operation(['m9'], ['t1', 't2', 't12', 't14'], ['-2', '-1', '1', '3'], [])
        o60 = Operation(['m2', 'm4', 'm6', 'm9'], ['t9'], ['-3', '-2', '-1', '1'], ['o11', 'o69'])
        o61 = Operation(['m2', 'm6', 'm7', 'm10'], ['t4', 't6', 't13'], ['-3', '3'], [])
        o62 = Operation(['m2', 'm4', 'm5', 'm6'], ['t3', 't5', 't10', 't13'], ['-1', '0', '1'], ['o91'])
        o63 = Operation(['m6', 'm8', 'm9', 'm10'], ['t13'], ['-3', '-1', '1', '2'], [])
        o64 = Operation(['m9'], ['t1', 't5', 't10', 't12'], ['-2', '2', '3'], [])
        o65 = Operation(['m1', 'm7', 'm8', 'm9'], ['t5', 't6', 't7', 't10'], ['-3', '-2'], ['o24', 'o25', 'o75'])
        o66 = Operation(['m5', 'm7'], ['t10', 't12'], ['-2', '1', '3'], ['o72'])
        o67 = Operation(['m5'], ['t1', 't6', 't9', 't11', 't12'], ['-3', '1'], ['o25'])
        o68 = Operation(['m2', 'm3', 'm4'], ['t5', 't7'], ['0'], ['o22', 'o33'])
        o69 = Operation(['m3', 'm8'], ['t7', 't10'], ['-2', '0', '2'], [])
        o70 = Operation(['m1', 'm4', 'm10'], ['t5', 't9', 't13'], ['-2', '-1', '0', '2'], ['o44'])
        o71 = Operation(['m8'], ['t6'], ['-1', '3'], ['o15', 'o18'])
        o72 = Operation(['m2', 'm6', 'm7'], ['t7', 't11', 't14'], ['0'], [])
        o73 = Operation(['m6'], ['t4', 't7', 't9', 't13', 't14'], ['-2', '0', '3'], ['o3'])
        o74 = Operation(['m2', 'm7', 'm8', 'm9'], ['t2', 't7', 't8', 't12', 't13'], ['-3', '0', '1', '2'], ['o66'])
        o75 = Operation(['m7'], ['t9'], ['-3', '-2', '2'], ['o82'])
        o76 = Operation(['m2'], ['t5', 't6', 't7', 't13'], ['-1'], ['o22', 'o59'])
        o77 = Operation(['m1', 'm10'], ['t11'], ['1'], [])
        o78 = Operation(['m4', 'm5'], ['t1', 't6', 't7', 't9'], ['-3', '-1'], [])
        o79 = Operation(['m2', 'm3', 'm4', 'm7'], ['t12'], ['-2'], ['o27'])
        o80 = Operation(['m4', 'm6', 'm10'], ['t2', 't6', 't13'], ['-3'], ['o9'])
        o81 = Operation(['m2', 'm6', 'm7', 'm8'], ['t10'], ['0'], [])
        o82 = Operation(['m7', 'm8'], ['t5', 't6', 't13', 't14'], ['-2', '-1'], [])
        o83 = Operation(['m6'], ['t13'], ['2', '3'], [])
        o84 = Operation(['m2', 'm3', 'm6', 'm8'], ['t8', 't9'], ['-2', '0'], [])
        o85 = Operation(['m1', 'm6', 'm7'], ['t9', 't11'], ['-3', '-1'], ['o37'])
        o86 = Operation(['m2', 'm3', 'm5', 'm9'], ['t5', 't8', 't11', 't12', 't14'], ['-1'], [])
        o87 = Operation(['m9'], ['t3', 't7', 't8', 't13'], ['2'], [])
        o88 = Operation(['m6'], ['t2', 't10'], ['1'], ['o24', 'o71'])
        o89 = Operation(['m2', 'm6'], ['t6', 't10', 't11'], ['-1', '3'], ['o10'])
        o90 = Operation(['m4', 'm7', 'm8'], ['t3', 't10'], ['-1', '0'], [])
        o91 = Operation(['m4', 'm6'], ['t6'], ['-3', '-2', '-1', '0'], [])
        operations = {
            'o1': o1, 'o2': o2, 'o3': o3, 'o4': o4, 'o5': o5, 'o6': o6, 'o7': o7, 'o8': o8, 'o9': o9, 'o10': o10,
            'o11': o11, 'o12': o12, 'o13': o13, 'o14': o14, 'o15': o15, 'o16': o16, 'o17': o17, 'o18': o18,
            'o19': o19, 'o20': o20, 'o21': o21, 'o22': o22, 'o23': o23, 'o24': o24, 'o25': o25, 'o26': o26,
            'o27': o27, 'o28': o28, 'o29': o29, 'o30': o30, 'o31': o31, 'o32': o32, 'o33': o33, 'o34': o34,
            'o35': o35, 'o36': o36, 'o37': o37, 'o38': o38, 'o39': o39, 'o40': o40, 'o41': o41, 'o42': o42,
            'o43': o43, 'o44': o44, 'o45': o45, 'o46': o46, 'o47': o47, 'o48': o48, 'o49': o49, 'o50': o50,
            'o51': o51, 'o52': o52, 'o53': o53, 'o54': o54, 'o55': o55, 'o56': o56, 'o57': o57, 'o58': o58,
            'o59': o59, 'o60': o60, 'o61': o61, 'o62': o62, 'o63': o63, 'o64': o64, 'o65': o65, 'o66': o66,
            'o67': o67, 'o68': o68, 'o69': o69, 'o70': o70, 'o71': o71, 'o72': o72, 'o73': o73, 'o74': o74,
            'o75': o75, 'o76': o76, 'o77': o77, 'o78': o78, 'o79': o79, 'o80': o80, 'o81': o81, 'o82': o82,
            'o83': o83, 'o84': o84, 'o85': o85, 'o86': o86, 'o87': o87, 'o88': o88, 'o89': o89, 'o90': o90,
            'o91': o91,
        }

        # alternatives
        alternative_operations = {
            'o1': {'o3'},
            'o2': {'o32'},
            'o3': {'o1'},
            'o4': {'o55', 'o91'},
            'o5': {'o47'},
            'o6': {'o37', 'o83'},
            'o7': {'o40', 'o68'},
            'o8': {'o49', 'o50'},
            'o9': {'o11'},
            'o10': {'o17', 'o60'},
            'o11': {'o9'},
            'o12': {'o58', 'o76'},
            'o13': {'o86'},
            'o15': {'o79', 'o82'},
            'o17': {'o10', 'o60'},
            'o22': {'o52', 'o56'},
            'o23': {'o73'},
            'o26': {'o38'},
            'o30': {'o62', 'o67'},
            'o31': {'o88'},
            'o32': {'o2'},
            'o33': {'o59'},
            'o34': {'o87'},
            'o35': {'o45'},
            'o37': {'o6', 'o83'},
            'o38': {'o26'},
            'o39': {'o71', 'o89'},
            'o40': {'o7', 'o68'},
            'o41': {'o54', 'o77'},
            'o43': {'o44', 'o48'},
            'o44': {'o43', 'o48'},
            'o45': {'o35'},
            'o47': {'o5'},
            'o48': {'o43', 'o44'},
            'o49': {'o8', 'o50'},
            'o50': {'o8', 'o49'},
            'o51': {'o65', 'o84'},
            'o52': {'o22', 'o56'},
            'o53': {'o64'},
            'o54': {'o41', 'o77'},
            'o55': {'o4', 'o91'},
            'o56': {'o22', 'o52'},
            'o57': {'o85'},
            'o58': {'o12', 'o76'},
            'o59': {'o33'},
            'o60': {'o10', 'o17'},
            'o61': {'o90'},
            'o62': {'o30', 'o67'},
            'o63': {'o78'},
            'o64': {'o53'},
            'o65': {'o51', 'o84'},
            'o67': {'o30', 'o62'},
            'o68': {'o7', 'o40'},
            'o70': {'o75'},
            'o71': {'o39', 'o89'},
            'o72': {'o80'},
            'o73': {'o23'},
            'o75': {'o70'},
            'o76': {'o12', 'o58'},
            'o77': {'o41', 'o54'},
            'o78': {'o63'},
            'o79': {'o15', 'o82'},
            'o80': {'o72'},
            'o82': {'o15', 'o79'},
            'o83': {'o6', 'o37'},
            'o84': {'o51', 'o65'},
            'o85': {'o57'},
            'o86': {'o13'},
            'o87': {'o34'},
            'o88': {'o31'},
            'o89': {'o39', 'o71'},
            'o90': {'o61'},
            'o91': {'o4', 'o55'},
        }
        alternatives = [
            {'o1', 'o3'},
            {'o2', 'o32'},
            {'o4', 'o55', 'o91'},
            {'o5', 'o47'},
            {'o6', 'o37', 'o83'},
            {'o7', 'o40', 'o68'},
            {'o8', 'o49', 'o50'},
            {'o9', 'o11'},
            {'o10', 'o17', 'o60'},
            {'o12', 'o58', 'o76'},
            {'o13', 'o86'},
            {'o15', 'o79', 'o82'},
            {'o22', 'o52', 'o56'},
            {'o23', 'o73'},
            {'o26', 'o38'},
            {'o30', 'o62', 'o67'},
            {'o31', 'o88'},
            {'o33', 'o59'},
            {'o34', 'o87'},
            {'o35', 'o45'},
            {'o39', 'o71', 'o89'},
            {'o41', 'o54', 'o77'},
            {'o43', 'o44', 'o48'},
            {'o51', 'o65', 'o84'},
            {'o53', 'o64'},
            {'o57', 'o85'},
            {'o61', 'o90'},
            {'o62', 'o30', 'o67'},
            {'o63', 'o78'},
            {'o70', 'o75'},
            {'o72', 'o80'},
        ]

        specifications['type'] = case_type
        specifications['muc'] = muc
        specifications['tuc'] = tuc
        specifications['mcc'] = mcc
        specifications['tcc'] = tcc
        specifications['scc'] = scc
        specifications['operations'] = operations
        specifications['alternative_operations'] = alternative_operations
        specifications['alternatives'] = alternatives

    else:
        raise ValueError("Invalid case number.")

    op2ind = {}
    ind2op = {}
    temp_ind = 0
    for key in operations:
        op2ind[key] = temp_ind
        ind2op[temp_ind] = key
        temp_ind += 1

    indices = {}
    if specifications['type']['objective'] == 'cost':
        for o in operations.keys():
            indices[o] = {}
            operation = operations[o]
            for m in operation.machine:
                for t in operation.tool:
                    # usage cost
                    uc = muc[m] + tuc[t]
                    for d in operation.direction:
                        ind = o + '&' + m + '&' + t + '&' + d
                        indices[o][ind] = uc
    else:
        for o in operations.keys():
            indices[o] = {}
            operation = operations[o]
            num_machines = len(operation.machine)
            num_tools = len(operation.tool)
            flag = num_tools * num_machines > len(operation.time)
            for ind_m, m in enumerate(operation.machine):
                if flag:
                    for t in operation.tool:
                        # processing time
                        pt = operation.time[ind_m]
                        for d in operation.direction:
                            ind = o + '&' + m + '&' + t + '&' + d
                            indices[o][ind] = pt
                else:
                    for ind_t, t in enumerate(operation.tool):
                        # processing time
                        pt = operation.time[ind_m * num_tools + ind_t]
                        for d in operation.direction:
                            ind = o + '&' + m + '&' + t + '&' + d
                            indices[o][ind] = pt

    specifications['op2ind'] = op2ind
    specifications['ind2op'] = ind2op
    specifications['indices'] = indices

    return specifications
