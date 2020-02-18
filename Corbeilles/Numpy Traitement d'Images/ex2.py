import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as img
def createImg(name, h, w):
    matrix = np.zeros((h, w, 3))
    # matrix2 = np.triu(matrix, k=1)
    # matrix2[matrix2 == 0] = 1
    plt.imshow(matrix)
    plt.show()
    return matrix
    
createImg('caca', 2160, 3840)
