# Function to print the solution
def printSolution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Function to check whether the position is safe or not
def isSafe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# The function that solves the problem using backtracking
def solveNQueens(n):
    def backtrack(col):
        if col >= n:
            return True

        for row in range(n):
            if isSafe(board, row, col):
                board[row][col] = 1
                steps.append([row[:] for row in board])

                if backtrack(col + 1):
                    return True

                board[row][col] = 0  # BACKTRACK
                steps.append([row[:] for row in board])

        return False

    board = [[0] * n for _ in range(n)]
    steps = []

    if backtrack(0):
        return board, steps
    else:
        return None, None

# Get user input for the number of queens
n = int(input("Enter the number of queens: "))

# Solve the N queens problem
solution, steps = solveNQueens(n)

# Print solution or steps
if solution:
    print("Solution:")
    printSolution(solution)
    print("Number of steps taken:", len(steps))
else:
    print("No solution exists for the given number of queens.")
