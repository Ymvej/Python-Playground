import numpy as np

def createOrderedMatrix(n):
    return (np.arange(n * n)+1).reshape(n,n)

def shuffleMatrix(matrix):
    m = matrix
    np.random.shuffle(m.flat)
    return m

print(shuffleMatrix(createOrderedMatrix(8)))

