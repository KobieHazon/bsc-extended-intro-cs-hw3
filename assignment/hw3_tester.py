
##########################
#### HW3 TESTER 2018a ####
##########################

import sys

ALL_TESTS = {
    21: dict(
        seif_string='Q21',
        function=lambda f, check_func: check_func(find_root1(f)),
        func_name="find_root1",
        total_grade=6,
        tests=[
            dict(args=(lambda x: x - 1, 
                       lambda result: result is not None and result == 1), 
                 expected=True, symbol='T21_1', grade=3), 

            dict(args=(lambda x: x + 1,
                       lambda result: result is None),
                 expected=True, symbol='T21_2', grade=3), 
            ],
        ),

    22: dict(
        seif_string='Q22',
        function=lambda f, a, b, check_func: check_func(find_root_range(f, a, b)),
        func_name="find_root_range",
        total_grade=4,
        tests=[
            dict(args=(lambda x: x - 4, 3, 10, 
                       lambda result: result is not None and result == 4),
                 expected=True, symbol='T22_1', grade=2),

            dict(args=(lambda x: x - 20, 6, 19, 
                       lambda result: result is None),
                 expected=True, symbol='T22_2', grade=2),
            ],
        ),

    23: dict(
        seif_string='Q23',
        function=lambda f, check_func: check_func(find_root2(f)),
        func_name="find_root2",
        total_grade=4,
        tests=[
            dict(args=(lambda x: x - 1,
                       lambda result: result is not None and result == 1),
                 expected=True, symbol='T23_1', grade=2),
            dict(args=(lambda x: x**2 - 4,
                       lambda result: result is not None and result == 2),
                 expected=True, symbol='T23_2', grade=2)
              ],
        ),


    31: dict(
        seif_string='Q31',
        function=lambda lst, k, check_func: check_func(generate_sorted_blocks(lst, k)),
        func_name="generate_sorted_blocks",
        total_grade=5,
        tests=[
            dict(args=([19, 156, 322, 11, 188, 921, 543, 222], 3,
                       lambda result: result is not None and isinstance(result[-1], list) and result == [[19, 156, 322], [11, 188, 921], [222, 543]]),
                 expected=True, symbol='T31_1', grade=2,
                 help = "maybe the functions doesn't handle it's end."),
            dict(args=([13, 366, 12, 5, 77], 1,
                       lambda result: result is not None and result == [[13], [366], [12], [5], [77]]),
                 expected=True, symbol='T32_2', grade=1),
            dict(args=([13, 366, 12, 5, 77], 5,
                       lambda result: result is not None and result == [[5, 12, 13, 77, 366]]),
                 expected=True, symbol='T32_3', grade=1),
            dict(args=([], 5,
                       lambda result: result is not None and result == []),
                 expected=True, symbol='T32_4', grade=1)
             ],                    
        ),

    33: dict(
        seif_string='Q33',
        function=lambda lst, check_func: check_func(merge_sorted_blocks(lst)),
        func_name="merge_sorted_blocks",
        total_grade=5,
        tests=[
            dict(args=([[19, 156, 322], [11, 188, 921], [222, 543]],
                       lambda result: result is not None and isinstance(result[-1], int) and result == [11, 19, 156, 188, 222, 322, 543, 921]),
                 expected=True, symbol='T33_1', grade=2,
                 help="maybe the functions doesn't return one list."),
            dict(args=([[1]],
                       lambda result: result is not None and isinstance(result[-1], int) and result == [1]),
                 expected=True, symbol='T33_2', grade=1,
                 help="maybe the functions doesn't return one list."),
            dict(args=([[13], [366], [12], [5], [77]],
                       lambda result: result is not None and result == [5, 12, 13, 77, 366]),
                 expected=True, symbol='T33_3', grade=2)
            ],
            
        ),    


    51: dict(
        seif_string='Q51',
        function=lambda l, k, i: (sort_triplets1(l, k), l)[i],
        func_name="sort_triplets1",
        total_grade=5,
        tests=[
            dict(args=([(34, 22, 14), (1, 4, 7), (34, 22, 9), (1, 2, 2), (8, 8, 8), (8, 9, 10), (1, 7, 33), (50, 34, 11)], 100, 0),
                 expected=[(1, 2, 2), (1, 4, 7), (1, 7, 33), (8, 8, 8), (8, 9, 10), (34, 22, 9), (34, 22, 14), (50, 34, 11)],
                 symbol='T51_1', grade=2),
            dict(args=([(11, 11, 4), (11, 11, 3), (11, 11, 2), (11, 11, 1), (11, 11, 0)], 70, 0),
                 expected=[(11, 11, 0), (11, 11, 1), (11, 11, 2), (11, 11, 3), (11, 11, 4)],
                 symbol='T51_2', grade=2),
            dict(args=([(1, 1, 1), (3, 40, 6), (4, 2, 2), (4, 5, 9), (50, 50, 50)], 51, 1),
                 expected=[(1, 1, 1), (3, 40, 6), (4, 2, 2), (4, 5, 9), (50, 50, 50)],
                 symbol='T51_3', grade=1, 
                 help="function sort_triplets1 changed the list."),
            ],
        ),

    53: dict(
        seif_string='Q53',
        function=lambda l, k, i: (sort_triplets2(l, k), l)[i],
        func_name="sort_triplets2",
        total_grade=5,
        tests=[
            dict(args=([(56, 1, 3), (44, 1, 2), (1, 2, 4), (44, 5, 9), (44, 5, 7), (44, 5, 7), (0, 0, 0), (56, 1, 9), (30, 1, 2)], 100, 0),
                 expected=[(0, 0, 0), (1, 2, 4), (30, 1, 2), (44, 1, 2), (44, 5, 7), (44, 5, 7), (44, 5, 9), (56, 1, 3), (56, 1, 9)],
                 symbol='T53_1', grade=2),
            dict(args=([(5, 5, 4), (5, 5, 3), (9, 8, 3), (9, 7, 3), (20, 20, 20), (18, 18, 6)], 30, 0),
                 expected=[(5, 5, 3), (5, 5, 4), (9, 7, 3), (9, 8, 3), (18, 18, 6), (20, 20, 20)],
                 symbol='T53_2', grade=2),
            dict(args=([(1, 1, 1), (3, 40, 6), (4, 2, 2), (4, 5, 9), (50, 50, 50)], 51, 1),
                 expected=[(1, 1, 1), (3, 40, 6), (4, 2, 2), (4, 5, 9), (50, 50, 50)],
                 symbol='T53_3', grade=1, 
                 help="function sort_triplets2 changed the list."),
            ],
        ),
    
     61: dict(
        seif_string='Q6a',
        function=lambda f1, f2, check_func: check_func(equal(f1,f2)),
        func_name="equal",
        total_grade=4,
        tests=[
            dict(args=(lambda x: x+1, lambda x:-x-1, 
                       lambda result: result is not None and abs(abs(result)-1) <= 0.001),
                 expected=True, symbol='T6c1_1', grade=2),
            dict(args=(lambda x: x**2-1, lambda x:3, 
                       lambda result: result is not None and abs(result**2-4) <= 0.001),
                 expected=True, symbol='T6c1_2', grade=2),
            ],
        ),   
    
     631: dict(
        seif_string='Q6c1',
        function=lambda f, a, check_func: check_func(source(f,a)),
        func_name="source",
        total_grade=4,
        tests=[
            dict(args=(lambda x: x**2, 9, 
                       lambda result: result is not None and abs(abs(result)-3) <= 0.001),
                 expected=True, symbol='T6c1_1', grade=2),
            dict(args=(lambda x: x ** 2, -1, lambda result: result is None),
                 expected=True, symbol='T6c1_2', grade=2),
            ],
        ),
    
     632: dict(
        seif_string='Q6c2',
        function=lambda f, check_func:check_func(inverse(f)),
        func_name="inverse",
        total_grade=4,
        tests=[
            dict(args=(lambda x: x**3,  
                       lambda function: function is not None and callable(function) and abs(function(-27)+3) <= 0.001),
                 expected=True, symbol='T6c2_1', grade=2,
            help="Maybe the return value of inverse is not a function"),
            dict(args=(lambda x: 5*x - 3,  
                       lambda function: function is not None and callable(function) and abs(function(12)-3) <= 0.001),
                 expected=True, symbol='T6c2_2', grade=2,
            help="Maybe the return value of inverse is not a function"),
            ],
        ), 
}


def run_with_limited_time(func, args=(), kwargs={}, timeout_duration=10):
    """
    This function will spawn a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    """
    import threading

    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception:
                self.result = (sys.exc_info()[0], sys.exc_info()[1])

    it = InterruptableThread()
    it.daemon = True
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return [True, it.result]
    else:
        return [False, it.result]


def t(n=0):
    err_l = []
    err_s = []
    grade = 0

    for seif in ALL_TESTS:
        if n == 0 or seif == n or n == -1:
            function = ALL_TESTS[seif]['function']
            tests = ALL_TESTS[seif]['tests']
            seif_string = ALL_TESTS[seif]['seif_string']
            total_grade = ALL_TESTS[seif]['total_grade']
            func_name = ALL_TESTS[seif]['func_name']
            timeout_symbol = "T" + seif_string[1:] + "_t"
            time_to_run = ALL_TESTS[seif].get('time_to_run', 40)
            symbol = ''

            if n != -1:
                print("Test %s: %s: (%d)" % (func_name, seif_string, total_grade))

            for test in tests:
                exception_symbol = test['symbol'] + "_X"
                reduce = False

                timeout = run_with_limited_time(function, test['args'], {}, time_to_run)
                if timeout[0]:
                    err_l.append("%s: Timeout in %s (running time was longer than %d seconds) - [%s] - (%d)\n" % (seif_string, func_name, time_to_run, timeout_symbol, test['grade']))
                    reduce = True
                    symbol = timeout_symbol
                else:
                    res = timeout[1]
                    if isinstance(res, tuple):
                        e = timeout[1][1]
                        err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                        reduce = True
                        symbol = exception_symbol
                    else:
                        try:
                            if res != test['expected']:
                                err_l.append("%s: Error in %s - [%s] - (%d)" % (seif_string, func_name, test['symbol'], test['grade']))
                                if 'help' in test:
                                    err_l.append(test['help'])
                                err_l.append("Expected: " + str(test['expected']))
                                err_l.append("Got:      " + str(res) + "\n")
                                reduce = True
                                symbol = test['symbol']
                        except Exception:
                            e = sys.exc_info()[1]
                            err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                            reduce = True
                            symbol = exception_symbol

                if reduce:
                    err_s.append(symbol)
                    grade -= test['grade']

    if n != -1:
        print()
        print("\n".join(str(err) for err in err_l))
        print("Reduced grade: ",grade)

    return err_s,grade

t()
