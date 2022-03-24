n = int(input())
laptops = []
for i in range(n):
    a,b = map(int,input().split())
    laptops.append((a,b))
laptops.sort()
base = laptops[0][1]
found = False
for a,b in laptops:
    if b<base:
        found=True
        break
    base = b
if found:
    print("Happy Alex")
else:
    print("Poor Alex")
