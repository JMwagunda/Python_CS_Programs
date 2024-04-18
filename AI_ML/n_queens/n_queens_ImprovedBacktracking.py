# Function to print the solution
def printSolution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

# The function that solves the problem using improved backtracking
def solveNQueens(n):
    def isSafe(row, col, slashCode, backslashCode, rowLookup):
        if slashCode[row + col] or backslashCode[row - col + n - 1] or rowLookup[col]:
            return False
        return True

    def solveNQueensUtil(col, slashCode, backslashCode, rowLookup, board, steps):
        if col == n:
            return True

        for row in range(n):
            if isSafe(row, col, slashCode, backslashCode, rowLookup):
                board[row][col] = 1
                slashCode[row + col] = True
                backslashCode[row - col + n - 1] = True
                rowLookup[col] = True

                steps.append([row[:] for row in board])  # Record the current state
                if solveNQueensUtil(col + 1, slashCode, backslashCode, rowLookup, board, steps):
                    return True

                board[row][col] = 0  # BACKTRACK
                slashCode[row + col] = False
                backslashCode[row - col + n - 1] = False
                rowLookup[col] = False

        return False

    board = [[0] * n for _ in range(n)]
    steps = []

    slashCode = [False] * (2 * n - 1)
    backslashCode = [False] * (2 * n - 1)
    rowLookup = [False] * n

    if not solveNQueensUtil(0, slashCode, backslashCode, rowLookup, board, steps):
        print("No solution exists for the given number of queens.")
    else:
        print("Solution:")
        printSolution(board)
        print("Number of steps taken:", len(steps))

# Get user input for the number of queens
n = int(input("Enter the number of queens: "))

# Solve the N queens problem using improved backtracking
solveNQueens(n)