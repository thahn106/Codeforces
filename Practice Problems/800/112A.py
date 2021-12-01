def main():
    first = input().lower()
    second = input().lower()
    if first < second:
        print(-1)
    elif first > second:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
