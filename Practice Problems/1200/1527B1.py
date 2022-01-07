for t in range(int(input())):
    n = int(input())
    s= input()
    z = 0
    for c in s:
        z += c=='0'
    if z == 0:
        print("DRAW")
    elif z==1 or z%2==0:
        print("BOB")
    else:
        print("ALICE")
