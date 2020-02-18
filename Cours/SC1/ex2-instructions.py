moyenne = 8.3
admis = False

if moyenne >= 10:
    admis = True

if admis == True and moyenne < 12:
    print("Vous êtes admis sans mention.")
elif admis == True and moyenne >= 12 and moyenne < 14:
    print("Vous êtes admis avec mention Assez Bien.")
elif admis == True and moyenne >= 14 and moyenne < 16:
    print("Vous êtes admis avec mention Bien.")
elif admis == True and moyenne >= 16:
    print("Vous êtes admis avec mention Très Bien.")
else:
    print("Vous êtes non admis.")
