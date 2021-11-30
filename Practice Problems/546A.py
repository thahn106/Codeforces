def main():
    k,n,w = [int(x) for x in input().split()]
    cost = int(k*w*(w+1)/2)
    if cost < n:
        print(0)
    else: print(cost-n)

if __name__ == "__main__":
    main()
