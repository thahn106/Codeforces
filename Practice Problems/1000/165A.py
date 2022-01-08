n = int(input())
points = []
for i in range(n):
    a,b = map(int,input().split())
    points.append((a,b))

ans = 0
for a,b in points:
    left,right,up,down = False, False, False, False
    for x,y in points:
        if a == x:
            if b<y:
                up = True
            elif b>y:
                down = True
        elif b == y:
            if a<x:
                right = True
            elif a>x:
                left = True
    if left and right and up and down:
        ans+=1
print(ans)
