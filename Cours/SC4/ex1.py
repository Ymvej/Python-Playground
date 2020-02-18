import numpy as np


def createMatrix(n):
    n += 1
    r = np.zeros((2*n, 2*n))
    r[n-1] = np.ones(2*n)
    r[:, n-1] = np.ones(2*n)
    return r

print(createMatrix(4))

