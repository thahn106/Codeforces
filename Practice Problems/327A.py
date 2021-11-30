def main():
    n = int(input())
    nums =  [int(x) for x in input().split()]
    base = sum(nums)
    ans = -n
    for i in range(n):
        running = 0
        for j in range(i,n):
            if nums[j] == 0:
                running += 1
            else:
                running -= 1
            ans = max(ans, running)
    base += ans
    print(base)




if __name__ == "__main__":
    main()
