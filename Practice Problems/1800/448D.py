n,m,k = map(int,input().split())

def below(x):
    ans = 0
    for i in range(1,n+1):
        ans +=min(m, x//i)
    return ans >= k

start = 1
end = n*m

while(start < end):
    cur = (start+end)//2
    if below(cur):
        end = cur
    else:
        start = cur +1
print(start)
