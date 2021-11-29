def main():
    n = int(input())
    boys = [int(x) for x in input().split()]
    m = int(input())
    girls = [int(x) for x in input().split()]

    boys.sort()
    girls.sort()

    count = 0

    i = 0
    j = 0
    while (i < n and j < m):
        b = boys[i]
        g = girls[j]
        if abs(b-g) <= 1:
            count+=1
            i += 1
            j += 1
        elif b < g:
            i +=1
        else:
            j += 1
    print(count)


if __name__ == "__main__":
    main()
