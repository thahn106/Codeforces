import math

def test():
    n = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    needed = n // 2
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            y = nums[i]
            x = nums[j]
            if y==1:
                print("{} {}".format(x,y))
                count +=1
            elif not (x%y in nums[:i]):
                print("{} {}".format(x,y))
                count +=1
            if count >= needed:
                return

def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        test()

if __name__ == "__main__":
    main()
