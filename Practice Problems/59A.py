def main():
    word = input()
    upper = 0
    lower = 0
    for char in word:
        if ord(char)>96:
            lower+=1
        else:
            upper+=1
    if upper>lower:
        print(word.upper())
    else:
        print(word.lower())

if __name__ == "__main__":
    main()
