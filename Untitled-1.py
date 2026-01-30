
from collections import deque

# Capacities of the jugs
CAP_A = 4
CAP_B = 3

# Initial and goal state
INITIAL_STATE = (0, 0)  # (Jug A, Jug B)
GOAL_AMOUNT = 2        # 2 liters in Jug A

def get_next_states(state):
    a, b = state
    states = []

    # Fill Jug A
    states.append((CAP_A, b))

    # Fill Jug B
    states.append((a, CAP_B))

    # Empty Jug A
    states.append((0, b))

    # Empty Jug B
    states.append((a, 0))

    # Pour A -> B
    transfer = min(a, CAP_B - b)
    states.append((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, CAP_A - a)
    states.append((a + transfer, b - transfer))

    return states


def bfs():
    queue = deque()
    queue.append((INITIAL_STATE, []))
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)
        path = path + [current_state]

        # Goal check
        if current_state[0] == GOAL_AMOUNT:
            return path

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path))

    return None


# Run BFS
solution = bfs()

# Display result
if solution:
    print("✅ Solution Found!\n")
    print("Step-by-step states (Jug A, Jug B):")
    for step, state in enumerate(solution):
        print(f"Step {step}: Jug A = {state[0]}L, Jug B = {state[1]}L")
else:
    print("❌ No solution found.")
