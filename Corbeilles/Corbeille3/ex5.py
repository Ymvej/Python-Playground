import random
authChar = 'azertyuiopqsdfghjklmwxcvbnéèàç'
message = 'This is a testing variable'
# global authInt
authInt = []
for i in range(0,256):
    authInt.append(i)

print(authInt)
def enigma(authC):
    dic = {}
    for i in authC:
        dic.update([(i, random.choice(authInt))])
        print(authInt)
        print(dic)
        del authInt[dic[i]]

    return dic

def code(dic, mess):
    for i in mess:
        print(i)

print(enigma(authChar))
code(enigma(authChar), message)