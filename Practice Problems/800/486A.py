def main():
    n, = [int(x) for x in input().split()]
    if n%2==0:
        print(n//2)
    else:
        print(-1*((n+1)//2))

if __name__ == "__main__":
    main()
