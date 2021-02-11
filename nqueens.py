import random

import random as r
import timeit


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    """Solves the n-queens problem given a board size n

    Args:
        board_size (int): The size of the n*n board containing n queens.

    Returns:
        board (int[]): A list where each element corresponds to the row of a queen.  It is 1-based.
    """

    counter = 0;
    # Starts the timer.
    start = timeit.default_timer()
    # Loop until a solution is found.
    while True:
        board, conflictList = initializeBoard(board_size)
        # The range here is the max_steps from the MINCONFLICTS() algorithm shown in the PDF.
        for i in range(12):
            counter += 1
            # Checks to see if the board is a solution.
            if solution(board, board_size):
                stop = timeit.default_timer()
                # Prints out the running time and the board
                print("Swaps: " + str(counter) + " Time: " + str(stop - start))
                return board
            # If not a solution, chose a random conflicting Queen.
            var = r.choice(conflictList)
            board, conflicting = minConflicts(board, board_size, var)
            if not conflicting:
                conflictList.remove(var)


# TO REVISE!!

def initializeBoard(boardSize):
    """Initializes the representation of the chess board.

    Args:
        boardSize (int): The size of the n*n board
    
    Returns:
        board (int[]): The representation of the chess board
        conflictList (int[(int, int)]): A list of tuples of type (int, int),
                                        this gets passed on to the minConflicts() function.
    """

    board = []
    # The list of Queens that conflict with each other.
    conflictList = []
    integerList = list(range(1, boardSize + 1))
    integerList2 = list(range(boardSize))

    halfSize = int(boardSize / 2)
    
    """
    The general idea is reducing the problem to a knight's problem.
    Two knights could take over each other on a 3*2 or 2*3 board on the corner,
    if we switch the knights to queens, it will show that the queens are not conflicting with each other on row/column/diagonal.
    The purpose of this part of algorithm is to repeat this process until the board has enough queens.
    The situation will change according to the size of the board, each branch of the if statement shows a different case
    """
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
            
    """
    Randomly picks x Queens to shuffle, creating conflicts. 
    This shows that our algorithm works, and it works well.
    The higher the value of x, the more our algorithm has to work.
    """
    for i in range(8):
        randomInt = r.choice(integerList)
        randomIndex = r.choice(integerList2)
        board[randomIndex] = randomInt
        conflictList.append((randomInt, randomIndex))

    return board, conflictList


def minConflicts(board, boardSize, var):
    """Checks to see if a Queen is conflicting with any other Queens on the board.

    Args:
        board (int[])   : The representation of our chess board.
        boardSize (int) : The size of the n*n chess board.
        var ((int,int)) : An element of the conflictList list that initializeBoard() returns.

    Returns:
        board (int[])       : The representation of our chess board.
        conflicting (bool)  : Whether the Queen is conflicting with another piece.
    """

    conflicting = True
    # Initializes a new board for conflict detection.
    counterRow = [0] * (boardSize + 1)
    counterDiagonal1 = [0] * (2 * boardSize + 1)
    counterDiagonal2 = [0] * (2 * boardSize + 1)

    # Gets the number of conflicts on rows/diagonals.
    for i in range(boardSize):
        counterRow[board[i]] += 1
        counterDiagonal1[board[i] - i + boardSize] += 1
        counterDiagonal2[board[i] + i] += 1

    minimalConflictor = boardSize
    minimalRow = 0
    
    # Loops through the board, adding the conflicts on each row and diagonal.
    for i in range(1, boardSize + 1):
        currentConflictor = counterRow[i]
        currentConflictor += counterDiagonal1[i - var[1] + boardSize]
        currentConflictor += counterDiagonal2[i + var[1]]
        if (currentConflictor < minimalConflictor):
            minimalConflictor = currentConflictor
            minimalRow = i
    # Moves the Queen to the row with minimal conflicts.
    board[var[1]] = minimalRow

    # Checks to see if there is still a conflict after the move.
    if minimalConflictor == 0:
        conflicting = False

    return board, conflicting


def solution(board, boardSize):

    """Checks to see if the board is a solution.

    Args:
        board (int[])   : The representation of the chess board.
        boardSize (int) : The size of the n*n chess board.
    """

    # If there is no board, no solution.
    if not board:
        return False
   
    """
    The set() function removes duplicates (turns a list into a set).
    For a board to be a solution, there needs to be exactly one Queen on every row & column.
    So if the length of the board is the same as the length of the set of the board, that means all elements are unique.
    """
    if len(board) != len(set(board)):
        return False

    diagonal1 = []
    diagonal2 = []

    # Checks the diagonals.
    for i in range(0, boardSize):
        diagonal1.append(board[i] + i)
        diagonal2.append(board[i] - i)
    # This is for the same reason as above.
    if len(diagonal1) != len(set(diagonal1)) or len(diagonal2) != len(set(diagonal2)):
        return False

    return True
