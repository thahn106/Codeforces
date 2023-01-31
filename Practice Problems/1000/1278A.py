for t in range(int(input())):
    p = sorted(list(input()))
    P = len(p)
    h = list(input())
    for l in range(len(h) - len(p) + 1):
        if sorted(h[l : l + P]) == p:
            print("YES")
            break
    else:
        print("NO")
