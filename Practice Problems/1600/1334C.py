import sys
input = sys.stdin.buffer.readline

M = [[1000000000000, 1000000000000] for i in range(300001)]
for T in range(int(input())):
    N = int(input())
    total = 0
    ans = 1000000000000
    for i in range(N):
        M[i][0], M[i][1] = map(int,input().split())
        if i>0:
            total+= max(0, M[i][0]-M[(i-1)%N][1])
            ans = min(ans, min(M[i][0],M[(i-1)%N][1]))
    i = 0
    total+= max(0, M[i][0]-M[(i-1)%N][1])
    ans = min(ans, min(M[i][0],M[(i-1)%N][1]))
    print(total+ans)
