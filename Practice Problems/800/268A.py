def main():
    n =  int(input())
    cc = [0 for i in range(100)]
    hosts = []
    for i in range(n):
        h,a=[int(x) for x in input().split()]
        hosts.append(h)
        cc[a-1]+=1

    count=0
    for color in hosts:
        count+=cc[color-1]
    print(count)

if __name__ == "__main__":
    main()
