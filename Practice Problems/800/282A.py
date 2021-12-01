def main():
    n = int(input())
    num = 0
    for op in range(n):
        line = input()
        if line[1] == '+':
            num+=1
        else:
            num-=1
    print(num)

if __name__ == "__main__":
    main()
