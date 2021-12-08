def main():
    s = input()
    hi  = "hello"
    i=0
    for char in s:
        if i<5:
            if hi[i]==char:
                i+=1
    if i == 5:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
