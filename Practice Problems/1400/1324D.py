n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
rel = []
for i in range(n):
    rel.append(a[i]-b[i])

rel.sort(reverse=True)
ans =0
end = n-1
for i in range(n):
    while end>i and rel[end]+rel[i]<=0:
        end -= 1
    if end>i:
        ans += end-i

print(ans)
