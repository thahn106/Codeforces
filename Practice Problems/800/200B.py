def main():
    n, = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    total = 0
    for num in nums:
        total += num
    print(total/n)


if __name__ == "__main__":
    main()
