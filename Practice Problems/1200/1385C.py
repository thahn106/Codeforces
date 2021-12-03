def test():
    n, = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    inc = True
    if n<=2:
        print(0)
        return
    for i in range(1,n):
        if nums[n-i-1] > nums[n-i]:
            if not inc:
                print(n-i)
                return
        elif nums[n-i-1] < nums[n-i]:
            inc = False
    print(0)
    return

def main():
    test_cases = int(input())
    for t in range(test_cases):
        test()

if __name__ == "__main__":
    main()
