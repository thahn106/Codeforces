n,x,y = map(int, input().split())
slopes = []
for i in range(n):
    a,b = map(int, input().split())
    if a==x:
        slopes.append("x")
    elif b==y:
        slopes.append("y")
    else:
        slopes.append((b-y)/(a-x))
print(len(set(slopes)))
