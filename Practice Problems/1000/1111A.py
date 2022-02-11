def v(c):
    return c in "aeiou"

s = input()
t = input()

same = True
if len(s)==len(t):
    for i in range(len(s)):
        if v(s[i])!=v(t[i]):
            same = False
            break
else:
    same =False

if same:
    print("Yes")
else:
    print("No")
