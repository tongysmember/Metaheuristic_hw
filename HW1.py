from Objective import Objective
from SA import SA
from GA4 import GeneAlgo

from GRAPH import Objective_Graph


def main():

    SA_Obj = SA(Objective.func_objective_q2)
    SA_Obj.proceed()
    
    #GA = GeneAlgo()
    #GA.proceed()

    #graph = Objective_Graph(500,.1)
    #graph.Draw_graph(Objective.func_objective_q2, list(SA_Obj.list_point)[::int(len(SA_Obj.list_point)/1000)])
    #graph.Draw_graph(Objective.func_objective_q2, list(SA_Obj.list_point))

if __name__ == '__main__':
    main()