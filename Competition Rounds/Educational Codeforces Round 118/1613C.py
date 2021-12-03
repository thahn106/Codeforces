import math

def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n,h = [int(x) for x in input().split()]
        hit_list = [int(x) for x in input().split()]

        time_dif = []
        for i in range(n-1):
            time_dif.append(hit_list[i+1]-hit_list[i])
        time_dif.sort()

        found = False
        if n==1:
            ans = h
            found = True
        cur = 0
        run_sum = 0
        while not found:
            if cur == n-1:
                ans = h-run_sum
                found = True
            else:
                bound = time_dif[cur]
                if h - run_sum > bound*(n-cur):
                    run_sum += bound
                    cur += 1
                else:
                    ans = math.ceil((h-run_sum) / (n-cur))
                    found = True
        print(ans)


if __name__ == "__main__":
    main()
