for t in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    run = 0
    for num in nums:
        run -=num
        ans = max(run,ans)
    print(ans)
