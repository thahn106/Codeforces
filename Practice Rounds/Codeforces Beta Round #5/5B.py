rows = []
try:
    while True:
        s = input()
        rows.append(s)
except EOFError as e:
    pass

M = max(map(len, rows))
la = 0 #left_adjust
ra = 1 #right_adjust
print('*'*(M+2))
for row in rows:
    es = M-len(row) # extra_spaces
    if es % 2:
        l = es // 2 + la
        r = es // 2 + ra
        la, ra = ra, la
    else:
        l = es // 2
        r = es // 2
    print('*' + ' '*l+row+' '*r+'*')
print('*'*(M+2))
