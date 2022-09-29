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
    def Draw_graph(self, func_objective, list_point:list):

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
            ax.scatter(point[0], point[1], func_objective(point[0], point[1])+self.padding, c=255, cmap='viridis', linewidth=0.5);

        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('z')
        ax.set_box_aspect((1, 1, 0.5))
        plt.title('M11015Q03_HW1_Q2_Plot_Surface')
        plt.show()
        


def main():
    graph = Objective_Graph(500,.1)
    graph.Draw_graph(Objective.func_objective_q2,[[1,1],[100,100],[500,500]])

if __name__ == '__main__':
    main()
    
