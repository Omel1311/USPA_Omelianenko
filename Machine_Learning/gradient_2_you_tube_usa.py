import numpy as np
import matplotlib.pyplot as plt


def y_function(x):
    return x**2


#    функция для опередлеения градиента (скорости измененения наклона)
def y_derevative(x):
    return x*2


x = np.arange(-100, 100, 0.1)
y = y_function(x)

current_position = (90, y_function(90))

learning_rate = 0.01

for _ in range(1000):
    new_x = current_position[0] - learning_rate*y_derevative(current_position[0])
    new_y = y_function(new_x)
    current_position = (new_x, new_y)


    plt.scatter(current_position[0], current_position[1], c='r')
    plt.plot(x,y)
    plt.pause(0.001)
    plt.clf()



