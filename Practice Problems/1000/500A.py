def main():
    n,t = [int(x) for x in input().split()]
    cells = [int(x) for x in input().split()]
    visited = [False for x in range(n)]
    cur = 1
    while cur <= n and not visited[cur-1]:
        visited[cur-1]=True
        if cur< n:
            cur += cells[cur-1]
    if visited[t-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
