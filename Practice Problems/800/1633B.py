for t in range(int(input())):
    s = list(input())
    o = sum(list(map(int,s)))
    z = len(s)-o
    if max(o,z)==min(o,z):
        print(max(o,z)-1)
    else:
        print(min(o,z))
