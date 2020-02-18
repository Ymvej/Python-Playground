testDominos = [[0,0],[0,1],[1,1],[4,6]]



def countPoints(listDominos): # counts the total points value of a list of Dominos
    c = 0
    for i in listDominos: # iterates over each domino on the list of Dominos
        for j in i: # iterates over each side of a single domino
            c += j # adds each value it reads to the c variable, which is the total number of points that the function eventually returns
    return c

def bestDomino(listDominos): # finds the best valued Domino in a list of Dominos
    bD = []
    maxC = 0
    for i in listDominos: # iterates over each domino on the list of Dominos
        c = 0 # reset the value counter, used 2 lines later
        for j in i: # iterates over each side of a single domino
            c += j # counts the value of that domino
        if c > maxC: # if it's the highest domino encountered yet...
            bD = i # ...set bD (the returned variable) to its value in list form
        else:
            pass # if it's not, we do nothing
    return bD

def createDominos(): # creates a 2-dimensional array filled with all 28 possible dominos
    dominos = []
    for i in range(0,7): # loops 6 times, i being the first digit of each domino
        for j in range(0,7): # in each loop on the first digit, loops 6 times, j being the second digit
            if [i,j] and [j,i] not in dominos: # checks if the unique combination of values we're currently iteraring is already in the set
                dominos.append([i,j]) # if not already in the set, adds the domino [i, j] to the set
    return dominos # returns the whole set

def showDominos(listDominos): # outputs a readable list of dominos when provided a 2-dimensional array
    string = ''
    for i in listDominos: # iterates over a 2d array
        string += str(i) # adds our current iteration in the string
        if i is not listDominos[-1]: # checks if our current iteration is the last iteration of the argument list
            string = string + '-' # if it's not, adds a dash to the end of the string. this is necessary to avoid having our list finishing with a dash
    return string

def isDominoPlayable(domino, board): # returns True if a domino is playable on the current board
    for i in domino: # iterates over the two digits composing a single domino
        if board[0][0] or board[-1][-1] is i: # if one of them is the same as either the first digit on the board or the last digit on the board, returns True
            return True
        elif board is []: # if not and the board is empty, returns True
            return True
        else: # if not, returns False
            return False

def isHandPlayable(hand, board):
    pD = []
    for i in hand:
        if isDominoPlayable(i) is True:
            pD.append(i)
        else:
            pass
    return pD


l = createDominos()

# print(l)
# print(len(l))

test = showDominos(l)
print(test)