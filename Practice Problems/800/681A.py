ans = "NO"
for n in range(int(input())):
    s, b, a = input().split()
    b = int(b)
    a = int(a)
    if b>=2400 and a>b:
        ans = "YES"
print(ans)
