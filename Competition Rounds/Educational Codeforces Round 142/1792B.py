for t in range(int(input())):
    a,b,c,d = map(int, input().split())
    mood = a
    ans = a
    m = min(b,c)
    k = max(b,c)-m
    if mood:
        ans += 2*m
        pos = min(mood, k+d)
        ans += pos
        if pos < k+d:
            ans +=1
        print(ans)
    elif b+c+d:
        print(ans+1)
    