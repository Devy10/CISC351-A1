import random

import random as r
import timeit


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    counter = 0;
    start = timeit.default_timer()

    while True:
        board, conflictList = initializeBoard(board_size)
        for i in range(0, 12):
            counter = counter + 1;
            if solution(board, board_size):
                stop = timeit.default_timer()
                print("Swaps: " + str(counter) + " Time: " + str(stop - start))
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
    if minimalConflictor == 0:
        conflicting = False

    return board, conflicting


# Check if the result is the solution of the problem
def solution(board, boardSize):
    if not board:
        return False

    if len(board) != len(set(board)):
        return False

    diagonal1 = []
    diagonal2 = []

    for i in range(0, boardSize):
        diagonal1.append(board[i] + i)
        diagonal2.append(board[i] - i)

    if len(diagonal1) != len(set(diagonal1)) or len(diagonal2) != len(set(diagonal2)):
        return False

    return True
