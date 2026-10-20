goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

def h(state):
    c = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                c += 1
    return c

def zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def astar(start):
    open = [(h(start), 0, start)]
    visited = []

    while open:
        open.sort()
        f, g, state = open.pop(0)

        if state == goal:
            for row in state:
                print(row)
            return

        if state in visited:
            continue

        visited.append(state)

        x, y = zero(state)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new = [r[:] for r in state]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                if new not in visited:
                    open.append((g + 1 + h(new), g + 1, new))

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

astar(start)