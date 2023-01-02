s = input()
stack = []
a = []
b = []
cur =0
for i,c in enumerate(s):
    if c == '(':
        cur += 1
        stack.append(i)
        a.append(-1)
        b.append(-1)
    else:
        if cur == 0:
            a.append(-1)
            b.append(-1)
        else:
            cur -= 1
            t = stack.pop()
            a.append(t)
            if t>0 and s[t-1]==')' and b[t-1]>-1:
                t = b[t-1]
            b.append(t)
ans = 0
count = 1
for i,c in enumerate(s):
    if c == ')' and b[i] != -1:
        tl = i-b[i]+1
        if tl>ans:
            ans = tl
            count = 1
        elif tl == ans:
            count +=1
print(ans, count)