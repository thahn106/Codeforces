a = list(input())
b = list(input())
key = sorted(zip(a, b))

ans = ""
for c in input():
    if ord(c) < 64:
        ans += c
    elif ord(c) < 96:
        ans += key[ord(c)-65][1].upper()
    else:
        ans += key[ord(c)-97][1]
print(ans)
