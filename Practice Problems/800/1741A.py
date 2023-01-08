def val(s):
    c = s[-1]
    if c == 'M':
        return 0
    elif c == 'L':
        return len(s)
    else:
        return -len(s)


for t in range(int(input())):
    a, b = map(val, input().split())
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print("=")
