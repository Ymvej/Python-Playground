# a = 0
# b = 32
# resultat = 0
# mult = 0

# for i in range(a, b):
#     if i % 3 == True and i % 5 == True:
#         resultat = resultat + i-1
#         print(resultat)
#     else:
#         pass

# print(resultat)


a = 0
b = 32
resultat = 0
mult = 0

for i in range(a, b):
    if i % 3 == True or i % 5 == True:
        resultat = resultat + i-1
        print(resultat)
    else:
        pass

print(resultat)