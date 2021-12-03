def main():
    n, = [int(x) for x in input().split()]
    rec = [int(x) for x in input().split()]
    give = [0 for x in range(n)]
    for i in range(n):
        give[rec[i]-1]=str(i+1)
    print(" ".join(give))


if __name__ == "__main__":
    main()
