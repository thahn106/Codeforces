for t in range(int(input())):
    n = int(input())
    stack = 0
    for c in input():
        if c == "Q":
            stack += 1
        else:
            stack -= 1
            stack = max(0, stack)
    if stack:
        print("No")
    else:
        print("Yes")
