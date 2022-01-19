for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    cur = [0 for i in range(200)]
    cs = [chr(c+97) for c in cur]
    print("".join(cs))
    for i in a:
        cur[i]=1-cur[i]
        cs = [chr(c+97) for c in cur]
        print("".join(cs))
