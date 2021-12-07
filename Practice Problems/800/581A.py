def main():
    a, b  = [int(x) for x in input().split()]
    dif = min(a,b)
    a-=dif
    b-=dif
    same = max(a,b)//2
    print("{} {}".format(dif,same))

if __name__ == "__main__":
    main()
