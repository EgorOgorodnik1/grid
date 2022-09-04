import math
import matplotlib
import numpy as np
from prettytable import PrettyTable
import matplotlib.pyplot as plt

x = []
y = [[],[],[]]
step = [101, 201, 401]
h = np.around([5*math.pi/200, 5*math.pi/400, 5*math.pi/800], 4)
for l in range (3):
    x_help = np.around(list(np.linspace(0, 5*math.pi/2, step[l])), 4)
    p = []
    for i in range(1,len(x_help)-1):
        p.append(np.around(2/(x_help[i]+1), 3))
    q = []
    for i in range(1,len(x_help)-1):
        q.append(1)
    b = np.zeros((len(x_help),1))
    for i in range(len(x_help)):
        for j in range(1):
            if i==0:
                b[i,j]=1
            else:
                b[i,j]=0
    y_help = np.zeros((len(x_help),len(x_help)))
    counter = 0
    for i in range(len(x_help)):
        for j in range(len(x_help)):
            if i==j==0 or i==j==len(x_help)-1:
                y_help[i,j] = 1
            elif i==j!=0 and i==j!=len(x_help)-1:
                y_help[i,j] = np.around(-(2-q[counter]*h[l]**2), 4)
                y_help[i,j-1] = np.around(1 - (h[l]/2)*p[counter], 4)
                y_help[i,j+1] = np.around(1 + (h[l]/2)*p[counter], 4)
                counter = counter + 1
            elif i - j != 1 and i - j != -1:
                y_help[i,j] = 0

    y_solution = np.around(np.linalg.solve(y_help, b), 4)
  
    counter_1 = 0
    counter_2 = 0
    if l == 0:
        y[l] = y_solution
        x = x_help
    elif l == 1:
        for i in range(0,len(y_solution),2):
            y[l].insert(counter_1, y_solution[i])
            counter_1 = counter_1 + 1
    else:
        for i in range(0,len(y_solution),4):
            y[l].insert(counter_2, y_solution[i])
            counter_2 = counter_2 + 1

table = PrettyTable()
table.field_names = ['x\u1d62', '''y\u1d62 
\t(N=100)''', 'y\u1d62 (N=200)', 'y\u1d62 (N=400)']
for i in range(len(x)):
    table.add_row([x[i], y[0][i], y[1][i], y[2][i]])
print(table)

def Draw_Graphics(): 

    plt.subplot()
    plt.xlim([0, 5*math.pi/2])
    plt.ylim([-0.5, 1])
    plt.grid(color='green')
    plt.plot(x, y[0], '--', label='y(x) (N=100)')
    plt.plot(x, y[1], 'r-', label='y(x) (N=200)')
    plt.plot(x, y[2], 'k-.', label='y(x) (N=400)')
    plt.legend(bbox_to_anchor=(0.125, 1.15))
    plt.show()

Draw_Graphics()
