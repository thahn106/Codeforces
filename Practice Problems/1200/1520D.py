def main():
    test_cases = int(input())
    for t in range(test_cases):
        n, = [int(x) for x in input().split()]
        nums = [int(x) for x in input().split()]
        for i in range(n):
            nums[i]-=i
        nums.sort()
        ans = 0
        cur = nums[0]
        cur_count =0
        for num in nums:
            if num == cur:
                cur_count +=1
            else:
                ans += (cur_count)*(cur_count-1)//2
                cur = num
                cur_count = 1
        ans += (cur_count)*(cur_count-1)//2
        print(int(ans))

if __name__ == "__main__":
    main()
