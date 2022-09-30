
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from FUNC.Objective import Objective
## Ref: https://aistudio.csdn.net/62e38a8ecd38997446774d1d.html



class GeneAlgo(object):
    def __init__(self,lower_bound,  upper_bound, N_GENERATIONS, func_objective):
        self.DNA_SIZE = 30
        self.POP_SIZE = 100
        self.CROSSOVER_RATE = 0.7
        self.MUTATION_RATE = 0.05
        self.N_GENERATIONS = N_GENERATIONS
        self.X_BOUND = [lower_bound, upper_bound]
        self.Y_BOUND = [lower_bound, upper_bound]
        self.F = func_objective
        self.list_point = list()
        self.best_fitness = sys.maxsize
    
    def get_fitness(self, pop): 
        x,y = self.translateDNA(pop)
        return self.F(x, y)
    
    
    def translateDNA(self, pop): #pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
        x_pop = pop[:,1::2]#奇数列表示X
        y_pop = pop[:,::2] #偶数列表示y
        
        #pop:(POP_SIZE,DNA_SIZE)*(DNA_SIZE,1) --> (POP_SIZE,1)
        x = x_pop.dot(2**np.arange(self.DNA_SIZE)[::-1])/float(2**self.DNA_SIZE-1)*(self.X_BOUND[1]-self.X_BOUND[0])+self.X_BOUND[0]
        y = y_pop.dot(2**np.arange(self.DNA_SIZE)[::-1])/float(2**self.DNA_SIZE-1)*(self.Y_BOUND[1]-self.Y_BOUND[0])+self.Y_BOUND[0]
        return x,y
    
    def crossover_and_mutation(self, pop, CROSSOVER_RATE = 0.8):
        new_pop = []
        for father in pop:		#遍历种群中的每一个个体，将该个体作为父亲
            child = father		#孩子先得到父亲的全部基因（这里我把一串二进制串的那些0，1称为基因）
            if np.random.rand() < CROSSOVER_RATE:			#产生子代时不是必然发生交叉，而是以一定的概率发生交叉
                mother = pop[np.random.randint(self.POP_SIZE)]	#再种群中选择另一个个体，并将该个体作为母亲
                cross_points = np.random.randint(low=0, high=self.DNA_SIZE*2)	#随机产生交叉的点
                child[cross_points:] = mother[cross_points:]		#孩子得到位于交叉点后的母亲的基因
            self.mutation(child)	#每个后代有一定的机率发生变异
            new_pop.append(child)
        return new_pop
    
    def mutation(self, child, MUTATION_RATE=0.003):
    	if np.random.rand() < MUTATION_RATE: 				#以MUTATION_RATE的概率进行变异
            mutate_point = np.random.randint(0, self.DNA_SIZE*2)#随机产生一个实数，代表要变异基因的位置
            child[mutate_point] = child[mutate_point]^1 	#将变异点的二进制为反转
    
    def select(self, pop, fitness):    # nature selection wrt pop's fitness
        idx = np.random.choice(np.arange(self.POP_SIZE), size=self.POP_SIZE, replace=True, p= (1/fitness)/((1/fitness).sum()))
        return pop[idx]
    
    def print_info(self, pop):
        fitness = self.get_fitness(pop)
        #max_fitness_index = np.argmax(fitness)
        #測試修改最小值
        min_fitness_index = np.argmin(fitness)
        print("min_fitness:", fitness[min_fitness_index])
        x,y = self.translateDNA(pop)
        print("(x, y):", (x[min_fitness_index], y[min_fitness_index]))
        if min(fitness) < self.best_fitness:
            self.best_fitness = min(fitness)
            self.list_point.append([x[min_fitness_index], y[min_fitness_index]])
    
    def proceed(self):
        pop = np.random.randint(2, size=(self.POP_SIZE, self.DNA_SIZE*2)) #matrix (POP_SIZE, DNA_SIZE)
        for _ in range(self.N_GENERATIONS):#迭代N代
            x,y = self.translateDNA(pop)
            pop = np.array(self.crossover_and_mutation(pop, self.CROSSOVER_RATE))
            fitness = self.get_fitness(pop)
            self.print_info(pop)
            pop = self.select(pop, fitness) #选择生成新的种群
        #self.print_info(pop)


if __name__ == "__main__":
    GA = GeneAlgo(-500, 500, 5000, Objective.func_objective_q2)
    GA.proceed()
    #print(GA.list_point)