n = int(input())
s = input()
ans = 0
x = 0
for i in s:
    if i=="x":
        x+=1
    else:
        if x>=3:
            ans += x-2
        x = 0
if x>=3:
    ans += x-2
x = 0

print(ans)
