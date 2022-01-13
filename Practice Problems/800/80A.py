p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
n,m = map(int,input().split())
yes = False
for i in range(len(p)-1):
    if p[i]==n and p[i+1]==m:
        yes = True
if yes:
    print("YES")
else:
    print("NO")
