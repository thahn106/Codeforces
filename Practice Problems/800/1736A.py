for t in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    x = abs(sum(A) - sum(B)) + 1
    y = 0
    for a, b in zip(A, B):
        if a != b:
            y += 1
    print(min(x, y))
