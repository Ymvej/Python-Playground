import numpy as np

def createMatrixDiag(n):

    k = np.ones(n)
    m = np.diag(k, 1)
    m[0] = 1
    m[-1] = 1
    return m

print(createMatrixDiag(5))