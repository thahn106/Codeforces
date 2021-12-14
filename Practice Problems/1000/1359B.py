for t in range(int(input())):
    n, m, x, y = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        row = input()
        single = row.count(".")
        double = row.count("..")
        if 2*x <= y:
            ans += single*x
        else:
            ans += double*y+(single-2*double)*x
    print(ans)
