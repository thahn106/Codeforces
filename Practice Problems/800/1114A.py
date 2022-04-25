x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

working = False
if x<=a:
    a -= x
    b += a
    if y<=b:
        b -= y
        c += b
        if z<=c:
            working = True
if working:
    print("YES")
else:
    print("NO")
