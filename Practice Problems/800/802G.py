ans = False
i = 0
for c in input():
    if 'heidi'[i] == c:
        i += 1
    if i >= 5:
        ans = True
        break
if ans:
    print("YES")
else:
    print("NO")
