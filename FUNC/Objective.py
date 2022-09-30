import numpy as np
import math
class Objective(object):
    ''' Objective Function Class '''

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