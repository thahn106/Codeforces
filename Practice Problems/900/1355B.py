for t in range(int(input())):
    n,a,b = map(int,input().split())
    substr = ["a"]*a
    for i in range(b):
        substr[i]=chr(i+97)
    ans = ""
    for i in range(n):
        ans+=substr[i%a]
    print(ans)
