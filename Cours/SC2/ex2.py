# main

k = [1, 3, 8, 41, 66, 87, 11, 8, 9, 1113]

def moyenne(listInput):
    r = 0
    for i in listInput:
        r+= i
    r/= len(listInput)
    return r

print(moyenne(k))

def moyenneTotale(cc1, cc2, ef):
    r = 0
    l = [cc1, cc2, ef]
    for i in l:
        r+= i
    r/= len(l)
    return r

def admission(mg):
    if mg >= 10:
        return 'L\'étudiant est admis'
    else:
        return 'L\'étudiant est non-admis'

def mention(mg):
    if mg >= 10 and mg < 12:
        return 'sans mention.'
    elif mg >= 12 and mg < 14:
        return 'avec mention AB.'
    elif mg >= 14 and mg < 16:
        return 'avec mention B.'
    elif mg >= 16: 
        return 'avec mention TB.'
    else:
        return ''

from ex2 import *