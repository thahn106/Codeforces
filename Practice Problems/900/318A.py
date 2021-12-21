n, k = map(int,input().split())
h = (n+1)//2
if k > h:
    print((k-h)*2)
else:
    print(2*(k-1)+1)
