n = int(input())
a = list(map(int, input().split()))
A = []
for i,c in enumerate(a):
    A.append((c,i+1))
A.sort()
for i in range(n//2):
    print(A[i][1], A[n-1-i][1])
