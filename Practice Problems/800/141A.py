def main():
    chars = [0 for x in range(26)]
    word = input()
    for char in word:
        chars[ord(char)-65]+=1
    word = input()
    for char in word:
        chars[ord(char)-65]+=1
    word = input()
    for char in word:
        chars[ord(char)-65]-=1
    if max(chars)==0 and min(chars)==0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
