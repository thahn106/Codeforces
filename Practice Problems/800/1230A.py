from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

a = list(map(int,input().split()))
s = sum(a)/2
found = False
for group in powerset(a):
    if sum(group) == s:
        found = True
        break
if found:
    print("YES")
else:
    print("NO")
