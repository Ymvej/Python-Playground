while True:
    try:
        userinput = input("Année à tester : \n")
        userinput = int(userinput)
        userinput = max(0, userinput)
        
        if userinput == 0:
            print("Veuillez entrer une année positive.")
        elif (userinput/400) % 1 == 0 or userinput % 4 == 0:
            print("L'année est bissextile.")
        else:
            print("L'année n'est pas bissextile.")
        
    except (ValueError, TypeError):
        print("Veuillez entrer une année valide.")