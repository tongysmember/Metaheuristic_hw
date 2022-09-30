from FUNC.Objective import Objective
from ALGO.SA import SA
from ALGO.GA4 import GeneAlgo

from FUNC.GRAPH import Objective_Graph


def main():

    func_objctive = Objective.func_objective_q2
    lower_bound, upper_bound = -500, 500
    sa_update_step =5
    graph = Objective_Graph(upper_bound,.1)
    repeat_value_range = 10

    #func_objctive = Objective.func_objective_q5
    #lower_bound, upper_bound = -10, 10
    #sa_update_step =.1
    #graph = Objective_Graph(upper_bound,1)
    #repeat_value_range = 1

    #iteration_times = 10
    #SA_Obj = SA(lower_bound, upper_bound, iteration_times, func_objctive, sa_update_step, repeat_value_range)
    #SA_Obj.proceed()
    #graph.Draw_graph_2D(func_objctive, list(SA_Obj.list_point))
    #graph.Draw_graph_3D(func_objctive, list(SA_Obj.list_point))

    
    iteration_times = 5000
    GA = GeneAlgo(lower_bound, upper_bound, iteration_times, func_objctive)
    GA.proceed()
    graph.Draw_graph_2D(func_objctive, list(GA.list_point))
    graph.Draw_graph_3D(func_objctive, list(GA.list_point))
  
    
    

if __name__ == '__main__':
    main()