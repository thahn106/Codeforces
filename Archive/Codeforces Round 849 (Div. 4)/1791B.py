def solve():
    input()
    x, y = 0, 0
    for c in input():
        if c == "U":
            y += 1
        elif c == "D":
            y -= 1
        elif c == "R":
            x += 1
        elif c == "L":
            x -= 1

        if x == 1 and y == 1:
            return "YES"

    return "NO"


for t in range(int(input())):
    print(solve())
