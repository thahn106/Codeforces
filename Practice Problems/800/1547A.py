for t in range(int(input())):
    s = input()
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xf,yf = map(int,input().split())
    ans = abs(xa-xb)+abs(ya-yb)
    if xa==xb==xf and (ya<yf<yb or ya>yf>yb):
        ans +=2
    if ya==yb==yf and (xa<xf<xb or xa>xf>xb):
        ans +=2
    print(ans)
