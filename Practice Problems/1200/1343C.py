def main():
    test_cases = int(input())
    for t in range(test_cases):
        n = int(input())
        nums = [int(x) for x in input().split()]

        pos = -1
        if nums[0]>0:
            pos = 1
        total_sum = 0
        running_max = nums[0]
        for i in range(n):
            if pos*nums[i]>0:
                running_max = max(running_max, nums[i])
            else:
                pos *= -1
                total_sum += running_max
                running_max = nums[i]
        total_sum += running_max
        print(total_sum)

if __name__ == "__main__":
    main()
