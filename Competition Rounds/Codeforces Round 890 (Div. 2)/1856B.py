import sys

input = sys.stdin.readline

for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    downcap = 0
    for x in a:
        if x == 1:
            downcap -= 1
        else:
            downcap += x-1

    if downcap >= 0 and  N > 1:
        print("YES")
    else:
        print("NO")
