def main():
    n = int(input())
    m = 0
    cur = 0
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        cur += b-a
        m = max(m,cur)
    print(m)

if __name__ == "__main__":
    main()
