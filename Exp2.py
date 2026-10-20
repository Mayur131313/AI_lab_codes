grid = [
    ['S', '.', '.'],
    ['X', '.', '.'],
    ['.', '.', 'G']
]

row = 0
column = 0

visited = []

while True:
    visited.append([row, column])
    print("Visited:", [row, column])

    
    if grid[row][column] == 'G':
        print("Goal reached!")
        break

    
    if column < 2 and grid[row][column + 1] != 'X':
        column += 1

    
    elif row < 2 and grid[row + 1][column] != 'X':
        row += 1

    else:
        print("Path not found")
        break

print("Visited Cells:", visited)