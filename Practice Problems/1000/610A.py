n = int(input())
if n%2:
    print(0)
else:
    k = n//2
    print(k//2 - int(k%2==0))
