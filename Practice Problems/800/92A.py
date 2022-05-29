n, m = map(int, input().split())
i = 0
while True:
    if i+1<=m:
        m -= i+1
        i = (i+1) % n
    else:
        break
print(m)
