cur = 0
ans = 0
try:
    while True:
        s = input()
        if s[0] == '+':
            cur += 1
        elif s[0] == '-':
            cur -= 1
        else:
            a = s.split(':')
            if len(a)>1:
                ans += cur*len(a[1])
except EOFError as e:
    print(ans)