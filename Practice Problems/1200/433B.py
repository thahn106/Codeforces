def main():
    n = int(input())
    costs = [int(x) for x in input().split()]
    m = int(input())

    sorted_costs = [x for x in costs]
    sorted_costs.sort()
    rs_costs = [0]
    rs_sorted = [0]
    rs = 0
    rss = 0
    for i in range(n):
        rs += costs[i]
        rs_costs.append(rs)
        rss += sorted_costs[i]
        rs_sorted.append(rss)
    for q in range(m):
        type, l, r = [int(x) for x in input().split()]
        if type == 1:
            print(rs_costs[r]-rs_costs[l-1])
        else:
            print(rs_sorted[r]-rs_sorted[l-1])

if __name__ == "__main__":
    main()
