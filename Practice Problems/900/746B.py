n = int(input())
s = input()
ans = ["0"]*n
d = n//2
if n%2:
    ans[d] = s[0]
    a = d-1
    b = d+1
    for i in range(1, n):
        if i % 2:
            ans[a] = s[i]
            a -= 1
        else:
            ans[b] = s[i]
            b += 1
else:
    a = d-1
    b = d
    for i in range(n):
        if i % 2 == 0:
            ans[a] = s[i]
            a -= 1
        else:
            ans[b] = s[i]
            b += 1

print("".join(ans))
