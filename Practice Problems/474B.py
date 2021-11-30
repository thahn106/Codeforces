def find(divs,worm):
    start = 0
    end = len(divs)-1
    while (end-start>0):
        cur = (start+end)//2
        if divs[cur]<worm:
            start = cur+1
        else:
            end = cur
    return start+1


def main():
    n = int(input())
    divs = [int(x) for x in input().split()]
    for i in range(1,n):
        divs[i]+=divs[i-1]
    m = int(input())
    worms = [int(x) for x in input().split()]
    for worm in worms:
        print(find(divs, worm))

if __name__ == "__main__":
    main()
