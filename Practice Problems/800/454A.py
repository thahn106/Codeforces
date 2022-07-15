n = int(input())
d = n//2
for i in range(n):
    D = min(i, n-1-i)
    s = d-D
    print("*"*s+ "D"*(2*D+1) +"*"*s)
