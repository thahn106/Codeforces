for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    A,B = 0,0
    for x in a[0::2]:
        if not x%2:
            A+=x
    for x in a[1::2]:
        if x%2:
            B+=x
    if A>B:
        print("Alice")
    elif A==B:
        print("Tie")
    else:
        print("Bob")
