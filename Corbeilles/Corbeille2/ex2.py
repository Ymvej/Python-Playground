long1 = 1.6
long2 = 5.4
long3 = 8.7

def pythagore (l1, l2, l3):

    l1 = l1 * l1
    l2 = l2 * l2
    l3 = l3 * l3

    hypo = max(l1, l2, l3)
    sides = (l1 + l2 + l3) - hypo

    if sides == hypo:
        return 'rectangle.'
    else:
        return 'non-rectangle.'


print(pythagore(long1, long2, long3))