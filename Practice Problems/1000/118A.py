def main():
    s = input().lower()
    ans = []
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char =='u' or char =='y':
            pass
        else:
            ans.append(".")
            ans.append(char)
    print("".join(ans))


if __name__ == "__main__":
    main()
