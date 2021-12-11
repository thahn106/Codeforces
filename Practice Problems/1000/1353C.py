for t in range(int(input())):
    n = int(input())
    max = (n+1)//2
    ans = 0
    for i in range(max):
        ans -= (2*i+1)*(2*i+1)
        if i+1 == max:
            ans+=(i+1)*(2*i+1)*(2*i+1)
    print(ans)
