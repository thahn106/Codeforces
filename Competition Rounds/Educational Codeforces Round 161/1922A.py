import sys

input = sys.stdin.readline


for t in range(int(input())):
    N = int(input())
    A = input()
    B = input()
    C = input()

    c_invalidated = False

    for i in range(N):
        a, b, c = A[i], B[i], C[i]
        if c != a and c != b:
            c_invalidated = True
            break

    if c_invalidated:
        print("YES")
    else:
        print("NO")
