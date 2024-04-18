from collections import deque
from rich.console import Console
from rich.table import Table

def water_jug_problem_bfs(jug1_capacity, jug2_capacity, goal_capacity):
    initial_state = (0, 0)
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        jug1, jug2 = current_state

        if jug1 == goal_capacity or jug2 == goal_capacity:
            return path + [current_state]

        new_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug1 + jug2, jug2_capacity)),  # Pour from jug1 to jug2
            (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1)))   # Pour from jug2 to jug1
        ]

        for new_state in new_states:
            if new_state not in visited:
                queue.append((new_state, path + [current_state]))
    return None

console = Console()

# Get user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
goal_capacity = int(input("Enter the target amount of water required: "))

# Solve the water jug problem and get the path
path = water_jug_problem_bfs(jug1_capacity, jug2_capacity, goal_capacity)

if path:
    console.print("Steps to measure", goal_capacity, "liters in one of the jugs:")
    table = Table(title="Steps")
    table.add_column("Jug 1", justify="center")
    table.add_column("Jug 2", justify="center")
    for state in path:
        table.add_row(str(state[0]), str(state[1]))
    console.print(table)
    console.print("Number of steps taken:", len(path) - 1)
else:
    console.print(f"No solution found to measure {goal_capacity} liters in one of the jugs.")