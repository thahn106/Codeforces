for t in range(int(input())):
    ans = 0
    for _ in range(2):
        ans += sum(list(map(int, input().split())))
    if ans == 4:
        print(2)
    elif ans:
        print(1)
    else:
        print(0)
