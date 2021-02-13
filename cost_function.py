import numpy as np
from hypothises import hypothises

def cost_function(x, y, theta):
    m = len(y)
    h = hypothises(x, theta)
    hy = h - y
    hy = np.square(hy)
    cost = 1/(2*m) * np.sum(hy)
    return cost