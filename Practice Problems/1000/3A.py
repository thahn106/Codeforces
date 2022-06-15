a = input()
b = input()
x1 = ord(a[0])-ord('a')
y1 = int(a[1])
x2 = ord(b[0])-ord('a')
y2 = int(b[1])

ans = []

while x1!=x2 or y1!=y2:
    t = ""
    if x1<x2:
        x1 += 1
        t+= 'R'
    elif x1>x2:
        x1 -= 1
        t+='L'
    if y1<y2:
        y1 +=1
        t+='U'
    elif y1>y2:
        y1 -= 1
        t+='D'

    ans.append(t)

print(len(ans))
for i in ans:
    print(i)
