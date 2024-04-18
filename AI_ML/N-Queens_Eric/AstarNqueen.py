#this is an informed search that uses a heruistics that checks the number of attacking queens at each step to determine the best course to follow 
N = 8

def print_solution(board):
	for i in range(N):
		for j in range(N):
			if board[i][j] == 1:
				print("Q",end=" ")
			else:
				print(".",end=" ")
		print()

  
def is_safe(board, row, col):

	# Check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check upper diagonal on left side
	for i, j in zip(range(row, -1, -1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Check lower diagonal on left side
	for i, j in zip(range(row, N, 1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True



def heuristic(board):
    # A simple heuristic: count the number of attacking queen pairs
    attacks = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i][j] == 1 or board[j][i] == 1:
                attacks += 1
    return attacks

def a_star_search(board, col):
    if col == len(board):
        return board, heuristic(board)

    possible_states = []
    for i in range(len(board)):
        if is_safe(board, i, col):
            new_board = [row[:] for row in board]   
            new_board[i][col] = 1
            print_solution(new_board)
            print(' ')
            h_value = heuristic(new_board)
            possible_states.append((new_board, h_value))

    possible_states.sort(key=lambda x: x[1])  # Sort by heuristic value
    for new_board, _ in possible_states:
        result, h_value = a_star_search(new_board, col + 1)
        if result is not None:
            return result, h_value

    return None, float('inf')

def solve_n_queens_a_star():
    board_size = 8
    initial_board = [[0] * board_size for _ in range(board_size)]
    result, h_value = a_star_search(initial_board, 0)

    if result is None:
        print("Solution does not exist")
        return False

    print_solution(result)
    print(' ')
    return True

if __name__ == '__main__':
    solve_n_queens_a_star()
