def main():
    n,h = [int(x) for x in input().split()]
    for x in input().split():
        if int(x)>h:
            n+=1
    print(n)

if __name__ == "__main__":
    main()
