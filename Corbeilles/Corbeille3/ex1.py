dic1   = {'chocolat': 1.25, 'nutella': 2.55, 'miel': 4.52, 'carambar': 2.79}


def combien(dico):
    return len(dico.keys())

def moyenne(dico):
    sumDico = sum(list(dico.values()))
    sumDico /= len(dico.values())
    return sumDico

def moinscher(dico):
    return min(dico, key=dico.get)

def dollars(dico):
    for k, v in dico.items():
        v *= 1.13
        dico[k] = round(v, 2)
    return dico



print(dollars(dic1))