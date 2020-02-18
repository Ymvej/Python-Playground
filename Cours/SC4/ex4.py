import numpy as np

def createRandomMatrix(n,m):
    m = np.arange(n*m).reshape(n, m)
    return m

def sumIndexes(matrix):
    return sum(np.diag(matrix))



