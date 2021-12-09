def main():
    word = input()
    FULL  = word.upper()
    FIRST = chr(ord(FULL[0])+32)+FULL[1:]
    if word==FULL:
        print(word.lower())
    elif word == FIRST:
        FIRST = FIRST.lower()
        FIRST = chr(ord(FIRST[0])-32)+FIRST[1:]
        print(FIRST)
    else:
        print(word)



if __name__ == "__main__":
    main()
