import random

import random as r
import timeit

# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    # Creating the board.
    board = [[0 for col in range(board_size)] for row in range(board_size)]
    for i in range(len(board)):
        board[i][i] = 1

    counter = 0;

    start = timeit.default_timer()

    while True:
        board = randomShuffle(board_size)
        board = initializeBoard(board)
        for i in range(0, 60):
            counter = counter + 1;
            answer = converter(board, board_size)
            if solution(answer, board_size):
                stop = timeit.default_timer()
                print("Swaps: " + str(counter) + " Time: " + str(stop - start))
                return answer
            queens = findQueens(board)
            board = minConflicts(board, 1, queens)

def initializeBoard(board):
    queens = findQueens(board);
    for i in range(len(board)):
        row = queens[i][0]
        column = queens[i][1]
        minimumConflict = len(board)
        rowList = []
        for j in range(len(board)):
            currentConflict = checkConflicts(j, column, board)
            if currentConflict < minimumConflict:
                minimumConflict = currentConflict
                rowList = [j]
            elif currentConflict == minimumConflict:
                rowList.append(j)

        newRow = r.choice(rowList)

        board[row][column] = 0
        board[newRow][column] = 1

    return board


def converter(board, boardSize):

    rowVector = [];

    for i in range(1, boardSize + 1):
        for j in range(1, boardSize + 1):
            if board[j-1][i-1] == 1:
                rowVector.append(j);

    return rowVector

# Checks to see if a board space is available
def minConflicts(board, steps, queens):
    for i in range(steps):
        # Checks to see if the board is a solution before carrying on.
        #if solution(board):
            #return board

        random = r.choice(queens)
        row = random[0]
        column = random[1]
        minimumConflict = len(board)
        rowList = []

        for j in range(0, len(board)):
            currentConflict = checkConflicts(j, column, board)
            if currentConflict < minimumConflict:
                minimumConflict = currentConflict
                rowList = [j]
            elif currentConflict == minimumConflict:
                rowList.append(j)

        newRow = r.choice(rowList)

        board[row][column] = 0
        board[newRow][column] = 1

        return board


        # Pick random variable of all chosen conflicting queens.
        # queens is list of tuples (x,y).
        #queens = findQueens(board)
        #conflicting = []
        #for queen in queens:
            #if checkConflicts(queen[0], queen[1], board) > 0:
                #conflicting.append(queen)
        # Queen picked at random
        #chosenOne = r.choice(conflicting)

        # Pick coordinates for chosenOne that minimizes conflicts
        #best = checkConflicts(chosenOne)
        #row = chosenOne[0]
        #col = chosenOne[1]

        # Gather a list of conflicts for entire column
        #conflicts = []
        #for i in range(len(board)):
            #conflicts.append(checkConflicts(i, col, board))

        # Index of smallest conflicts.
        #index = conflicts.index(min(conflicts))

        # Move queen to new index
        #board[row][col] = 0
        #board[index][col] = 1

    # In the event no solution is found.
    # TODO: Call a new board and redo the minConflicts().
    #return False


# TODO: Find better way to do this
def findQueens(board):
    queens = []
    b = len(board)
    for i in range(b):
        for j in range(b):
            if board[j][i] == 1:
                queens.append((j, i))
    return queens


# Checks to see if a board space is available
def checkConflicts(row, col, board):
    conflicts = 0
    # Checks row/column
    for i in range(len(board)):
        # Queen cannot conflict with itself
        if board[row][i] == 1 and col != i:
            conflicts += 1
        #if board[i][col] == 1 and row != i:
            #conflicts += 1

        # For diagonals
        for j in range(len(board)):
            if (row + col == i + j) or (row - col == i - j):
                if board[i][j] == 1 and (i != row and j != col):
                    conflicts += 1

    return conflicts

# Creates a new board with random placement of queens.
def randomShuffle(n):
    # Creates a new blank board
    board = [[0 for col in range(n)] for row in range(n)]

    # Place n queens
    for i in range(n):
        #while True:
        row = r.randint(0,n-1)
        board[row][i] = 1
            #col = r.randint(0,n-1)

            #if board[row][col] == 0:
                #board[row][col] = 1
                #break


    return board

def solution(board, boardSize):
    for x in range(1, boardSize + 1):
        for y in range(x + 1, boardSize + 1):
            if board[x-1] == board[y-1]:
                return False

    for i in range(1, boardSize + 1):
        j = i
        k = board[i - 1]
        while j < boardSize and k < boardSize:
            j = j + 1
            k = k + 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j < boardSize and k > 1:
            j = j + 1
            k = k - 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j > 1 and k < boardSize:
            j = j - 1
            k = k + 1
            if board[j - 1] == k:
                return False
        j = i
        k = board[i - 1]
        while j > 1 and k > 1:
            j = j - 1
            k = k - 1
            if board[j - 1] == k:
                return False
    return True

if __name__ == "__main__":
    solve(4)
