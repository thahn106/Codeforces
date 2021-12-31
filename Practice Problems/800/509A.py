n = int(input())
ans = 1
den = 1
#2 is 2c1 3 is 4c2 4 is 6choose3
if n>1:
    for i in range(n-1):
        ans *= (2*(n-1)-i)
        den *= (i+1)
print(ans//den)
