from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, goal_capacity):
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

# Get user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of jug 1: "))
jug2_capacity = int(input("Enter the capacity of jug 2: "))
goal_capacity = int(input("Enter the target amount of water required: "))

# Solve the water jug problem and get the path
path = water_jug_problem(jug1_capacity, jug2_capacity, goal_capacity)

# Print the path or indicate no solution
if path:
    print(f"Steps to measure {goal_capacity} liters in one of the jugs:")
    for state in path:
        print(state)
else:
    print(f"No solution found to measure {goal_capacity} liters in one of the jugs.")
