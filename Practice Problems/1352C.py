def main():
    test_cases = int(input())
    for t in range(test_cases):
        n,k = [int(x) for x in input().split()]
        rem = k%(n-1)
        if rem==0:
            print((k // (n-1))*n -1)
        else:
            print((k // (n-1))*n+rem)
            
if __name__ == "__main__":
    main()
