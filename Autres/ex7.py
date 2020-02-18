import random


def grille(x,y): # crée un array de longueur x et de hauteur y
    d = [] # on initialise la liste d, qui represente la longueur
    e = [] # on initialise la liste e, qui represente la hauteur
    for i in range(0,y): # on boucle sur la longueur désirée
        d.append(0) # on ajoute 0 à la fin de la liste d, autant de fois qu'on boucle, donc autant de fois que la valeur de y
    for i in range(0,x): # on boucle sur la hauteur desirée
        e.append(d) # on ajoute à la liste e les listes de longueur y, et ça x fois
    return e # on retourne e, qui est un array sous la forme [[0,0,0,0][0,0,0,0][0,0,0,0]]

def alea(x,y): # crée un array de longueur x et de hauteur y au contenu aléatoire
    d = [] # on initialise la longueur
    e = [] # on initialise la hauteur

    for i in range(0,x): # on boucle sur la hauteur
        for i in range (0,y): # on boucle sur la longueur
            d.append(random.randrange(0,10)) # on ajoute un nombre aleatoire entre 0 et 9, autant de fois qu'on boucle, i.e. autant de fois que y.
        e.append(d) # on ajoute la liste de y nombres qu'on vient de créer à e
        d = [] # on réinitialise d, tout ça repeté x fois.
    return e # on retourne e

def doubleloopsum(array): # fonction qui somme un array avec une double boucle
    z = 0 # on initialise notre resultat
    for i in array: # on boucle sur la longueur de l'array, i.e. le nombre de lignes, i.e x dans alea(x,y)
        for k in i: # dans la boucle sur la longueur, on boucle sur chaque liste indiviudellement
            z = z + k # on ajoute à notre resultat la valeur de chaque élement de la liste
    return z # on retourne le total, bouclé array.len() fois.

def loopsum(array): # fonction quisomme un array avec une boucle simple
    z = 0 # on initialise notre résultat
    for i in array: # on boucle sur la longueur de l'array, i.e. le nombre de lignes, i.e. x dans alea(x,y)
        z = z + sum(i) # on ajoute à notre résultat la valeur de la somme de chaque ligne de l'array
    return z # on retourne le résultat, bouclé array.len() fois


loopsum(alea(3,4))