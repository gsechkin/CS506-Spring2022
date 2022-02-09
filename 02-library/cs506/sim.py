import numpy as np
from scipy.spatial import distance

def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res


def jaccard_dist(x, y):
    x = set(x)
    y = set(y)
    nominator = x.intersection(y)
    denominator = x.union(y)
    if len(denominator) == 0:
        similarity = 1
    else:
        similarity = len(nominator) / len(denominator)
    return (1-similarity)

def cosine_sim(x, y):
    res = 0
    res = distance.cosine(x, y, w=None)
    return (1-res)
# Feel free to add more
