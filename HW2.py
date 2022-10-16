from FUNC.Objective import Objective
from FUNC.GRAPH import Objective_Graph
from ALGO.SA_limit import SA
from ALGO.GA_limit import GA
from ALGO.PSO import PSO
from FUNC.METRIC import metric_time, metric_memory
import random



class HW2(object):
    def __init__(self):
        '''
        Setting Init Env
        '''
        self.metric_obj = metric_time()
        self.lower_bound, self.upper_bound = -4, 5
        self.dim = 100 # 20,50
        self.func_objctive = Objective.func_objective_hw2_q11
        self.iteration_times = 20000
        self.sa_update_step = 1e-1
        self.graph = Objective_Graph(self.upper_bound,.1)

    def Algo_SA(self):
        print('SA')
        self.metric_obj.metric_time_start()

        SA_Obj = SA(self.lower_bound, self.upper_bound, self.iteration_times, self.func_objctive, self.sa_update_step, self.dim)
        SA_Obj.proceed()

        self.metric_obj.metric_time_end()
        self.metric_obj.metric_time_calculate()

        self.graph.Draw_graph_2D_Question(self.lower_bound, self.upper_bound, self.func_objctive, list(SA_Obj.list_point))
        print('SA_End')

        metric_memory.metric_memory_usage()
        del SA_Obj # release Object Memroy

    def Algo_GA(self):
        print('GA')
        ## Genetic Algorithm
        #iteration_times = 5000
        self.metric_obj.metric_time_start()
        GA_Obj = GA(self.lower_bound, self.upper_bound, self.iteration_times, self.func_objctive)
        GA_Obj.proceed()
        self.metric_obj.metric_time_end()
        self.metric_obj.metric_time_calculate()

        self.graph.Draw_graph_2D_Question(self.lower_bound, self.upper_bound, self.func_objctive, list(GA_Obj.list_point))
        print('GA_End')
        metric_memory.metric_memory_usage()
        del GA_Obj

    def Algo_PSO(self):
        print('PSO')
        # w,c1,c2,r1,r2,N,D,M参数初始化
        self.metric_obj.metric_time_start()
        self.metric_obj.metric_time_start()
        w=random.random()
        c1=c2=2#一般设置为2
        r1=0.7
        r2=0.5
        N=30
        D=1
        M=200
        PSO_Objt=PSO(w, self.lower_bound, self.upper_bound, c1,c2,r1,r2,N,D,M, self.func_objctive)#设置初始权值
        PSO_Objt.init_pop()
        PSO_Objt.proceed()
        self.metric_obj.metric_time_end()
        self.metric_obj.metric_time_calculate()
        print('PSO_End')
        metric_memory.metric_memory_usage()
        del PSO_Objt

def main():
        HW = HW2()
        HW.Algo_SA()
        HW.Algo_GA()
        HW.Algo_PSO()
    
    
if __name__ == '__main__':
    main()
        


def init():
    '''
    Setting Init Env
    '''
    global metric_obj, lower_bound, upper_bound, dim, func_objctive
    metric_obj = metric_time()
    lower_bound, upper_bound = -4, 5
    dim = 10 # 20,50
    func_objctive = Objective.func_objective_hw2_q11

def algo_SA():
    print('SA')
    global metric_obj
    global func_objctive

def algo_GA():
    print('GA')

def algo_PSO():
    print('PSO')

def main():
    '''
    1. 設定初始變數
    2. 計算 Simulate Annealing Algorighm
    3. 計算 Genetic Algorithm
    '''
    # 設定初始變數, 目標函式, 上下界資訊, 迭代次數
    metric_obj = metric_time()
    func_objctive = Objective.func_objective_hw2_q11
    lower_bound, upper_bound = -4, 5
    sa_update_step = 1e-1
    graph = Objective_Graph(upper_bound,.1)
    dim = 50
    #graph.Draw_graph_3D_Question(func_objctive)
    #repeat_value_range = 10
    iteration_times = 20000

    metric_obj.metric_time_start()

    SA_Obj = SA(lower_bound, upper_bound, iteration_times, func_objctive, sa_update_step, dim)
    SA_Obj.proceed()

    metric_obj.metric_time_end()
    print(metric_obj.metric_time_calculate())

    #graph.Draw_graph_3D(func_objctive, list(SA_Obj.list_point))
    #graph.Draw_graph_2D_Question(func_objctive, list(SA_Obj.list_point))
    graph.Draw_graph_2D_Question(lower_bound, upper_bound, func_objctive, list(SA_Obj.list_point))
    print('SA_End')

    metric_memory.metric_memory_usage()
    del SA_Obj # release Object Memroy

    ## Genetic Algorithm
    #iteration_times = 5000
    metric_obj.metric_time_start()
    GA_Obj = GA(lower_bound, upper_bound, iteration_times, func_objctive)
    GA_Obj.proceed()
    metric_obj.metric_time_end()
    print(metric_obj.metric_time_calculate())

    graph.Draw_graph_2D_Question(lower_bound, upper_bound, func_objctive, list(GA_Obj.list_point))
    print('GA_End')
    metric_memory.metric_memory_usage()






    