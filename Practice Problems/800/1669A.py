for t in range(int(input())):
    r = int(input())
    if r>=1900:
        ans = 1
    elif r>=1600:
        ans = 2
    elif r>=1400:
        ans = 3
    else:
        ans = 4
    print(f"Division {ans}")
