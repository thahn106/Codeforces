s = input()
ans = 0
for c in s:
    if c == 'a':
        ans +=1

print(min(2*ans-1, len(s)))
