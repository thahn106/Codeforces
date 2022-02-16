n = int(input())
b = list(map(int,input().split()))

a= [0]*n
x= [0]*n
for i in range(n):
    if i>0:
        x[i] = max(x[i-1], a[i-1])
    a[i]=b[i]+x[i]
print(*a)
