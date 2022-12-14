import numpy as np
import math 

class SA(object):
    '''
    Ref : 
    1. Course Material Ch2_Single_State_Algorithms.pdf => Page.33
    2. CSDN: https://blog.csdn.net/weixin_45666249/article/details/113761920?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&utm_relevant_index=4
    '''
    def __init__(self, lower_bound,  upper_bound, iteration_times, func_objective, update_step, repeat_value_range):
        self.func_objective = func_objective
        self.list_point = list()
        print("Init_SA")
        self.Temperature_now = 10
        self.Temperature_start = self.Temperature_now
        self.Temperature_min = .1
        self.time = 0
        self.k = iteration_times                                     
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.update_step = update_step
        self.fitness_repeat_times = 0
        self.fitness_repeat_times_limit = 10
        self.repeat_value_range = repeat_value_range

    def proceed(self):
        '''
        Process
        '''
        x1 = np.random.uniform(low=self.lower_bound,high=self.upper_bound)       # Random Set Init x1, x2
        x2 = np.random.uniform(low=self.lower_bound,high=self.upper_bound)
        self.list_point.append([x1, x2])
        y = 0                                                                    # declare y value
        step = self.update_step                                                  # 每次前進位移距離 

        while self.Temperature_now > self.Temperature_min:
            for _ in range(self.k):
                y = self.func_objective(x1,x2)                                   # 目標涵式, 適應值
                x1New = x1 + np.random.uniform(low=-1*step,high=+1*step)         # 更新 x1, x2
                x2New = x2 + np.random.uniform(low=-1*step,high=+1*step)         
                yNew = self.func_objective(x1New, x2New)						 # 計算更新後數值

                if (x1New < self.upper_bound and x1New > self.lower_bound) and (x2New < self.upper_bound and x2New > self.lower_bound):  #確認產生值小於邊界							
                    if y > yNew:                                                 # 若亂數產生值高於目標值, 更新x1, x2 座標
                        x1 = x1New
                        x2 = x2New
                    else:
                        r = np.random.uniform(low=0,high=1)                      # 隨機產生亂數
                        p = math.exp(-(yNew-y)/self.Temperature_now)                # 概率值
                        if r < p:                                                # 若小於該機率則同樣更新
                            x1 = x1New
                            x2 = x2New

            self.time = self.time + 1                                            # 計算次數
            self.Temperature_now = self.Temperature_start/(1+self.time)                # 降溫
            print("Times:",self.time," Temprate_now:",self.Temperature_now,'x1:{0}, x2:{1}'.format(x1,x2))
            self.list_point.append([x1, x2])
