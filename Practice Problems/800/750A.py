def main():
    n, k  = [int(x) for x in input().split()]
    left =240-k
    i=1
    while left > 0:
        left -= 5*i
        i+=1
    if left <0:
        i-=1
    print(min(i-1,n))


if __name__ == "__main__":
    main()
