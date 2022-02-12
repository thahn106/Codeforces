n = int(input())
a = list(map(int,input().split()))
c = [0 for i in range(101)]
for i in a:
    c[i]+=1
print(max(c))
