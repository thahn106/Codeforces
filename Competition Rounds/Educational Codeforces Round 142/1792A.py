for t in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    ones = 0
    for i in h:
        if i ==1:
            ones +=1
    print(n - (ones//2))
