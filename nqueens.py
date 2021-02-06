import random as r

# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    # Creating the board.
    board = [[0 for col in range(board_size)] for row in range(board_size)]

    # Initial config of queens on board.
    for i in range(len(board)):
        board[i][i] = 1

    print(board)
    board = randomShuffle(board_size)

    print(board)

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

# Creates a new board with random placement of queens.
def randomShuffle(n):
    # Creates a new blank board
    board = [[0 for col in range(n)] for row in range(n)]

    # Place n queens
    for i in range(n):
        while True:
            row = r.randint(0,n-1)
            col = r.randint(0,n-1)
            
            if board[row][col] == 0:
                board[row][col] = 1
                break
            
            
    return board



if __name__ == "__main__":
    solve(4)