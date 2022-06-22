n = int(input())
print((n*n+1)//2)
d, r = divmod(n, 2)
e = 'C.'*d+'C'*r
o = '.C'*d+'.'*r
for i in range(n):
    if i % 2:
        print(o)
    else:
        print(e)
