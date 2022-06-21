n = int(input())
ans = [1]*6
ref = ["Power", "Time", "Space", "Soul", "Reality", "Mind"]
for i in range(n):
    s = input()
    for j, c in enumerate('pgbory'):
        if c == s[0]:
            ans[j] = 0
print(6-n)
for i in range(6):
    if ans[i]:
        print(ref[i])
