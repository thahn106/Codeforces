n = int(input())
ans = []
for i in input():
    if i =='n':
        ans.append(1)
    elif i == 'z':
        ans.append(0)

ans.sort(reverse=True)
print(*ans)
