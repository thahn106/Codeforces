N = int(input())
l = list(map(int,input().split()))
towers = [0  for i in range(1001)]
for h in l:
    towers[h]+=1
m = max(towers)
c = len(set(l))
print("{} {}".format(m,c))
