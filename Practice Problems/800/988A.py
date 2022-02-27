n,k = list(map(int,input().split()))
a = list(map(int,input().split()))
ans = []
found = set()
for i,e in enumerate(a):
    if e not in found:
        found.add(e)
        ans.append(i+1)
if len(ans)>=k:
    print("YES")
    print(*(ans[:k]))
else:
    print("NO")
