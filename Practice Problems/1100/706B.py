from bisect import bisect_right
n = int(input())
x = list(map(int,input().split()))
x.sort()
for q in range(int(input())):
    print(bisect_right(x,int(input())))
