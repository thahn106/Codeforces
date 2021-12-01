def main():
    n,l = [int(x) for x in input().split()]
    line = [int(x) for x in input().split()]
    line.sort()
    ans = line[0]
    for i in range(n):
        if i == n-1:
            ans =  max(ans, (l-line[i]))
        else:
            ans = max(ans, (line[i+1]-line[i])/2)
    print(ans)

if __name__ == "__main__":
    main()
