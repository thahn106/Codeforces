for t in range(int(input())):
    w,h = map(int,input().split())
    ans = 0
    for i in range(2):
        a = list(map(int,input().split()))[1:]
        ans = max(ans,h*(max(a)-min(a)))
    for i in range(2):
        a = list(map(int,input().split()))[1:]
        ans = max(ans,w*(max(a)-min(a)))
    print(ans)
