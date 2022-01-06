for q in range(int(input())):
    n = int(input())
    p = list(map(int,input().split()))
    c = [0 for i in range(n)]
    for i in range(n):
        if c[i]==0:
            count = 1
            cur = i
            while p[cur]-1!=i:
                count +=1
                cur = p[cur]-1
            cur = p[cur]-1
            c[cur]=count
            while p[cur]-1!=i:
                cur = p[cur]-1
                c[cur]=count
    print(*c)
