n = int(input())
d = list(map(int,input().split()))
frun = []
run = 0
for i,x in enumerate(d):
    run += x
    frun.append((run,i+1))

d.reverse()
brun = []
run = 0
for i,x in enumerate(d):
    run += x
    brun.append((run,i+1))

frun.sort()
brun.sort()
# print(frun)
# print(brun)

ans = 0
i,j = 0,0
while i<n and j<n:
    fr,fi = frun[i]
    br,bi = brun[j]
    if fr<br:
        i+=1
    elif br<fr:
        j+=1
    else:
        if fi+bi<=n:
            ans = max(ans,fr)
        i+=1
        j+=1

print(ans)
