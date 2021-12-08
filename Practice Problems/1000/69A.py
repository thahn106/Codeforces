def main():
    n = int(input())
    a,b,c = 0,0,0
    for i in range(n):
        x,y,z = [int(x) for x in input().split()]
        a+=x
        b+=y
        c+=z
    if a==0 and b==0 and c==0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
