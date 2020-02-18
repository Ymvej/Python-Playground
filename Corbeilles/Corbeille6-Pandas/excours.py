import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as img 
import pandas as pd

heart = pd.read_table('/home/samuel/Projects/Cours/Corbeille6-Pandas/heart.txt', sep='\t',header=0)

# print(heart.head(10))
# print(heart.tail(10))
# print(heart.columns)
# print(heart.dtypes)
# print(heart.describe())



plt.show(heart.plot.scatter(x= 'age', y= 'pression'))