import numpy as np
import math 

from FUNC.Objective import Objective

class SA(object):
    '''
    Ref : 
    1. Course Material Ch2_Single_State_Algorithms.pdf => Page.33
    2. CSDN: https://blog.csdn.net/weixin_45666249/article/details/113761920?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&utm_relevant_index=4
    '''
    def __init__(self, lower_bound,  upper_bound, iteration_times, func_objective, update_step, dim:int=10, precision_level = 1e-6):
        self.func_objective = func_objective
        self.list_point = list()
        print("Init_SA")
        self.Temperature_now = 100
        self.Temperature_start = self.Temperature_now
        self.Temperature_min = .1
        self.time = 0
        self.k = iteration_times                                     
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.update_step = update_step
        self.fitness_repeat_times = 0
        self.fitness_repeat_times_limit = 10
        self.dim = dim
        self.precision_level = precision_level# 1e-6

    def proceed(self):
        '''
        Process
        '''
        x1 = np.random.uniform(low=self.lower_bound,high=self.upper_bound)       # Random Set Init x1, x2
        #x2 = np.random.uniform(low=self.lower_bound,high=self.upper_bound)
        self.list_point.append([x1])
        y = 0                                                                    # declare y value                                               # 每次前進位移距離 

        while self.Temperature_now > self.Temperature_min:
            for _ in range(self.k):
                y = self.func_objective(x1,self.dim)                                   # 目標涵式, 適應值
                x1New = x1 + np.random.uniform(low=-1*self.update_step,high=+1*self.update_step)         # 更新 x1, x2
                #x2New = x2 + np.random.uniform(low=-1*self.update_step,high=+1*self.update_step)         
                yNew = self.func_objective(x1New)						 # 計算更新後數值

                if (x1New < self.upper_bound and x1New > self.lower_bound):  #確認產生值小於邊界							
                    if y > yNew:                                                 # 若亂數產生值高於目標值, 更新x1, x2 座標
                        x1 = x1New
                        #print(abs(yNew-y), yNew)
                        if abs(yNew) <= self.precision_level:
                            self.update_step = self.precision_level
                        if abs(yNew-y) <= self.precision_level:                 # precision_level
                            break
                    else:
                        r = np.random.uniform(low=0,high=1)                      # 隨機產生亂數
                        p = math.exp(-(yNew-y)/self.Temperature_now)                # 概率值
                        if r < p:                                                # 若小於該機率則同樣更新
                            x1 = x1New

            self.time = self.time + 1                                            # 計算次數
            self.Temperature_now = self.Temperature_start/(1+self.time)                # 降溫
            print("Times:",self.time," Temprate_now:",self.Temperature_now,'x : {0}'.format(x1))
            self.list_point.append([x1])

def main():
    #print('haloWord')
    
    # 設定初始變數, 目標函式, 上下界資訊, 迭代次數
    func_objctive = Objective.func_objective_hw2_q11
    lower_bound, upper_bound = -4, 5
    sa_update_step = 1e-1
    #graph = Objective_Graph(upper_bound,.1)
    repeat_value_range = 10
    iteration_times = 20000
    SA_Obj = SA(lower_bound, upper_bound, iteration_times, func_objctive, sa_update_step, repeat_value_range)
    SA_Obj.proceed()


if __name__ == '__main__':
    main()
    