def main():
    n = int(input())
    heights = [int(x) for x in input().split()]
    minh = min(heights)
    maxh = max(heights)
    minp = -1
    maxp = -1
    for i in range(n):
        if heights[i]== maxh and maxp ==-1:
            maxp = i
        if heights[n-1-i]== minh and minp ==-1:
            minp = n-1-i
    swaps = maxp + n-1-minp
    if minp<maxp:
        swaps -= 1
    print(swaps)

if __name__ == "__main__":
    main()
