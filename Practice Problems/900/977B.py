n = int(input())
s = input()
ans = s[:2]
count = 0

for a in range(26):
    for b in range(26):
        ss = chr(a+65)+chr(b+65)
        cc = 0
        for i in range(n-1):
            if s[i:i+2]==ss:
                cc+=1
        if cc>count:
            ans = ss
            count = cc
print(ans)
