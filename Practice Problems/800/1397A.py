for t in range(int(input())):
    n = int(input())
    counts = [0 for i in range(26)]
    for i in range(n):
        for c in input():
            counts[ord(c)-97]+=1
    working = True
    for c in counts:
        if c%n:
            working = False
    if working:
        print("YES")
    else:
        print("NO")
