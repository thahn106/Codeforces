from math import ceil
for q in range(int(input())):
    n = int(input())
    print(ceil(sum(list(map(int,input().split())))/n))
