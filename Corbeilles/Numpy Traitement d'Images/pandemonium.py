#test.jpg

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import os

coolbird = plt.imread('test.jpg')

def viewport(func):
    plt.imshow(func)
    plt.show()

def invertImg(source):
    reverseBird = np.copy(source)
    for i in range(reverseBird.shape[0]):
        for j in range(reverseBird.shape[1]):
            r, g, b = reverseBird[i, j]
            reverseBird[i, j] = (255 - r, 255 - g, 255 - b)
    return reverseBird

def triSplitter(source):
    cwd = os.getcwd()
    
    currentcolor = 'Red'
    def exporter(output):
            writepath = cwd + '/' + currentcolor + '.jpg'
            with open(writepath, 'a') as f:
                f.write(currentcolor + '.jpg')
    
    tripleBird = np.copy(source)
    currentcolor = 'Red'
    for i in range(tripleBird.shape[0]):
        for j in range(tripleBird.shape[1]):
            r, g, b = tripleBird[i, j]
            tripleBird[i, j] = (r, 0, 0)
    exporter(tripleBird)
    
    tripleBird = np.copy(source)
    currentcolor = 'Green'
    for i in range(tripleBird.shape[0]):
        for j in range(tripleBird.shape[1]):
            r, g, b = tripleBird[i, j]
            tripleBird[i, j] = (0, g, 0)
    exporter(tripleBird)
    
    tripleBird = np.copy(source)
    currentcolor = 'Blue'
    for i in range(tripleBird.shape[0]):
        for j in range(tripleBird.shape[1]):
            r, g, b = tripleBird[i, j]
            tripleBird[i, j] = (0, 0, b)
    exporter(tripleBird)


    



    
triSplitter(coolbird)