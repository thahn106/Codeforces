n = int(input())
a = list(map(int, input().split()))
a.sort()
i = 1
for c in a:
    if i != c:
        break
    i += 1
print(i)
