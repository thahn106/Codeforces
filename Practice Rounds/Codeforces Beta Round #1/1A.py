def main():
    n,m,a = [int(x) for x in input().split()]
    r = n // a
    c = m // a
    if n % a != 0:
        r+=1
    if m % a != 0:
        c+=1
    print(r*c)

if __name__ == "__main__":
    main()
