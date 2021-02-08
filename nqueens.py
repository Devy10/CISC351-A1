import random

import random as r
import timeit


# Implement a solver that returns a list of queen's locations
#  - Make sure the list is the right length, and uses the numbers from 0 .. BOARD_SIZE-1
def solve(board_size):

    counter = 0;
    
    # Measures the starting execution time 
    start = timeit.default_timer()

    while True:
        board = randomShuffle(board_size) # Randomly places N queens on the board
        board = initializeBoard(board) # Rearranges the positions of N-queens without any conflicts
        
        for i in range(0, 60):
            counter = counter + 1;
            answer = converter(board, board_size)
            if solution(answer, board_size):
                stop = timeit.default_timer() # Measures the stopping execution time
                
                # Prints runtime - how long it takes to perform a series of swaps
                print("Swaps: " + str(counter) + " Time: " + str(stop - start)) 
                return answer
            
            # A list determining the positions (i,j) of current queens on the board
            queens = findQueens(board)
            board = minConflicts(board, 1, queens)

# TO REVISE!!

def initializeBoard(boardSize):
   newBoard = []
   availableRows = list(range(1, boardSize + 1))
   nonConflictions = boardSize - 50

   for i in range(0, boardSize):
       randomRow = r.choice(availableRows)
       while not noConflict(randomRow, i, newBoard) and nonConflictions > i:
           randomRow = r.choice(availableRows)
       newBoard.append(randomRow)
       availableRows.remove(newBoard[i])

   return newBoard


def noConflict(row, col, board):
   for i in range(0, len(board)):
       if i + board[i] == row + col or row - col == board[i] - i:
           return False
   return True


# Checks to see if a board space is available
def minConflicts(board, board_size):

   for i in range(0, board_size):
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
                   board[j] = temp

   return board


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
   '''for element in board:
       if board.count(element) > 1:
           return False'''

   # if len(board) != len(set(board)):
   # return False
   if not board:
       return False

   # check the diagonals
   for i in range(0, boardSize):
       j = board[i]
       k = i
       while j < boardSize and k < boardSize - 1:
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
               return False
   return True


if __name__ == "__main__":
   solve(4)
