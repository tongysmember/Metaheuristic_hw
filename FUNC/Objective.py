import numpy as np
import math
class Objective(object):
    ''' Objective Function Class
    Homework1: https://github.com/tongysmember/Metaheuristic_hw/blob/master/Document/HW1/Homework%201.pdf
    Homework2: https://github.com/tongysmember/Metaheuristic_hw/blob/master/Document/HW2/Homework2_Metaheuristics.pdf
    '''

    # Homework 1 ===================================================
    @staticmethod
    def func_objective_q2(x1, x2):
        return abs(x1**2 + x2**2 + x1*x2)+ abs(np.sin(x1))+ abs(np.cos(x2))

    @staticmethod
    def func_objective_q5(x1, x2):
        return (x1 + 2*x2 -7)**2 + (2*x1 + x2 -5)**2

    @staticmethod
    def func_objective_q8(x1, x2):
        return 100*((x2 - x1**3)**2) + (1 - x1)**2

    @staticmethod
    def func_objective_q13(x1, x2):
        return 1 + (np.sin(x1))**2 + (np.sin(x2))**2 -0.1*math.e**(-1*(x1**2 + x2**2))

    # Homework 2 ===================================================
    @staticmethod
    def func_objective_hw2_q2(x, D:int=10):
        sum_value = 0
        for i in range(1,D,1):
            sum_value += x**4
        return sum_value
    
    @staticmethod
    def func_objective_hw2_q4(x, D:int=10):
        sum_value = 0
        for i in range(1,D,1):
            sum_value += i*(x**2)
        return sum_value