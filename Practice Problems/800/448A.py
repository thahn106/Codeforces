from math import ceil
a = sum(list(map(int,input().split())))
b = sum(list(map(int,input().split())))
n = int(input())
if ceil(a/5)+ceil(b/10)<= n:
    print("YES")
else:
    print("NO")
