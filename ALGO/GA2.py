# coding=utf-8
# @Author: GongDeFeng
# Ref : https://blog.csdn.net/GDF0221/article/details/116005951?spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-13-116005951-blog-112997314.t5_download_0_7w&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-13-116005951-blog-112997314.t5_download_0_7w&utm_relevant_index=14
import random
import numpy as np
import matplotlib.pyplot as plt

population_size = 50                        # 种群初始规模
generation_count = 50                       # 遗传代数
gene_length = 23                            # 染色体长度
exchange_ratio = 0.8                        # 交叉概率
variation_ratio = 0.01                      # 变异概率
#solve_max = True                            # 为True则求解最大值，为False则求解最小值
solve_max = False                            # 为True则求解最大值，为False则求解最小值
function = lambda x: x * np.sin(x) + 1      # 需要求解的数学函数
x_min = 0                                   # 基因的最小值，即变量x能取到的最小值
x_max = 2 * np.pi                           # 基因的最大值，即变量x能取到的最大值

#plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 支持负号显示


def get_chromosome(size, length):
    """
    生成size个长度为length的染色体列表
    :param size: 种群规模规模
    :param length: 染色体长度
    :return: 二维列表
    """
    population_temp = []
    for i in range(size):
        population_temp.append([random.randint(0, 1) for _ in range(length)])   # 生成长度为length的随机二进制列表，并存放到population_temp列表中
    return population_temp


def get_accuracy(min_, max_, length):
    """
    计算搜索精度
    :param min_: 基因的最小值
    :param max_: 基因的最大值
    :param length: 染色体长度
    :return: 精度
    """
    return (max_ - min_) / (2 ** length - 1)    # 精度计算公式


def chromosome_decode(chromosome_list, min_, accuracy_):
    """
    染色体解码
    :param chromosome_list: 二进制染色体列表
    :param min_: 基因的最小值
    :param accuracy_: 精度
    :return: 解码的结果
    """
    decimal = int(''.join([str(i) for i in chromosome_list]), 2)    # 二进制列表转为十进制整型
    return min_ + accuracy_ * decimal   # 解码公式


def get_fitness(x, solve_flag):
    """
    计算适应度
    :param x: 染色体解码的结果
    :param solve_flag: 求最大值则为True，最小值则为False
    :return: 适应度结果
    """
    if solve_flag:
        return function(x)
    return -(function(x))


def select(chromosome_list, fitness_list):
    """
    选择(轮盘赌算法)
    :param chromosome_list: 二维列表的种群
    :param fitness_list: 适应度列表
    :return: 选择之后的种群列表
    """
    population_fitness = np.array(fitness_list).sum()  # 种群适应度
    fit_ratio = [i / population_fitness for i in fitness_list]  # 每个个体占种群适应度的比例
    fit_ratio_add = [0]  # 个体累计概率
    for i in fit_ratio:
        fit_ratio_add.append(fit_ratio_add[len(fit_ratio_add) - 1] + i)     # 计算每个个体的累计概率，并存放到fit_ratio_add中
    fit_ratio_add = fit_ratio_add[1:]   # 去掉首位的0

    rand_list = [random.uniform(0, 1) for _ in chromosome_list]     # 生成和种群规模相等的随机值列表，用于轮盘赌选择个体
    rand_list.sort()
    fit_index = 0
    new_index = 0
    new_population = chromosome_list.copy()
    '''个体选择 start'''
    while new_index < len(chromosome_list):
        if rand_list[new_index] < fit_ratio_add[fit_index]:
            new_population[new_index] = chromosome_list[fit_index]
            new_index = new_index + 1
        else:
            fit_index = fit_index + 1
    '''个体选择 end'''
    return new_population


def exchange(chromosome_list, pc):
    """
    交叉
    :param chromosome_list: 二维列表的种群
    :param pc: 交叉概率
    """
    for i in range(0, len(chromosome_list) - 1, 2):
        if random.uniform(0, 1) < pc:
            c_point = random.randint(0, len(chromosome_list[0]))    # 随机生成交叉点
            '''对第i位和i+1位进行交叉 start'''
            exchanged_list1 = []
            exchanged_list2 = []
            exchanged_list1.extend(chromosome_list[i][0:c_point])
            exchanged_list1.extend(chromosome_list[i + 1][c_point:len(chromosome_list[i])])
            exchanged_list2.extend(chromosome_list[i + 1][0:c_point])
            exchanged_list2.extend(chromosome_list[i][c_point:len(chromosome_list[i])])
            '''对第i位和i+1位进行交叉 end'''

            '''将新交叉后的染色体替换原染色体 start'''
            chromosome_list[i] = exchanged_list1
            chromosome_list[i + 1] = exchanged_list2
            '''将新交叉后的染色体替换原染色体 end'''


def mutation(chromosome_list, pm):
    """
    变异
    :param chromosome_list: 二维列表的种群
    :param pm: 变异概率
    """
    for i in range(len(chromosome_list)):
        if random.uniform(0, 1) < pm:
            m_point = random.randint(0, len(chromosome_list[0]) - 1)    # 随机生成变异点
            chromosome_list[i][m_point] = chromosome_list[i][m_point] ^ 1   # 将该位的值与1异或(即将0置为1,1置为0)


def get_best(fitness_list):
    """
    计算这一代中的最优个体
    :param fitness_list: 适应度列表
    :return: 最优个体的下标
    """
    return fitness_list.index(max(fitness_list))


def eliminate(fitness_list):
    """
    淘汰(去掉负值)
    :param fitness_list: 适应度列表
    :return: 淘汰后的列表
    """
    fit_value = []
    for i in range(len(fitness_list)):
        fit_value.append(fitness_list[i] if fitness_list[i] >= 0 else 0.0)   # 将小于0的适应度置为0
    return fit_value


if __name__ == '__main__':
    results = []  # 存储每一代的最优解，二维列表
    all_fitness = []    # 存放每一代中的最高适应度和种群适应度
    population = get_chromosome(population_size, gene_length)   # 种群初始化
    for _ in range(generation_count):
        accuracy = get_accuracy(x_min, x_max, gene_length)  # 计算搜索精度
        decode_list = [chromosome_decode(individual, x_min, accuracy) for individual in population]  # 解码之后的列表
        fit_list = [get_fitness(decode_i, solve_max) for decode_i in decode_list]  # 计算每个个体的适应度
        fit_list = eliminate(fit_list)  # 淘汰一部分，去掉负值
        results.append([decode_list[get_best(fit_list)],
                        fit_list[get_best(fit_list)] if solve_max else -fit_list[get_best(fit_list)]])  # 保存每一代最优解，即适应度最高的个体
        all_fitness.append(np.array(fit_list).sum() if solve_max else -np.array(fit_list).sum())    # 保存每一代中的最高适应度和种群适应度
        population = select(population.copy(), fit_list)
        exchange(population, exchange_ratio)
        mutation(population, variation_ratio)

    if solve_max:
        results.sort(key=lambda x: x[1])
    else:
        results.sort(key=lambda x: x[1], reverse=True)
    print('最{}值点 x={},y={}'.format('大' if solve_max else '小', results[-1][0], results[-1][1]))

    '''绘制极值趋势图和种群适应度趋势图 start'''
    X = [generation_i for generation_i in range(generation_count)]
    Y1 = [results[generation_i][1] for generation_i in range(generation_count)]
    Y2 = [all_fitness[generation_i] for generation_i in range(generation_count)]

    fig1 = plt.figure('figure', figsize=(13, 5)).add_subplot(121)
    fig1.plot(X, Y1)
    fig2 = plt.figure('figure', figsize=(13, 5)).add_subplot(122)
    fig2.plot(X, Y2)

    fig1.set_title('極值曲線圖')
    fig1.set_xlabel("遗传代数")
    fig1.set_ylabel("极值")
    fig2.set_title('族群適應度趨勢圖')
    fig2.set_xlabel("遗传代数")
    fig2.set_ylabel("种群适应度")

    plt.show()
    '''绘制极值趋势图和种群适应度趋势图 end'''

