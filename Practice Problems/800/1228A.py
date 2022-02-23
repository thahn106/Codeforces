l,r = map(int,input().split())
found = False
for x in range(l,r+1):
    n = str(x)
    if len(n)==len(set(list(n))):
        found = True
        print(x)
        break

if not found:
    print(-1)
