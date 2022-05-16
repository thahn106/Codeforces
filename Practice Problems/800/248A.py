n = int(input())
L,R = 0,0
for i in range(n):
    l,r = map(int, input().split())
    L += l
    R += r
print(min(L,n-L)+min(R,n-R))
