from collections import deque
from rich.console import Console
from rich.table import Table

def water_jug_dfs(current_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path):
    jug1, jug2 = current_state
    if jug1 == goal_capacity or jug2 == goal_capacity:
        return path + [current_state]

    visited.add(current_state)

    # Fill jug1
    new_state = (jug1_capacity, jug2)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    # Fill jug2
    new_state = (jug1, jug2_capacity)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    # Empty jug1
    new_state = (0, jug2)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    # Empty jug2
    new_state = (jug1, 0)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    # Pour from jug1 to jug2
    transfer_amount = min(jug1, jug2_capacity - jug2)
    new_state = (jug1 - transfer_amount, jug2 + transfer_amount)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    # Pour from jug2 to jug1
    transfer_amount = min(jug2, jug1_capacity - jug1)
    new_state = (jug1 + transfer_amount, jug2 - transfer_amount)
    if new_state not in visited:
        result = water_jug_dfs(new_state, jug1_capacity, jug2_capacity, goal_capacity, visited, path + [current_state])
        if result:
            return result

    return None

def water_jug_dfs_wrapper(jug1_capacity, jug2_capacity, goal_capacity):
    initial_state = (0, 0)
    visited = set()
    path = water_jug_dfs(initial_state, jug1_capacity, jug2_capacity, goal_capacity, visited, [])
    return path

# Get user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
goal_capacity = int(input("Enter the target amount of water required: "))


# Solve the water jug problem using DFS and get the path
path = water_jug_dfs_wrapper(jug1_capacity, jug2_capacity, goal_capacity)

# Print the path or indicate no solution
if path:
    print(f"Steps to measure {goal_capacity} liters in one of the jugs:")
    for state in path:
        print(state)
else:
    print(f"No solution found to measure {goal_capacity} liters in one of the jugs.")