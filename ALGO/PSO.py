import numpy as np
import random


class PSO:
    '''
    Ref: https://blog.csdn.net/brilliantZC/article/details/123846525
    '''
    def __init__(self, lower_bound, upper_bound, w,c1,c2,r1,r2,N,D,M, func_objective):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.w = w # 惯性权值
        self.c1=c1
        self.c2=c2
        self.r1=r1
        self.r2=r2
        self.N=N # 初始化种群数量个数
        self.D=D # 搜索空间维度
        self.M=M # 迭代的最大次数
        self.x=np.zeros((self.N,self.D))  #粒子的初始位置
        self.v=np.zeros((self.N,self.D))  #粒子的初始速度
        self.pbest=np.zeros((self.N,self.D))  #个体最优值初始化
        self.gbest=np.zeros((1,self.D))  #种群最优值
        self.p_fit=np.zeros(self.N)
        self.fit=1e8 #初始化全局最优适应度
        self.func_objective = func_objective


     # 初始化种群
    def init_pop(self):
        for i in range(self.N):
            for j in range(self.D):
                self.x[i][j] = np.random.uniform(low=self.lower_bound,high=self.upper_bound) 
                self.v[i][j] = random.random()
            self.pbest[i] = self.x[i] # 初始化个体的最优值
            #aim=self.function(self.x[i]) # 计算个体的适应度值
            aim= self.func_objective(self.x[i][0]) # 计算个体的适应度值
            self.p_fit[i]=aim # 初始化个体的最优位置
            if aim < self.fit:  # 对个体适应度进行比较，计算出最优的种群适应度
                self.fit = aim
                self.gbest = self.x[i]

    # 更新粒子的位置与速度
    def proceed(self):
        for t in range(self.M): # 在迭代次数M内进行循环
            for i in range(self.N): # 对所有种群进行一次循环
                aim=self.func_objective(self.x[i][0]) # 计算一次目标函数的适应度
                if aim<self.p_fit[i]: # 比较适应度大小，将小的负值给个体最优
                    self.p_fit[i]=aim
                    self.pbest[i]=self.x[i]
                    if self.p_fit[i]<self.fit: # 如果是个体最优再将和全体最优进行对比
                        self.gbest=self.x[i]
                        self.fit = self.p_fit[i]
            for i in range(self.N): # 更新粒子的速度和位置
                print(self.x[i])
                self.v[i]=self.w*self.v[i]+self.c1*self.r1*(self.pbest[i]-self.x[i])+ self.c2*self.r2*(self.gbest-self.x[i])
                self.x[i]=self.x[i]+self.v[i]
                
        print("最优值：",self.fit,"位置为：",self.gbest)


if __name__ == '__main__':
    # w,c1,c2,r1,r2,N,D,M参数初始化
    upper_bound, lower_bound = 5, -4
    w=random.random()
    c1=c2=2#一般设置为2
    r1=0.7
    r2=0.5
    N=30
    D=1
    M=200
    pso_object=PSO(w, lower_bound, upper_bound, c1,c2,r1,r2,N,D,M)#设置初始权值
    pso_object.init_pop()
    pso_object.update()
