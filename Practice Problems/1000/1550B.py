for t in range(int(input())):
    n,a,b = map(int, input().split())
    s = input()
    if b>=0:
        print((a+b)*len(s))
    else:
        count = 0
        for i in range(len(s)-1):
            if s[i] !=s[i+1]:
                count+=1
        print(a*len(s) + b* (((count+1)//2)+1))
