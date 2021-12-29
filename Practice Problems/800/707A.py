n,m = map(int,input().split())
colors = ['C', 'M', 'Y']
bw = True

for i in range(n):
    for c in input().split():
        if c in colors:
            bw = False
if bw:
    print("#Black&White")
else:
    print("#Color")
