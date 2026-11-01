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