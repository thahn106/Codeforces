def main():
    n, = [int(x) for x in input().split()]
    for i in input():
        if i == "1":
            print("HARD")
            return
    print("EASY")

if __name__ == "__main__":
    main()
