import random

import random as r
import timeit


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    counter = 0;
    #start timing
    start = timeit.default_timer()
    # loop until a solution is found
    while True:
        board, conflictList = initializeBoard(board_size)
        #find the solution in 12 steps in a loop
        for i in range(0, 12):
            counter = counter + 1;
            #detect if a solution is found
            if solution(board, board_size):
                stop = timeit.default_timer()
                #print out the running time and the board
                print("Swaps: " + str(counter) + " Time: " + str(stop - start))
                exit(0)
                return board
            #pick a conflicted chess
            var = r.choice(conflictList)
            board, conflicting = minConflicts(board, board_size, var)
            if not conflicting:
                conflictList.remove(var)


# TO REVISE!!

def initializeBoard(boardSize):
    #the board, represented by a list of Integer
    #each Integer represent the number of row for a queen on each column
    board = []
    #the list of chess that conflicts with one or more another
    conflictList = []
    #list of integers 
    integerList = list(range(1, boardSize + 1))
    integerList2 = list(range(0, boardSize))

    halfSize = int(boardSize / 2)
    
    #initialize the board 
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
            index1 = (2 * (i - 1) + halfSize - 1) % (boardSize - 1)
            index2 = boardSize - (index1 + 2)
            board[index1] = i
            board[index2] = boardSize - i
        board[boardSize - 1] = boardSize
    else:
        for i in range(1, halfSize + 1):
            board.append(halfSize + i)
            board.append(i)
        if boardSize % 2 == 1:
            board.append(boardSize)
            
    #randomly pick some chess on the board
    for i in range(0, 8):
        randomInt = r.choice(integerList)
        randomIndex = r.choice(integerList2)
        board[randomIndex] = randomInt
        conflictList.append((randomInt, randomIndex))

    return board, conflictList


# Checks to see if a board space is available
def minConflicts(board, boardSize, var):
    conflicting = True
    counterRow = [0] * (boardSize + 1)
    counterDiagonal1 = [0] * (2 * boardSize + 1)
    counterDiagonal2 = [0] * (2 * boardSize + 1)
    #initilze a raw board for conflict detection
    for i in range(boardSize):
        counterRow[board[i]] += 1
        counterDiagonal1[board[i] - i + boardSize] += 1
        counterDiagonal2[board[i] + i] += 1

    minimalConflictor = boardSize
    minimalRow = 0
    #loop though the list to see if there are still conflicting 
    for j in range(1, boardSize + 1):
        currentConflictor = counterRow[j]
        currentConflictor += counterDiagonal1[j - var[1] + boardSize]
        currentConflictor += counterDiagonal2[j + var[1]]
        if (currentConflictor < minimalConflictor):
            minimalConflictor = currentConflictor
            minimalRow = j
    #move the conflicted chess to a row with minimum conflicts
    board[var[1]] = minimalRow
    if minimalConflictor == 0:
        conflicting = False

    return board, conflicting


# Check if the result is the solution of the problem
def solution(board, boardSize):
    # no solution if no input for board
    if not board:
        return False
    # no solution if there is no queen on one or more rows
    if len(board) != len(set(board)):
        return False

    diagonal1 = []
    diagonal2 = []
    #checking the diagonals
    for i in range(0, boardSize):
        diagonal1.append(board[i] + i)
        diagonal2.append(board[i] - i)
    # solution invalid if there is conflict in diagonal
    if len(diagonal1) != len(set(diagonal1)) or len(diagonal2) != len(set(diagonal2)):
        return False

    return True
