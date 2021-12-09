def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        arr =[int(x)-1 for x in  input()]
        dp = {0:1}
        ans=0
        run = 0
        for i in range(n):
            run+=arr[i]
            ans+=dp.get(run,0)
            dp[run]=dp.get(run,0)+1
        print(ans)

if __name__ == "__main__":
    main()
