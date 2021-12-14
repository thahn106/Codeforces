n,t = map(int,input().split())
a = list(map(int, input().split()))
start = 0
end = 0
ans = 0
run = 0
while end <n:
    if run <= t:
        run += a[end]
        if run<=t:
            ans = max(ans, end-start+1)
        end+=1
    else:
        run -= a[start]
        start+=1
        if start>end:
            end = start
print(ans)
