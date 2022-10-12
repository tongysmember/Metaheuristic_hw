import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
from Objective import Objective

class Objective_Graph(object):
    '''
    Draw Objective Function Graph
    '''
    def __init__(self, width, step):
        '''
        width : Setting witdh Upper and lower bound
        step : Upper and lower bound step
        '''
        self.width = width
        self.step = step
        self.padding = 200
    
    def Draw_graph_3D_Question(self, func_objective):
        # Draw 3D axis plot
        x = np.arange(-self.width, self.width, self.step)
        y = np.arange(-self.width, self.width, self.step)
        X, Y = np.meshgrid(x, y) 
        Z = func_objective(X)
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')
        ax.set_box_aspect((1, 1, 0.5))
        plt.title('M11015Q03_HW1_Q2_Plot_Surface')
        plt.show()

    def Draw_graph_3D(self, func_objective, list_point:list):

        # Draw 3D axis plot
        x = np.arange(-self.width, self.width, self.step)
        y = np.arange(-self.width, self.width, self.step)
        X, Y = np.meshgrid(x, y) 
        Z = func_objective(X, Y)
        ax = plt.axes(projection='3d')
        ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)


        # Calcute Z value in plot
        list_point_z_value = list()
        for point in list_point:

            #min_x1, min_x2 = 0,0
            #min_z = func_objective(min_x1, min_x2)
            #list_point_z_value.append([point[0], point[1], func_objective(point[0], point[1])])

            # Draw Point 
            ax.scatter(point[0], point[1], func_objective(point[0], point[1])+self.padding, c=100, cmap='viridis', linewidth=0.5);

        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')
        ax.set_box_aspect((1, 1, 0.5))
        plt.title('M11015Q03_HW1_Q2_Plot_Surface')
        plt.show()
    
    def Draw_graph_2D(self, func_objective, list_point:list):
        print('2D')
        fig = plt.figure(figsize = (10, 5))
        iter, list_iter, list_fitness = 0, list(), list()
        for data in list_point:
            list_iter.append(iter)
            list_fitness.append(func_objective(data[0], data[1]))
            iter+=1
        plt.plot(list_iter, list_fitness)
        plt.title("Convergence Curve")
        plt.xlabel('Iteration No.')
        plt.ylabel('r. Fitness')
        plt.show()


    def Draw_graph_2D_Question(self,lower_bound, upper_bound, func_objective, list_point:list):
        x = np.linspace ( start = lower_bound    
                        , stop = upper_bound     
                        , num = (upper_bound-lower_bound)      
                        )
        y = func_objective(x)    # This is already vectorized, that is, y will be a vector!
        plt.plot(x, y)
        plt.show()


def main():
    #graph = Objective_Graph(500,.1)
    #graph.Draw_graph(Objective.func_objective_q2,[[1,1],[100,100],[500,500]])
    #graph.Draw_graph_2D(Objective.func_objective_q2,[[1,1],[100,100],[500,500]])

    graph = Objective_Graph(500,.1)
    graph.Draw_graph_2D_Question(Objective.func_objective_hw2_q2, [])

if __name__ == '__main__':
    main()
    
