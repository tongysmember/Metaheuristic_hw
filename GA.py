import numpy as np
import random
from math import ceil, log, pow, pi, sin

class GeneticAlogorithm:
    '''
    Ref:https://codeantenna.com/a/Oz1GSmNXKX
    '''
    #约束变量
    a1, b1, a2, b2=3.0,12.1,4.1,5.8
    #存储相关值
    precison=10000
    output=[0.0,0.0,0.0]

    def init(self,M,T,Pc,Pm):
        self.M,self.T,self.Pc,self.Pm=M,T,Pc,Pm
        #码位，二进制编码长度
        self.xLen=int(ceil(log((self.b1-self.a1)*self.precison,2)))
        self.yLen=int(ceil(log((self.b2-self.a2)*self.precison,2)))
        self.Len=self.xLen+self.yLen
        #存储种群基因
        self.population=np.random.rand(self.M, self.Len)
        self.value=np.zeros(self.M)

    def decodegroup(self):
        x=y=0.0
        tmp_value=[]
        for i in range(self.M):
            tmp=0.0
            for j in range(0, self.xLen):
                tmp=tmp+self.population[i][j] * pow(2, j) 
            x = tmp * (self.b1- self.a1) / (pow(2, self.xLen) - 1) + self.a1 
            #
            tmp=0.0
            for j in range(self.xLen, self.Len):
                tmp=tmp+self.population[i][j] * pow(2, j-self.xLen) 
            y = tmp * (self.b2- self.a2) / (pow(2, self.yLen) - 1) + self.a2
            cal_value=21.5 + x * sin(4 * pi * x ) + y * sin(20 * pi * y)
            tmp_value.append(cal_value)
            if cal_value > self.output[2]:
                self.output=[x, y, cal_value]
            ###
            self.value=np.array(tmp_value)

    def makecopy(self):
        #计算所有的值的和
        value_sum = np.sum(self.value)
        #计算适应度
        self.value = np.add.accumlate(self.value)
        value_pi = self.value / value_sum
        value_pi = np.add.acculate(value_pi)
        #轮盘赌法
        choice=np.zeros(self.M)
        for i in range(self.M):
            for j in range(self.M):
                if random.random()  < value_pi[j]:
                    choice[i]=j
                    break
        self.population=self.population[choice]

    def doswitch(self):
        '''
        单点交叉算子 交叉概率 Pc'''
        tmp = np.random.permutation(self.M)
        self.population[tmp]
        for i in range(0, self.M, 2):
            index=int(random.randint(1,self.M-1) * self.Pc)
            self.population[i][-index:],self.population[i+1][-index:]=self.population[i+1][-index:],self.population[i][-index:]


    def domutation(self):
        '''
        平均每代会有cnt个基因发生突变'''
        count=int(ceil(self.Pm * self.M * self.Len))
        for i in range(count):
            index=random.randint(0, self.M * self.Len-1)#[a,b]
            m,n=index/self.Len, index%self.Len
            self.population[m][n]= 1 if self.population[m][n]==1 else 0

    def run(self):
        self.init(1000, 1700, 0.1345, 0.0001234)
        self.decodegroup()
        for i in range(self.T):
            self.makecopy
            self.doswitch()
            self.domutation()
            self.decodegroup()
        print(self.output)

if __name__=='__main__':
    hao=GeneticAlogorithm()
    hao.run()