def main():
    num = input()
    count = 0
    for char in num:
        if char == "4" or char == "7":
            count+=1

    count = str(count)
    nl = True
    for char in count:
        if not (char == "4" or char == "7"):
            nl =False

    if nl:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
