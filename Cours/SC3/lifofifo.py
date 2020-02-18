#lifo
def creerPile():
    global pile
    pile = []
    return pile

def emptyPile(pile):
    if not pile:
        return True
    else:
        return False

def empiler(x, pile):
    pile.append(x)
    return pile

def depiler(pile):
    return pile.pop(-1)

def sommet(pile):
    copie = pile.pop(-1)
    pile.append(copie)
    return copie

def hauteur(pile):
    return len(pile)


# fifo
def creerFile():
    global file
    file = []
    return file

def emptyFile(file):
    if not file():
        return True
    else:
        return False

def enfiler(x,file):
    file.insert(0, x)

def defiler(file):
    return file.pop(-1)

def lenFile(file):
    return len(file)
