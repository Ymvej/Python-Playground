import numpy as np
import ex4

source = ex4.createRandomMatrix(8,16)

def transposeMatrix(matrix):
    return np.transpose(matrix)

print(transposeMatrix(source))