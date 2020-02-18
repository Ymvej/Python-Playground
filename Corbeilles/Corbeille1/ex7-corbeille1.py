distance = 0.05
masseA = 10000
masseB = 10000
G = 6.67 * 10 ** -11
resultat = 0
iterations = 15
count = 0

while count < iterations:
    resultat = (G * masseA * masseB) / (distance * distance)
    print("La force d'attraction gravitationnelle entre les deux corps vaut : "  ,resultat, "m/s²")
    distance = distance * 2
    count = count + 1
