n = int(input())
if n%2:
    print(-1)
else:
    print(*[2*((i//2)+1) -(i%2) for i in range(n)])
