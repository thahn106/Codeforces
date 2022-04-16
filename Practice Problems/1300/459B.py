n = int(input())
b = list(map(int, input().split()))
ma = max(b)
mi = min(b)
mac = 0
mic = 0
for i in b:
    if i == ma:
        mac += 1
    if i == mi:
        mic += 1
if ma-mi:
    print(ma-mi, mac*mic)
else:
    print(0, mac*(mac-1)//2)
