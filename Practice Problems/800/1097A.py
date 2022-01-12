S = input()
possible = False
b = input().split()
for a in b:
    if a[0]==S[0] or a[1]==S[1]:
        possible = True
if possible:
    print("YES")
else:
    print("NO")
