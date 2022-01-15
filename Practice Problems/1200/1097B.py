from itertools import combinations

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

s = sum(a)
found = False
for k in range((n//2)+1):
    for ss in combinations(a,k):
        if (s-2*sum(ss))%360==0:
            found = True
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")
