n, m = map(int, input().split())
d, r = divmod(n, m)
a = [d]*(m-r) + [d+1]*(r)
print(*a)
