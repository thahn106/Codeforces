n,c = map(int,input().split())
t = list(map(int,input().split()))


run = 0
s = 0
for i in t:
    if i-s<=c:
        run+=1
    else:
        run =1
    s = i

print(run)
