def bin2dec(bin):
    l = len(bin)
    b = list(bin)
    d = 0
    for i,e in enumerate(b):
        d = d + (int(e) * 2 ** (l - i - 1))


    print(d)

def list2string(list):
    str1=''
    for i in list:
        i = str(i)
        str1 += i
    return str1

def dec2bin(dec):
    dec = int(dec)
    p = int(dec)
    l = []

    while dec > 1:

        p = dec % 2
        dec = int(dec / 2)
        l.append(p)

    return list2string(l)

print(dec2bin(6202))