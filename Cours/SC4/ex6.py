import numpy as np
import ex4

def genOut(li, co, n):
    m = ex4.createRandomMatrix(li, co)
    r = np.insert(m,0,n, axis=1)

    for i in range(0, co):
        c = np.insert(m,i+1,n, axis=1)
        r = np.concatenate((r, c))

    return r


print(genOut(3,1,99))