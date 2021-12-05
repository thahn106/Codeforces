def main():
    n, = [int(x) for x in input().split()]
    can = [0 for x in range(n)]
    X = [int(x) for x in input().split()]
    for i in range(X[0]):
        can[X[i+1]-1] = 1
    X = [int(x) for x in input().split()]
    for i in range(X[0]):
        can[X[i+1]-1] = 1
    if min(can)==1:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

if __name__ == "__main__":
    main()
