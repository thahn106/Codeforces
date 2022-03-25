n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())))
c = sorted(list(map(int,input().split())))

found = False
for i,e in enumerate(b):
    if a[i]!=e:
        found = True
        print(a[i])
        break
if not found:
    print(a[-1])
found = False
for i,e in enumerate(c):
    if b[i]!=e:
        found = True
        print(b[i])
        break
if not found:
    print(b[-1])
