from collections import deque

def jug_problem(x, y, goal):
    # Create a queue to store the states
    queue = deque()
    # Create a set to store visited states
    visited = set()
    # Add the initial state to the queue
    queue.append((0, 0))
    # Start the breadth-first search
    while queue:
        # Get the current state
        state = queue.popleft()
        # Check if the current state is the goal state
        if state == goal:
            return True
        # Check if the current state has been visited
        if state in visited:
            continue
        # Mark the current state as visited
        visited.add(state)
        # Get the amount of water in each jug
        jug_x, jug_y = state
        # Fill jug x
        if jug_x < x:
            queue.append((x, jug_y))
        # Fill jug y
        if jug_y < y:
            queue.append((jug_x, y))
        # Pour water from jug x to jug y
        if jug_x > 0 and jug_y < y:
            pour_amount = min(jug_x, y - jug_y)
            queue.append((jug_x - pour_amount, jug_y + pour_amount))
        # Pour water from jug y to jug x
        if jug_y > 0 and jug_x < x:
            pour_amount = min(jug_y, x - jug_x)
            queue.append((jug_x + pour_amount, jug_y - pour_amount))
        # Pour water from jug x onto the ground
        if jug_x > 0:
            queue.append((0, jug_y))
        # Pour water from jug y onto the ground
        if jug_y > 0:
            queue.append((jug_x, 0))
    # If the goal state is not reached, return False
    return False

# Test the jug_problem function
x = 4
y = 5
goal = (0, 2)
print(jug_problem(x, y, goal))  # Output: True
