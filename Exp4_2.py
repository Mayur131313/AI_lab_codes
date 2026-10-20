def tower_of_hanoi(n,source,auxiliary, destination):
    stack = []
    stack.append((n, source, auxiliary, destination))

    while stack:
        n,source,auxiliary,destination = stack.pop()
        if n==1:
            print(f"Move Disk 1 From", {source},"to",{destination})
            return
        else:
            stack.append((n-1,auxiliary,source,destination))
            stack.append((1, source, auxiliary, destination))
            stack.append((n-1, source, destination, auxiliary))


n = int(input("Enter Number of Disks : "))
tower_of_hanoi(n,"A","B","C")

count = (2 ** n) - 1 
print("Total Moves are : ",count)