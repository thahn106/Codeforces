def main():
    a = int(input())
    b = int(input())
    c = int(input())
    nums = []
    nums.append(a+b+c)
    nums.append(a*b*c)
    nums.append((a+b)*c)
    nums.append(a+b*c)
    nums.append(a*(b+c))
    nums.append(a*b+c)
    print(max(nums))


if __name__ == "__main__":
    main()
