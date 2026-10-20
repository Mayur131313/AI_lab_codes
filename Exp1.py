

rooms = {"A": "Dirty", "B": "Clean"}


location = "A"

while True:

    print("Current Room:", location)
    print("Room Status:", rooms[location])

    if rooms[location] == "Dirty":
        print("Action: SUCK")
        rooms[location] = "Clean"

    elif location == "A":
        print("Action: Move Right")
        location = "B"

    elif location == "B":
        print("Action: Move Left")
        location = "A"

   
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean.")
        print("Agent Stops.")
        break