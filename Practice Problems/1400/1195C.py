n = int(input())
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))

f = 0
s = 0
for i in range(n):
    f,s  = max(f,s+h1[i]),max(s,f+h2[i])
print(max(f,s))
