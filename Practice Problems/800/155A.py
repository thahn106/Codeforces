def main():
    n,  = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    maxc = nums[0]
    minc = nums[0]
    count = 0
    for i in range(1,n):
        score = nums[i]
        if score < minc:
            minc = score
            count += 1
        elif score > maxc:
            maxc = score
            count += 1
    print(count)

if __name__ == "__main__":
    main()
