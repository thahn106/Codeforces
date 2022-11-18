ref = sorted(list("Timur"))
for t in range(int(input())):
    n = int(input())
    s = sorted(list(input()))
    if s == ref:
        print("YES")
    else:
        print("NO")