def main():
    test_cases = int(input())
    for t in range(test_cases):
        n, = [int(x) for x in input().split()]
        counts = [0 for x in range(n+1)]
        weights = [int(x) for x in input().split()]
        for w in weights:
            counts[w]+=1;
        ans = 0
        for i in range(2,2*n+1):
            cur = 0
            for j in range(max(1,i-n),(i//2)+1):
                if i == 2*j:
                    cur += counts[j]//2
                else:
                    cur += min(counts[j],counts[i-j])
                # print("w:{} 1:{} 2:{}".format(i, j, i-j))
            # print("w:{} cur:{}".format(i,cur))
            ans = max(cur,ans)
        print(ans)

if __name__ == "__main__":
    main()
