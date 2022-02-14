n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
C = A+B
found = False
for a in A:
    for b in B:
        if a+b not in C:
            print("{} {}".format(a,b))
            found = True
            break
    if found:
        break
