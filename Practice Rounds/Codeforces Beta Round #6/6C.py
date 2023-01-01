n = int(input())
t = list(map(int, input().split()))
A,B=0,0
a,b=0,0
i,j = 0,n-1
while i<=j:
    if A<=B:
        A += t[i]
        a += 1
        i += 1
    else:
        B += t[j]
        b += 1
        j -= 1
print(a,b)

