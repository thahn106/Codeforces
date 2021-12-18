for t in range(int(input())):
    n = int(input())
    r = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    ans_r = 0
    run = 0
    for ri in r:
        run+=ri
        ans_r = max(ans_r, run)
    ans_b = 0
    run = 0
    for bi in b:
        run+=bi
        ans_b = max(ans_b, run)
    print(ans_b+ans_r)
