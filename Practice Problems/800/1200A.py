n = int(input())
a = ['0']*10
for c in input():
    if c == 'L':
        for i in range(10):
            if a[i] == '0':
                a[i] = '1'
                break
    elif c == 'R':
        for i in range(10):
            if a[9-i] == '0':
                a[9-i] = '1'
                break
    else:
        a[int(c)] = '0'
print("".join(a))
