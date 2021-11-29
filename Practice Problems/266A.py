def main():
    N = int(input())
    word = input()
    count = 0
    for i in range(N-1):
        if word[i]==word[i+1]:
            count+=1
    print(count)

if __name__ == "__main__":
    main()
