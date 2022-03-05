from xml.etree.ElementTree import XML


n = int(input())
x = list(map(int, input().split()))
e = 0
o = 0
for i in x:
    if i % 2:
        o += 1
    else:
        e += 1
print(min(e, o))
