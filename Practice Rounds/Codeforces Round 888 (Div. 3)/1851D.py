for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    valid = [0] * N
    sum = N * (N + 1) // 2
    rem = 0
    count = 0
    for i in range(N - 1):
        if i == 0:
            x = a[i]
        else:
            x = a[i] - a[i - 1]
        if x <= N and valid[x - 1] == 0:
            valid[x - 1] = 1
            count += 1
            sum -= x
        else:
            rem += x
    if (count == N - 2 and rem == sum) or (count == N - 1 and rem == 0):
        print("YES")
    else:
        print("NO")
