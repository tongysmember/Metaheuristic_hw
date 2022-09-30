from FUNC.Objective import Objective
from ALGO.SA import SA
from ALGO.GA import GA

from FUNC.GRAPH import Objective_Graph


def main():
    '''
    1. 設定初始變數
    2. 計算 Simulate Annealing Algorighm
    3. 計算 Genetic Algorithm
    '''

    # 設定初始變數, 目標函式, 上下界資訊, 迭代次數
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

    
    # Simulate Annealing Algorighm
    iteration_times = 10
    SA_Obj = SA(lower_bound, upper_bound, iteration_times, func_objctive, sa_update_step, repeat_value_range)
    SA_Obj.proceed()
    #graph.Draw_graph_2D(func_objctive, list(SA_Obj.list_point))
    graph.Draw_graph_3D(func_objctive, list(SA_Obj.list_point))

    ## Genetic Algorithm
    #iteration_times = 5000
    #GA_Obj = GA(lower_bound, upper_bound, iteration_times, func_objctive)
    #GA_Obj.proceed()
    #graph.Draw_graph_2D(func_objctive, list(GA_Obj.list_point))
    #graph.Draw_graph_3D(func_objctive, list(GA_Obj.list_point))
  
    
    

if __name__ == '__main__':
    main()