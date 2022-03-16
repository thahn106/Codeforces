for t in range(int(input())):
    a = int(input())
    n = 3
    found = False
    if a>=60:
        while a*n >180*(n-2):
            n+=1
    if a*n == 180*(n-2):
        print("YES")
    else:
        print("NO")
