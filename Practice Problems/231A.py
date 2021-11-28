def main():
    n = int(input())
    count = 0
    for i in range(n):
        test_list = input().split()
        test_list = [int(x) for x in test_list]
        if sum(test_list)>1:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
