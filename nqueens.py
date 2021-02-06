<<<<<<< HEAD
=======

import random

>>>>>>> f9fb2d850cc9f1e0e3c3ec6a4d0d8e15ae5f6975
# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    # Creating the board.
    board = [[0 for col in range(board_size)] for row in range(board_size)]

    # TODO: Create algo for randomly putting queens on board
    # TODO: Implement this: 
    # A reasonably good starting point can, 
    # for instance, be found by putting each queen in its own row and column so that it conflicts with the smallest number of queens already on the board

# Checks to see if a board space is available   
def checkPos(row, col, board):
    # Checks row/column
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col]== 1:
            return False

        # Checks the diagonal
        for j in range(len(board)):
            if (i+j == row+col) or (i-j == row-col):
                if board[i][j] == 1:
                    return False
    return True




if __name__ == "__main__":
    solve(4)