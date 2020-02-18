dico = {'John':[1, 34, 1.76, 148], 'Jack':[1, 25, 1.90, 82], 'Emma':[2, 18, 1.32, 95], 'Julie':[2, 21, 1.72, 32], 'Liam':[1, 89, 1.65, 88], 'Olivia':[2, 104, 1.56, 120], 'Noura':[2,30,1.76,105]}


def ageSeek(source, name):
    if name in source:
        i = dico[name]
        return i[1]
    else:
        return 0

# print(ageSeek(dico, 'John'))

def womenCount(source):
    c = 0
    for i in source:
        t = dico[i]
        if t[0] is 2:
            c += 1
        else:
            continue
    return c


# print(womenCount(dico))


def imc(h, w):
    return round((w / (h * h)), 2)

def imcCount(source):
    c = []
    for i in source:
        t = source[i]
        imctest = imc(t[2], t[3])
        if imctest >= 25:
            c.append(i)
            print(c)
        else:
            continue

def plusOne(source):
    for i in source:
        t = source[i]
        t[1] += 1

