for t in range(int(input())):
    if t:
        _ = input()
    n, x = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())), reverse=True)

    possible = True
    for a,b in zip(A,B):
        if a+b>x:
            possible = False
    if possible:
        print("Yes")
    else:
        print("No")
