for t in range(int(input())):
    n = int(input())
    s = input()
    x=0
    for c in s[::-1]:
        if c==')':
            x+=1
        else:
            break
    if 2*x>n:
        print("YES")
    else:
        print("NO")
