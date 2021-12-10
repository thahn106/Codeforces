for t in range(int(input())):
    n = int(input())
    word = input()
    ans = 0
    run = 0
    for char in word:
        if char == ")":
            run +=1
        else:
            run -=1
        if run >0:
            ans  = max(run,ans)
    print(ans)
