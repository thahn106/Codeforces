n = int(input())
X = True
for i in range(n):
    s = input()
    if i == 0:
        x = s[0]
        r = s[1]
    if x == r:
        X=False
    for j in range(n):
        if j == n-1-i or j == i:
            if s[j] != x:
                X = False
        else:
            if s[j] != r:
                X = False
if X:
    print("YES")
else:
    print("NO")
