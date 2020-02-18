stock={"crayon ":43 ," stylobleu ":23 ," stylorouge ":40 ,"gomme":12 ," regle ":25 , "compas":10}
commande1={"crayon ": 3 ," stylovert ":23 ,"gomme":22 ," regle ":5}
commande2={"crayon ": 3 ,"gomme":12 ,"compas":2}

def mergeOrders(order1, order2):
    d = {}
    d.update(order1)
    for k,v in order2.items():
        if not k in d:
            d.update({k:v})
        elif k in d:
            d[k] = d[k] + order2[k]
    return d

print(mergeOrders(commande1, commande2))
