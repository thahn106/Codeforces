ans = []
cur = 0
n = int(input())
for c in input():
    if c == 'B':
        cur +=1
    else:
        if cur:
            ans.append(cur)
        cur = 0
if cur:
    ans.append(cur)
print(len(ans))
if ans:
    print(*ans)
