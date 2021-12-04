def main():
    n, = [int(x) for x in input().split()]
    str = "I hate "
    even = "that I love "
    odd = "that I hate "
    for i in range(2,n+1):
        if i%2==0:
            str+=even
        else:
            str+=odd
    print(str+"it")

if __name__ == "__main__":
    main()
