n = int(input())
a = list(map(int, input().split()))


reached = [0]*n
sum = 0
for i in range(n):
    sum += a[i]
    reached[i] = sum



def value(i):
    if i < 0:
        return 0
    return reached[i] - (i-1)


lo = 1
hi = 2*n

while lo < hi:
    mid = 


