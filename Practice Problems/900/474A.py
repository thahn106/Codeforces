
dir = input()=='R'
s = input()


def shift(c):
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    for i,x in enumerate(keyboard):
        if x == c:
            if dir:
                return (keyboard[i-1])
            else:
                return (keyboard[i+1])
ans = ""
for c in s:
    ans += shift(c)
print(ans)
