import sys

input = sys.stdin.readline


for t in range(int(input())):
    X = int(input())
    original_X = X
    X -= 1
    ans = []
    i = 1000
    while X:
        if X & 1:
            ans.append(i)
            X = (X - 1) // 2
        else:
            ans.append(-i)
            X = X - 1
        i -= 1

    ans.reverse()
    print(len(ans))
    print(*ans)
