for t in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)
    print(*nums)
