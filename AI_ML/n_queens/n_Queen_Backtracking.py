import heapq
import time

# Define a heuristic function to estimate the cost of a state
def heuristic(board):
    conflicts = 0  # Initialize conflicts counter
    # Iterate over each queen on the board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                # Check conflicts in the same row
                for k in range(j+1, len(board)):
                    if board[i][k] == 1:
                        conflicts += 1
                # Check conflicts in the upper diagonal
                for k, l in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
                    if board[k][l] == 1:
                        conflicts += 1
                # Check conflicts in the lower diagonal
                for k, l in zip(range(i+1, len(board)), range(j-1, -1, -1)):
                    if board[k][l] == 1:
                        conflicts += 1
    return conflicts  # Return the total number of conflicts as the heuristic value

# Check if it's safe to place a queen at a given position
def is_safe(board, row, col):
    # Check if there's no queen in the same row or in the upper/lower diagonals
    for i in range(col):
        if (board[row][i] == 1) or (board[i][col] == 1 and abs(i-row) == abs(col-i)):
            return False
    return True

# Solve the N Queens problem using backtracking
def solve_n_queens(board, col, steps):
    if col >= len(board):  # Base case: all queens are placed
        return True
    # Try placing a queen in each row of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place the queen
            steps[0] += 1  # Increment step count
            if solve_n_queens(board, col + 1, steps):  # Recursively solve for the next column
                return True
            board[i][col] = 0  # Backtrack if no solution found
    return False

# Solve the N Queens problem and measure time and steps
def solve_n_queens_with_time(n):
    start_time = time.time()  # Record start time
    steps = [0]  # Initialize step count
    board = [[0] * n for _ in range(n)]  # Create an NxN chessboard
    if solve_n_queens(board, 0, steps):  # Start solving from the first column
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print("Solution found in {:.6f} seconds with {} steps:".format(elapsed_time, steps[0]))
        for row in board:  # Print the solution if found
            print(row)
    else:
        print("No solution found")  # Print if no solution found

# Example usage: Solve the 8 Queens problem and measure time and steps
solve_n_queens_with_time(8)
