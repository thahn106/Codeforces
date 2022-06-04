for t in range(int(input())):
    n, s = map(int, input().split())
    ans = s*25
    words = [input() for i in range(n)]
    for i in range(n-1):
        A = words[i]
        for j in range(i+1, n):
            B = words[j]
            temp = 0
            for a, b in zip(A, B):
                temp += abs(ord(a)-ord(b))
            ans = min(temp, ans)
    print(ans)
