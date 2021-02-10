import random

import random as r
import timeit


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):
    counter = 0;

    start = timeit.default_timer()

    while True:
        #board = list(range(1, board_size + 1))
        #random.shuffle(board)
        board, conflictList = initializeBoard(board_size)
        '''if solution(board, board_size):
            stop = timeit.default_timer()
            print("Swaps: " + str(counter) + " Time: " + str(stop - start))
        exit(0)'''
        for i in range(0, 12):
            counter = counter + 1;
            #print("Swaps: " + str(counter) + " Time: " + str(stop - start))
            #exit(0)
            if solution(board, board_size):
                stop = timeit.default_timer()
                print("Swaps: " + str(counter) + " Time: " + str(stop - start))
                print(conflictList)
                exit(0)
                return board
            var = r.choice(conflictList)
            board, conflicting = minConflicts(board, board_size, var)
            if not conflicting:
                conflictList.remove(var)

# TO REVISE!!

def initializeBoard(boardSize):



    board = []
    conflictList = []
    integerList = list(range(1, boardSize + 1))
    integerList2 = list(range(0, boardSize))

    halfSize = int(boardSize / 2)



    if boardSize % 6 == 2:
        board = [0] * (boardSize)
        for i in range(1, halfSize + 1):
            index1 = (2 * (i - 1) + halfSize - 1) % boardSize
            index2 = boardSize - (index1 + 1)
            board[index1] = i
            board[index2] = boardSize + 1 - i
    elif (boardSize - 1) % 6 == 2:
        board = [0] * (boardSize)
        for i in range(1, halfSize + 1):
            index1 = (2 * (i - 1) + halfSize - 1) % (boardSize-1)
            index2 = boardSize - (index1 + 2)
            board[index1] = i
            board[index2] = boardSize - i
        board[boardSize-1] = boardSize
    else:
        for i in range(1, halfSize + 1):
            board.append(halfSize + i)
            board.append(i)
        if boardSize % 2 == 1:
            board.append(boardSize)

    for i in range(0, 8):
        randomInt = r.choice(integerList)
        randomIndex = r.choice(integerList2)
        board[randomIndex] = randomInt
        conflictList.append((randomInt, randomIndex))

    return board, conflictList


    '''board = []
    availableRows = list(range(1, boardSize + 1))
    nonConflictions = boardSize - 30

    for i in range(boardSize):
        randomRow = r.choice(availableRows)
        while not noConflict(randomRow, i, board) and nonConflictions > i:
            randomRow = r.choice(availableRows)
        board.append(randomRow)
        availableRows.remove(board[i])'''

    '''for i in range(0, boardSize):
        print(i)
        # possibleList = []
        # minConflicts = boardSize
        if board == []:
            board.append(r.choice(availableRows))
            availableRows.remove(board[i])
        else:
            possibleList = []
            minConflicts = boardSize
            for j in availableRows:
                if minConflicts > conflictor(j, i, board):
                    minConflicts = conflictor(j, i, board)
                    possibleList = [j]
                elif conflictor(j, i, board) == minConflicts:
                    possibleList.append(j)

            board.append(r.choice(possibleList))
            availableRows.remove(board[i])'''

    '''attackList = []

    for i in range(0, boardSize):
        currentAttack = checkConflicts(board[i], i, board, boardSize) + board.count(i) - 1
        attackList.append(currentAttack)

    return board, attackList'''

    '''print(i);
   '''


def conflictor(row, col, board):
    counter = 0
    for i in range(0, len(board)):
        if i + board[i] == row + col or row - col == board[i] - i:
            counter = counter + 1
    return counter


def noConflict(row, col, board):
    for i in range(0, len(board)):
        if i + board[i] == row + col or row - col == board[i] - i:
            return False
    return True


# Checks to see if a board space is available
def minConflicts(board, boardSize, var):

    #print(var)
    #print("Row: " + str(var[0]))
    #print("Column: " + str(var[1]))

    conflicting = True
    counterRow = [0] * (boardSize + 1)
    counterDiagonal1 = [0] * (2 * boardSize + 1)
    counterDiagonal2 = [0] * (2 * boardSize + 1)

    for i in range(boardSize):
        counterRow[board[i]] += 1
        counterDiagonal1[board[i] - i + boardSize] += 1
        counterDiagonal2[board[i] + i] += 1

    minimalConflictor = boardSize
    minimalRow = 0
    for j in range(1, boardSize + 1):
        currentConflictor = counterRow[j]
        currentConflictor += counterDiagonal1[j - var[1] + boardSize]
        currentConflictor += counterDiagonal2[j + var[1]]
        if (currentConflictor < minimalConflictor):
            minimalConflictor = currentConflictor
            minimalRow = j

    board[var[1]] = minimalRow
    if (minimalConflictor == 0):
        conflicting = False

    '''mostAttacked = 0
    #for i in range(0, boardSize):

    #maximum = max(attackList)
    #maxIndex = attackList.index(maximum)
    minConflict = boardSize
    minRow = []
    for i in range(1, boardSize+1):
        #currentAttack = checkConflicts(i, maxIndex, board, boardSize) + board.count(i) - 1
        #if (currentAttack < minConflict):
            #minConflict = currentAttack
            minRow = [i]
        #elif (currentAttack == minConflict):
            minRow.append(i)

    #board[maxIndex] = r.choice(minRow)'''

    '''attackList = []
    for i in range(0, boardSize):
        currentAttack = checkConflicts(board[i], i, board, boardSize) + board.count(i) - 1
        attackList.append(currentAttack)'''

    return board, conflicting


'''for i in range(0, board_size):
       for j in range(i + 1, board_size):
           #print("(" + str(i) + " : " + str(j) + "): " + str(board[i]) + " : " + str(board[j]))
           if not noConflict(board[i], i, board) or not noConflict(board[j], j, board):
               boardCopy = board.copy()
               con11 = checkConflicts(board[i], i, board, board_size)
               con12 = checkConflicts(board[j], j, board, board_size)
               total1 = con11 + con12
               boardCopy[j] = board[i]
               boardCopy[i] = board[j]
               con21 = checkConflicts(boardCopy[i], i, boardCopy, board_size)
               con22 = checkConflicts(boardCopy[j], j, boardCopy, board_size)
               total2 = con21 + con22
               if (total1 >= total2):
                   temp = board[i]
                   board[i] = board[j]
                   board[j] = temp'''


# Checks to see if a board space is available
def checkConflicts(row, col, board, boardSize):
    conflicts = 0
    # Checks row/column
    j = row
    k = col
    while j < boardSize and k < boardSize - 1:
        j = j + 1
        k = k + 1
        if board[k] == j:
            conflicts = conflicts + 1
    j = row
    k = col
    while j < boardSize and k > 0:
        j = j + 1
        k = k - 1
        if board[k] == j:
            conflicts = conflicts + 1
    j = row
    k = col
    while j > 1 and k < boardSize - 1:
        j = j - 1
        k = k + 1
        if board[k] == j:
            conflicts = conflicts + 1
    j = row
    k = col
    while j > 1 and k > 0:
        j = j - 1
        k = k - 1
        if board[k] == j:
            conflicts = conflicts + 1

    return conflicts


# Check if the result is the solution of the problem
def solution(board, boardSize):
    # check the rows and columns
    if len(board) != len(set(board)):
           return False

    # if len(board) != len(set(board)):
    # return False
    if not board:
        return False

    diagonal1 = []
    diagonal2 = []

    # check the diagonals
    for i in range(0, boardSize):
        diagonal1.append(board[i] + i)
        diagonal2.append(board[i] - i)

    if len(diagonal1) != len(set(diagonal1)) or len(diagonal2) != len(set(diagonal2)):
        return False

    '''j = board[i]
        k = i
        for w in range(i+1, boardSize):
            if j + k == board[w] + w or j - k == board[w] - w:
                return False'''
    '''while j < boardSize and k < boardSize - 1:
            j = j + 1
            k = k + 1
            if board[k] == j:
                return False
        j = board[i]
        k = i
        while j < boardSize and k > 0:
            j = j + 1
            k = k - 1
            if board[k] == j:
                return False
        j = board[i]
        k = i
        while j > 1 and k < boardSize - 1:
            j = j - 1
            k = k + 1
            if board[k] == j:
                return False
        j = board[i]
        k = i
        while j > 1 and k > 0:
            j = j - 1
            k = k - 1
            if board[k] == j:
                return False'''

    return True

if __name__ == "__main__":
    solve(4)

'''for j in range(i + 1, boardSize):
if j + board[j] == row + col or board[j] - j == row - col:
return False'''