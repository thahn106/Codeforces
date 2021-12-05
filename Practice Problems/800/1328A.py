def test():
    a,b = [int(x) for x in input().split()]
    ans = (-1*a)%b
    print(ans)

def main():
    t =  int(input())
    for tests in range(t):
        test()

if __name__ == "__main__":
    main()
