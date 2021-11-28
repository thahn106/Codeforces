def main():
    test_cases =  int(input())
    for t in range(test_cases):
        param = input().split()
        param = [int(x) for x in param]
        n,l,r,k = param
        prices =  input().split()
        prices = [int(x) for x in prices]
        ok = []
        for x in prices:
            if x <= r and x >= l:
                ok.append(x)
        ok.sort()
        total = 0
        count = 0
        for x in ok:
            if total+x <= k:
                count += 1
                total += x
        print(count)

if __name__ == "__main__":
    main()
