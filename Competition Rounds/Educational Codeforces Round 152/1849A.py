import sys

input = sys.stdin.readline


for t in range(int(input())):
    b,c,h = map(int, input().split())
    f = c+h

    ans = min(b-1, f)
    print(2*ans+1)