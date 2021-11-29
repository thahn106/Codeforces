def main():
    word = input()
    charlist = [0 for i in range(26)]
    count = 0
    for char in range(len(word)):
        charlist[ord(word[char])-97] = 1
    num = sum(charlist)
    if num % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

if __name__ == "__main__":
    main()
