from FUNC.Objective import Objective
from FUNC.GRAPH import Objective_Graph
from SA_limit import SA



def main():
    '''
    1. 設定初始變數
    2. 計算 Simulate Annealing Algorighm
    3. 計算 Genetic Algorithm
    '''
    # 設定初始變數, 目標函式, 上下界資訊, 迭代次數
    func_objctive = Objective.func_objective_hw2_q2
    lower_bound, upper_bound = -100, 100
    sa_update_step = 1e-1
    graph = Objective_Graph(upper_bound,.1)
    repeat_value_range = 10
    #graph.Draw_graph_3D_Question(func_objctive)
    #repeat_value_range = 10
    iteration_times = 20000
    SA_Obj = SA(lower_bound, upper_bound, iteration_times, func_objctive, sa_update_step, repeat_value_range)
    SA_Obj.proceed()

    #graph.Draw_graph_3D(func_objctive, list(SA_Obj.list_point))
    #graph.Draw_graph_2D_Question(func_objctive, list(SA_Obj.list_point))
    graph.Draw_graph_2D_Question(lower_bound, upper_bound, func_objctive, list(SA_Obj.list_point))
    print('End')
if __name__ == '__main__':
    main()
    