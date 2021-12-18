n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ai = [0 for i in range(n)]
bi = [0 for i in range(n)]
for i in range(n):
    ai[a[i]-1]=i
    bi[b[i]-1]=i

d = [(ai[i]-bi[i]%n) for i in range(n)]

c = [0 for i in range(n)]

for dif in d:
    c[dif]+=1

print(max(c))
