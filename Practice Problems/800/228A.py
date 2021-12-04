def main():
    nums = [int(x) for x in input().split()]
    nums.sort()
    count=0
    for i in range(3):
        if nums[i]==nums[i+1]:
            count+=1
    print(count)


if __name__ == "__main__":
    main()
