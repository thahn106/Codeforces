for t in range(int(input())):
    n = int(input())
    counts = [0 for i in range(n+1)]
    a = list(map(int,input().split()))
    for i in a:
        counts[i]+=1
    print(max(counts))
