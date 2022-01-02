for t in range(int(input())):
    n = int(input())
    twos = 0
    threes = 0
    while not n%2:
        n=n//2
        twos +=1
    while not n%3:
        n=n//3
        threes +=1
    if n != 1 or twos>threes:
        print(-1)
    else:
        print(2*threes-twos)
