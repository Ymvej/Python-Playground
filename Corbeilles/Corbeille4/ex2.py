e1={'alg ' : 9.0 , 'python ' : 15 , ' anglais ' : 7 , 'cNum' : 15}
e2={'alg ' : 8 , 'python ' : 12 , ' anglais ' : 12 , 'cNum' : 14 , 'proba ' : 9 , 'SQL ' : 11 , 'maths' : 10 }
e3=e1
e4=e2
l1 = [e1, e2, e3, e4]
coeffs={"alg ":6 ," python ":6 ," anglais ":2 ,"cNum":4 ," proba ":6 ," sql ":4 , "maths":2}

def bestMark(dic):
    best = 0
    res = []
    for k,v in dic.items():
        if v > best:
            best = v
            res.clear()
            res.append(k)
        else:
            pass
    return res

def sumFactors(dic, coeff):
    s = 0
    ck = {}
    dk = {}
    u = ''
    for k, v in coeff.items():
        u = k.strip().lower()
        ck[u]=v
    for k, v in dic.items():
        u = k.strip().lower()
        dk[u]=v
    for k, v in dk.items():
        if k in ck.keys():
            s = s + ck[k]
    return s

def avgFactors(dic,coeff):
    ck = {}
    dk = {}
    nk = {}
    s = 0
    for k, v in coeff.items():
        u = k.strip().lower()
        ck[u]=v
    for k, v in dic.items():
        u = k.strip().lower()
        dk[u]=v

    for k, v in dk.items():
        if k in ck.keys():
            nk[k] = dk[k] * ck[k]

    for i in nk.values():
        s += i

    return s / sumFactors(dic, coeff)

def valid(dic, coeff):
    if sumFactors(dic, coeff) >= 30:
        if avgFactors(dic, coeff) >= 10:
            return True
        else:
            return False
    else:
        return False

def validCount(lis, coeff):
    s = 0
    for i in lis:
        if valid(i, coeff) is True:
            s +=1
        else:
            pass
    return s


def multDict(lis, mat, x):
    


print(validCount(l1, coeffs))

