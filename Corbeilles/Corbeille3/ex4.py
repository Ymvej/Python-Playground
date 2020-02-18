d = {'1':322,'2':548,'3':874,'4':412,'5':874,'6':784,'7':879,'8':12,'9':78}

def average(source):
    t = 0
    l = 0
    for i in source:
        v = source[i]
        t = t + v
        l += 1
    return round(t / l, 2)

def validate(source):
    c = []
    for i in source:
        v = source[i]
        if v >= 200:
            c.append(v)
        else:
            continue
    return c

def maxDict(source):
    c = []
    m = []
    for k,v in source.items():
        m.append(v)
    c.append(max(m))
    return c

def transvalidate(source):
    c = []
    for i in source:
        v = source[i]
        if v >= 200:
            v = 'valid'
        else:
            continue
    return c

def addpoints(score,id,source):


    if not id in source:
        source.update([(id, score)])
    elif source[id] == 'valid':
        pass
    else:
        source.update([(id, source[id] + score)])

    for i in source:
        if source[i] >= 200:
            source[i] = 'valid'
        else:
            continue





addpoints(241,8,d)
print(d)