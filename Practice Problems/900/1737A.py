for t in range(int(input())):
    n,k = map(int, input().split())
    counts = [0]*26
    for c in input():
        counts[ord(c)-ord('a')]+=1
    d = n//k
    ans = ""
    for i in range(k):
        t = chr(d+97)
        for j in range(d):
            if counts[j]<i+1:
                t = chr(j+97)
                break
        ans += t
    print(ans)
        