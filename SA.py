import numpy as np
import math 

class SA(object):
    '''
    Ref : CSDN:
    https://blog.csdn.net/weixin_45666249/article/details/113761920?spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-113761920-blog-113173241.pcrelevantt0_20220926_downloadratepraise_v1&utm_relevant_index=4
    '''
    def __init__(self, func_objective):
        self.func_objective = func_objective
        print("Init_SA")

    def proceed(self):
        # 模拟退火模型构建
        T  = 10000                                # 温度
        T0 = T                                      # 初始温度
        Tmin = 0                                    # 最小温度
        Tmin = 0.1                                  # 最小温度
        t = 0                                       # 时间
        k = 50                                      # 每个温度的迭代次数
        upper_bound = 500
        lower_bound = -500
        x1 = np.random.uniform(low=lower_bound,high=upper_bound)       # 随机化初始值
        x2 = np.random.uniform(low=lower_bound,high=upper_bound)       # 随机化初始值
        y = 0                                       # y初始值
        step = 5

        while T > Tmin:
            for i in range(k):
                y = self.func_objective(x1,x2)                                  # 目标函数
                x1New = x1 + np.random.uniform(low=-1*step,high=+1*step)   # 更新xNew
                x2New = x2 + np.random.uniform(low=-1*step,high=+1*step)   # 更新xNew
                yNew = self.func_objective(x1New, x2New)							# 求出新状态值
                if (x1New < upper_bound and x1New > lower_bound) and (x2New < upper_bound and x2New > lower_bound):							# 状态比较
                    if y > yNew:
                        x1 = x1New
                        x2 = x2New
                    else:
                        r = np.random.uniform(low=0,high=1)         # 随机数
                        p = math.exp(-(yNew-y)/T)                   # 概率值
                        if r < p:                                   # 小于则更新
                            x1 = x1New
                            x2 = x2New
            t = t + 1
            T = T0/(1+t)                                            # 快速模拟退火算法降温方式
            print("t:",t," T:",T,'x1:{0}, x2:{1}'.format(x1,x2))
