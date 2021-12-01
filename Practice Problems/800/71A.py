def main():
    n = int(input())
    for i in range(n):
        word = input()
        l = len(word)
        if l > 10:
            print(word[0],len(word)-2,word[-1], sep="")
        else:
            print(word)

if __name__ == "__main__":
    main()
