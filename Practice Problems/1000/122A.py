def main():
    n = int(input())
    lucky = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
    div = False
    for d in lucky:
        if n%d==0:
            div=True
    if div:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
