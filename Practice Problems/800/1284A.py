n,m = map(int,input().split())
a = input().split()
b = input().split()
for t in range(int(input())):
    x = int(input())-1
    print(a[x%n]+b[x%m])
