def main():
    n,m = [int(x) for x in input().split()]
    houses = [int(x) for x in input().split()]
    cur = 1
    steps = 0
    for house in houses:
        if house>=cur:
            steps += house-cur
        else:
            steps += (house+n-cur)
        cur = house
    print(steps)


if __name__ == "__main__":
    main()
