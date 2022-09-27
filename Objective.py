import numpy as np

class Objective(object):
    ''' Objective Function Class '''
    @staticmethod
    def func_objective(x1, x2):
        return abs(x1**2 + x2**2 + x1*x2) + abs(np.sin(x1))+abs(np.cos(x2))
