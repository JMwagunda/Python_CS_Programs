import heapq  # Import the heapq module for priority queue implementation

# Define a class to represent the state of the chessboard
class State:
    def __init__(self, board, cost, heuristic_value):
        self.board = board
        self.cost = cost
        self.heuristic_value = heuristic_value

    def __lt__(self, other):
        return (self.cost + self.heuristic_value) < (other.cost + other.heuristic_value)

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

# Solve the N Queens problem using A* informed search
def solve_n_queens_a_star():
    board_size = 8  # Set the size of the chessboard
    initial_board = [[0] * board_size for _ in range(board_size)]  # Create an empty chessboard
    priority_queue = []  # Initialize the priority queue

    # Add the initial state to the priority queue
    initial_state = State(initial_board, 0, heuristic(initial_board))
    heapq.heappush(priority_queue, initial_state)

    # Main loop for A* search
    while priority_queue:
        current_state = heapq.heappop(priority_queue)

        if current_state.heuristic_value == 0:  # Check if the goal state is reached
            for row in current_state.board:  # Print the solution if found
                print(row)
            return

        # Generate successor states and add them to the priority queue
        for col in range(board_size):
            for row in range(board_size):
                if is_safe(current_state.board, row, col):
                    new_board = [row[:] for row in current_state.board]
                    new_board[row][col] = 1
                    new_cost = current_state.cost + 1
                    new_heuristic = heuristic(new_board)
                    new_state = State(new_board, new_cost, new_heuristic)
                    heapq.heappush(priority_queue, new_state)

    print("No solution found")  # Print if no solution found

solve_n_queens_a_star()  # Call the function to solve the problem using A* informed search