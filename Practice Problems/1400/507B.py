import math
r, x1, y1, x2, y2 = map(int, input().split())
print(math.ceil(math.sqrt((x2-x1)**2+(y2-y1)**2)/(2*r)))
