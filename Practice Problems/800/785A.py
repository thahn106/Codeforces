def main():
    n = int(input())
    count = 0
    for i in range(n):
        word = input()
        if word[0] == "T":
            count+=4
        elif word[0] == "C":
            count+=6
        elif word[0] == "O":
            count+=8
        elif word[0] == "D":
            count+=12
        elif word[0] == "I":
            count+=20
    print(count)

if __name__ == "__main__":
    main()
