def tableMult(base, start, stop):
    n = stop
    k = base
    l = start # on initialise les arguments de la fonction

    while l<n: # tant que le compteur l (initialisé au nombre de départ) n'a pas atteint la valeur du compteur n (initialisé au nombre cible)
        print(l ,'x', k, '=', l*k) # on fait les trucs et on les affiche
        l+=1 # sans oublier d'incrementer le compteur l

tableMult(89,1,156) # et on appelle la fonction
