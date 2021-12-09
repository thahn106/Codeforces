def main():
    s,n = [int(x) for x in input().split()]
    dragons = []
    for i in range(n):
        x,y = [int(x) for x in input().split()]
        dragons.append((x,y))
    dragons.sort()
    i=0
    while s>0 and i<n:
        x,y = dragons[i]
        i+=1
        if s>x:
            s+=y
        else:
            s = 0
    if s>0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
