for t in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    p = True
    for i in range((n+1)//2):
        j = n-1-i
        if s[i]!=s[j]:
            p=False
    if not p and k>0:
        print(2)
    else:
        print(1)
