import numpy as np
from hypothises import hypothises
from cost_function import cost_function

def gradient_descent(x, y, theta, alpha, iteration):
    m = len(y)
    iter = 0
    while iter < iteration:
        h = hypothises(x, theta)
        hy = h - y
        theta[0][0] = theta[0][0] - alpha/m * sum(hy)
        theta[1][0] = theta[1][0] - alpha/m * np.sum(np.dot(np.transpose(hy), x[:,  1]))
        cost = cost_function(x, y, theta)
        # print(theta[0][0], theta[1][0], cost)

        iter += 1
    return theta