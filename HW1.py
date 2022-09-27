from Objective import Objective
from SA import SA

def main():
    SA_Obj = SA(Objective.func_objective)
    SA_Obj.proceed()

if __name__ == '__main__':
    main()