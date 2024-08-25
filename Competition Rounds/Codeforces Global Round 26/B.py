for t in range(int(input())):
    x = input()
    n = len(x)
    possible = True
    if n == 1:
        possible = False
    for i, v in enumerate(x):
        if i == 0:
            if v != "1":
                possible = False
                break
        elif i == n - 1:
            if v == "9":
                possible = False
                break
        else:
            if v == "0":
                possible = False
    print("YES" if possible else "NO")
