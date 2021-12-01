def main():
    n = int(input())
    word = input()
    a = 0
    d = 0
    for char in word:
        if char =="A":
            a += 1
        else:
            d += 1
    if a>d:
        print("Anton")
    elif d>a:
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    main()
