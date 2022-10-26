
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from FUNC.Objective import Objective
## Ref: https://aistudio.csdn.net/62e38a8ecd38997446774d1d.html



class GA(object):
    '''
    Genetic Algorithm
    '''
    def __init__(self,lower_bound,  upper_bound, N_GENERATIONS, func_objective, dim:int=10):
        self.DNA_SIZE = 10
        self.POP_SIZE = 10
        self.CROSSOVER_RATE = 0.7
        self.MUTATION_RATE = 0.05
        self.N_GENERATIONS = N_GENERATIONS
        self.X_BOUND = [lower_bound, upper_bound]
        self.Y_BOUND = [lower_bound, upper_bound]
        self.dim = dim
        self.F = func_objective
        self.list_point = list()
        self.best_fitness = sys.maxsize
        self.fitness_last = sys.maxsize
        self.precision_level = 1e-6
    def get_fitness(self, pop): 
        '''
        二進制轉換十進制, 並產生 Fitness 數值
        '''
        x = self.translateDNA(pop)
        return self.F(x,self.dim)
    
    
    def translateDNA(self, pop): 
        '''
        透過二進制編碼轉換數值, 產生 x1, x2, 上下界數值資料
        '''
        x_pop = pop[:,1::2]
        #y_pop = pop[:,::2] 
        x = x_pop.dot(2**np.arange(self.DNA_SIZE)[::-1])/float(2**self.DNA_SIZE-1)*(self.X_BOUND[1]-self.X_BOUND[0])+self.X_BOUND[0]
        return x
    
    def crossover_and_mutation(self, pop, CROSSOVER_RATE = 0.8):
        '''
        將二進制轉換進行交配率運作, 父母代產生子代, 並有一定機率產生突變
        '''
        new_pop = []
        for father in pop:		
            child = father		
            if np.random.rand() < CROSSOVER_RATE:	
                mother = pop[np.random.randint(self.POP_SIZE)]	
                cross_points = np.random.randint(low=0, high=self.DNA_SIZE*2)	
                child[cross_points:] = mother[cross_points:]		
            self.mutation(child)
            new_pop.append(child)
        return new_pop
    
    def mutation(self, child, MUTATION_RATE=0.003):
        '''
        透過隨機產生突變位置, 並以二進制反轉
        '''
        if np.random.rand() < MUTATION_RATE: 
            mutate_point = np.random.randint(0, self.DNA_SIZE*2)
            child[mutate_point] = child[mutate_point]^1
    
    def select(self, pop, fitness):   
        '''
        隨機選擇子代, 機率為 Fitness 越小越容易選擇到 , 參考引數 p
        '''
        idx = np.random.choice(np.arange(self.POP_SIZE), size=self.POP_SIZE, replace=True, p= (1/fitness)/((1/fitness).sum()))
        return pop[idx]
    
    def print_info(self, pop):
        '''
        顯示 Fitness 資訊, 並有比較與原先 Fitness 是否有進步
        '''
        fitness = self.get_fitness(pop)
        min_fitness_index = np.argmin(fitness)
        print("min_fitness:", fitness[min_fitness_index])
        x= self.translateDNA(pop)
        print("(x):", (x[min_fitness_index]))
        if min(fitness) < self.best_fitness:
            self.best_fitness = min(fitness)
            self.list_point.append([x[min_fitness_index]])
    
    def proceed(self):
        '''
        演算法運算邏輯
        1. 產生母體二進制亂數資料
        2. 迭代開始
        3. 交配產生子代
        4. 子代突變
        5. 篩選新物種, Fitness 越小機率越高
        '''
        pop = np.random.randint(2, size=(self.POP_SIZE, self.DNA_SIZE*2)) 
        for _ in range(self.N_GENERATIONS):
            x= self.translateDNA(pop)
            fitness = self.get_fitness(pop)
            self.print_info(pop)
            if abs(self.best_fitness-self.fitness_last) <= self.precision_level and (self.best_fitness <=1e-2):                
                break
            self.fitness_last = self.best_fitness
            pop = self.select(pop, fitness) 
            pop = np.array(self.crossover_and_mutation(pop, self.CROSSOVER_RATE))
            
            

if __name__ == "__main__":
    GA = GA(-500, 500, 5000, Objective.func_objective_q2)
    GA.proceed()