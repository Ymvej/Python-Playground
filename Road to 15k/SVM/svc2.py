# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import math
import time
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


# %%
# import base et nettoyage
data = pd.read_csv('/home/samuel/Workspace/Playgrounds/Python-Playground/Road to 15k/credit.csv')

strtocat = ['Historique_credit',
            'Objet_credit',
            'Situation_familiale',
            'Garanties', 
            'Biens',
            'Autres_credits',
            'Statut_domicile',
            'Type_emploi',
            'Telephone']

def str_to_cat(column):
    uniques = column.unique()
    scale = {}
    for i in range(len(uniques)):
        scale[uniques[i]] = i  

    new_column = column.apply(lambda x: scale[x])
    return new_column

data.drop('Unnamed: 0', axis = 1, inplace=True)

for i in range(len(strtocat)):
    data[strtocat[i]] = str_to_cat(data[strtocat[i]])


# %%
# split
X = data.drop('Cible', axis=1)
y = data['Cible']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# %%
# svc
KERNELS = ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed']

maxacc = 0.0
start = time.time()

for k in range(len(KERNELS)):
    print('Starting kernel %s'%KERNELS[k])
    reg = 1.0
    for c in range(100):
        print('Regularization parameter at %s'%reg)
        svm = SVC(C=reg, kernel=KERNELS[k], gamma='auto').fit(X_train, y_train)
        y_pred = svm.predict(X_test)
        reg += 0.01
        
        acc = accuracy_score(y_test, y_pred)
        if acc > maxacc:
            maxacc = acc
            conmat = confusion_matrix(y_test, y_pred)
            print('New best accuracy at %s with trees %s branches deep.'%(acc, i+1))
        else:
            pass
    curr = time.time()
    timedd = round(curr - start, 2)
    print('Finished kernel %s in %s'%(KERNELS[k], timedd))

end = time.time()
timed = round(end - start, 2)
print('Model finished in %ss'%timed)
print('Best Accuracy : %s'%acc)
print('Best Confusion Matrix :')
print(conmat)

