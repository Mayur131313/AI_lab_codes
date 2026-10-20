from collections import deque

# Initial state: A, B, C are all on the table
initial_state = (
    ("A", "Table"),
    ("B", "Table"),
    ("C", "Table")
)

# Goal state: A on B, B on C, C on Table
goal_state = (
    ("A", "B"),
    ("B", "C"),
    ("C", "Table")
)


def get_moves(state):
    """Generate all possible legal moves."""
    moves = []

    # Find blocks that have another block on them
    blocked = {x for x, y in state if y != "Table"}

    for block, position in state:

        # A block can be moved only if it is clear
        if block in blocked:
            continue

        # Move block to the table
        if position != "Table":
            new_state = list(state)

            for i, (b, p) in enumerate(new_state):
                if b == block:
                    new_state[i] = (b, "Table")

            moves.append((
                tuple(sorted(new_state)),
                f"Move {block} to Table"
            ))

        # Move block onto another block
        for target, target_position in state:
            if block == target:
                continue

            # Target must be clear
            if target in blocked:
                continue

            # Block cannot be placed on itself
            if block == target:
                continue

            new_state = list(state)

            for i, (b, p) in enumerate(new_state):
                if b == block:
                    new_state[i] = (b, target)

            moves.append((
                tuple(sorted(new_state)),
                f"Move {block} onto {target}"
            ))

    return moves


def bfs(initial, goal):
    queue = deque([(initial, [])])
    visited = {initial}

    while queue:
        current_state, path = queue.popleft()

        # Goal test
        if current_state == goal:
            return path

        # Generate next states
        for new_state, action in get_moves(current_state):
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [action]))

    return None


# Run BFS
solution = bfs(initial_state, goal_state)

print("Initial State:")
print(initial_state)

print("\nGoal State:")
print(goal_state)

print("\nBFS Solution:")

if solution:
    for step, action in enumerate(solution, 1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")