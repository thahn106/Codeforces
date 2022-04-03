decstart = False
curdec = False
lastup = 0
n = int(input())
a = list(map(int,input().split()))

possible = True
for i in range(1,n):
    if a[i]<a[i-1]:
        if not decstart:
            decstart = i
            curdec = True
        elif not curdec:
            possible = False
    else:
        if curdec:
            lastup = i
        curdec = False

if not decstart:
    decstart=1
    lastup=1
elif curdec:
    lastup = n

if possible and sorted(a)==a[:decstart-1]+a[decstart-1:lastup][::-1]+a[lastup:]:
    # print(sorted(a))
    # print(a[:decstart-1]+a[decstart-1:lastup][::-1]+a[lastup:])
    print("yes")
    print(decstart, lastup)
else:
    print("no")
