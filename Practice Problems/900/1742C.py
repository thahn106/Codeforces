for t in range(int(input())):
    grid = [input() for _ in range(9)]
    if "RRRRRRRR" in grid:
        print("R")
    else:
        print("B")
