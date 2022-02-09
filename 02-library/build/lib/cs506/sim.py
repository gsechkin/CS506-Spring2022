import numpy as np
from scipy import pdist
def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res
    # raise NotImplementedError()

def jaccard_dist(x, y):
    matv = np.array([x, y])
    res = dist.pdist(matv, 'jaccard')
    return res
    # raise NotImplementedError()

def cosine_sim(x, y):
    # raise NotImplementedError()
    res = np.dot(x, y) / (np.linalg.norm(x) * (np.linalg.norm(y)))
    return res
# Feel free to add more
