import sys

input = sys.stdin.readline


def segment(i, N):
    return (N - i) * i


N, M = map(int, input().split())
A = [0] + list(map(int, input().split())) + [0]
ref = 0
total = (N * (N + 1)) // 2
for i in range(1, N + 1):
    if A[i] != A[i + 1]:
        ref += segment(i, N)
for m in range(M):
    i, val = map(int, input().split())
    if A[i] != A[i - 1]:
        ref -= segment(i - 1, N)
    if A[i] != A[i + 1]:
        ref -= segment(i, N)
    A[i] = val
    if A[i] != A[i - 1]:
        ref += segment(i - 1, N)
    if A[i] != A[i + 1]:
        ref += segment(i, N)
    print(ref + total)
