for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    df = len(set(a))
    counts = [0]*(n+1)
    for i in a:
        counts[i]+=1
    mc = max(counts)
    print(max(min(df,mc-1),min(df-1,mc)))
