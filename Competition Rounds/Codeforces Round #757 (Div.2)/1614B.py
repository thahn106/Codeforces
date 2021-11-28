def main():
    test_cases = int(input())
    for t in range(test_cases):
        n = int(input())
        visits = input().split()
        visits = [int(x) for x in visits]
        build_list = []

        i=1
        for x in visits:
            temp = (x, i)
            i += 1
            build_list.append(temp)
        build_list.sort()
        build_list.reverse()

        dis = 0
        pos = -1
        distance = 0
        locations = [0 for tr in range(n+1)]
        for house in build_list:
            c,d =  house
            if pos == -1:
                dis += 1
            pos *= -1
            loc = pos*dis
            distance += 2*dis*c
            locations[d]=loc
        print(distance)
        print(*locations, sep=" ")

if __name__ == "__main__":
    main()
