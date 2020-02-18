import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as img 
import pandas as pd

# #ex1
tuttut = pd.read_table('/home/samuel/Projects/Cours/Corbeille6-Pandas/Automobile_data.csv', sep=',',header=0)
# # print(tuttut.head())


# #ex2

# print(tuttut.iloc[tuttut['price'].idxmax()])
 

# #ex3 

# print(tuttut.loc[tuttut['company'] == 'toyota'])


# #ex4

plt.show(tuttut.groupby('company').count()[['index']].hist())


# #ex5

# plt.show(tuttut.groupby(['company'])['price'].max().plot.bar())


# #ex6

# plt.show(tuttut.groupby(['company'])['average-mileage'].mean().plot.bar())    

# #ex7

print(tuttut.sort_values(by=['price']))