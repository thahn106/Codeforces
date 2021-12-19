for t in range(int(input())):
    a = input()
    b = input()
    ans = len(a)+len(b)
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i:j+1] in b:
                ans = min (len(a)+len(b) - 2*(j-i+1), ans)
    print(ans)
