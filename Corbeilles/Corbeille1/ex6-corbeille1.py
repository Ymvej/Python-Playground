nom = input("Quel est votre nom ? \n")
genre = input("Êtes vous un Homme, une Femme, ou Autre ? \n")

if genre == "Homme" or genre == "H" or genre == "h" or genre == "Un Homme" or genre == "un homme":
    print("Cher Monsieur " + nom)
elif genre == "Femme" or genre == "F" or genre == "f" or genre == "Une Femme" or genre == "une femme":
    print("Chère Madame " + nom)
else:
    print("Vénérable " + genre + " " + nom)

