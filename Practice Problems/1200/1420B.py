for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()

    ans = 0
    start = 2
    cur = 0
    for i in a:
        if i<start:
            cur+=1
        else:
            ans += (cur*(cur-1)) //2
            while start<=i:
                start*=2
            cur = 1
    ans += (cur*(cur-1))//2
    print(ans)
