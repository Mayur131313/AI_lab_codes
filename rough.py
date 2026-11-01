# EXP-1
# rooms = {"A":"Dirty" , "B":"Clean"}

# location = "B"

# while True:

#     print("Current Room:",location)
#     print("Room Status:",rooms[location])

#     if rooms[location] == "Dirty":
#         print("Action:SUCK")
#         rooms[location] = "Clean"

#     elif location == "A":
#         print("move right")
#         location = "B"

#     elif location == "B":
#         print("move left")
#         location = "A"

#     if rooms["A"] == "Clean" and rooms["B"] == "Clean":
#          print("\nboth rooms are clean")
#          print("agent stops")
#          break



# Exp-2

# grid = [
#     ['S','.','X'],
#     ['X','.','.'],
#     ['.','.','G']
# ]

# row = 0 
# column = 0

# visited = []

# while True:

#     visited.append([row,column])
#     print("Current Cell :",[row,column])

#     if grid[row][column] == "G":
#         print("Goal reached!")
#         break

#     if column < 2 and grid[row][column+1] != "X":
#         column += 1

#     elif row < 2 and grid[row+1][column] != "X":
#         row += 1

#     else:
#         print("path not found")
#         break

# print("Visited cells :", visited)

#Exp-4

# def tower_of_hanoi(n,src,aux,dest):
#     if n == 1:
#         print("Move disk 1 from",src,"to",dest)
#         return

#     tower_of_hanoi(n-1,src,dest,aux)

#     print("Move disk",n,"from",src,"to",dest)

#     tower_of_hanoi(n-1,aux,src,dest)

# n = int(input("Enter number of disks:"))

# tower_of_hanoi(n,"A","B","C")
# count = (2**n)-1

# print("Total number of moves:",count)


#Exp-6
# N = 4
# row = []

# def solve(c=0):
#     if c == N:
#         return True
#     for r in range(N):
#         if r not in row and all(abs(r - row[i]) != c - i for i in range(c)):
#             row.append(r)
#             if solve(c + 1):
#                 return True
#             row.pop()
#     return False

# solve()
# print("Solution\n")

# for r in range(N):
#     print(" ".join("Q" if row[c] == r else "." for c in range(N)))



N = 4

row = []

def solve(c=0):
    if c == N:
        return True
    for r in range(N):
        if r not in row and all(abs(r-row[i]) != c - i for i in range(c)):
            row.append(r)
            if solve(c+1):
                return True
            row.pop()
    return False

solve()
print("solution:\n")

for r in range(N):
    print(" ".join("Q" if row[c] == r else "." for c in range(N)))