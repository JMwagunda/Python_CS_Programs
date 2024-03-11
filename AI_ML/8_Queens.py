def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col):
    # Base case: all queens are placed
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen in [i, col]
            board[i][col] = 1

            # Recursively check if placing the queen leads to a solution
            if solve_n_queens(board, col + 1):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If all rows have been tried and nothing worked, return false
    return False

def solve_8_queens():
    board = [[0] * 8 for _ in range(8)]  # Create an 8x8 chessboard

    if solve_n_queens(board, 0):
        # Print the solution
        for row in board:
            print(row)
    else:
        print("No solution found")

solve_8_queens()
