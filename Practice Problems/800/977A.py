def tanya(N):
    if N%10==0:
        return int(N/10)
    else:
        return N-1

def main():
    n, k  = [int(x) for x in input().split()]
    for i in range(k):
        n = tanya(n)
    print(n)

if __name__ == "__main__":
    main()
