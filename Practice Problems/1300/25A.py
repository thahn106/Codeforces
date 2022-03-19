n = int(input())
a = list(map(int,input().split()))

fo = 0
fe = 0
co = 0
ce = 0

for i,c in enumerate(a):
    if c%2:
        co +=1
        if not fo:
            fo = i+1
    else:
        ce +=1
        if not fe:
            fe = i+1
if ce>co:
    print(fo)
else:
    print(fe)
