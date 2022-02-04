def divs(n,d):
    return int(n)==n and d and (n//d == n/d) and (n/d)>0

for t in range(int(input())):
    a,b,c = map(int,input().split())
    ac = 2*b-c
    bc = (a+c)/2
    cc = 2*b-a
    if divs(ac,a) or divs(bc,b) or divs(cc,c):
        print("YES")
    else:
        print("NO")
