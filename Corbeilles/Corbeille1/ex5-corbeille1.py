userinput = input("Entrez les nombres de votre liste séparés par un espace : \n")
list1 = userinput.split() # convertit l'input en liste
list2=[]
count3=0
counteven=0
produit=1

print("Liste en colonne : ")
for element in list1: # boucle pour convertir les strings de la liste en ints
    list2.append((int)(element))
for e in list2: # boucle pour afficher la liste en colonne
    print(e)
print("Liste inversée : ")
list2.reverse() # inversion de la liste
print(list2) # affichage de la liste inversée
list2.reverse() # inversion de la liste

for i in list2:
    if (i/3) % 1 == 0:
        count3 = count3 + 1
    else:
        pass

print("Nombre de multiples de 3 : " + str(count3))

for i in list2:
    if i % 2 == 0:
        counteven = counteven + i
    else:
        pass

print("Somme des valeurs paires : " + str(counteven))
print("Min : " + str(min(list2)))
print("Max : " + str(max(list2)))

for i in list2:
    produit = produit * i

print("Produit : " + str(produit))