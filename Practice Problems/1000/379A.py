def main():
    a,b = [int(x) for x in input().split()]
    left = 0
    count = 0
    while a:
        count +=a
        left +=a
        a,left = divmod(left, b)
    print(count)
    
if __name__ == "__main__":
    main()
