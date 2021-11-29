def main():
    n,m,a,b = [int(x) for x in input().split()]
    price = 0
    cheaper = False
    if (b/m) < a:
        cheaper = True
        many =  n // m
        n -= many*m
        price += many*b
        if n*a > b:
            price += b
        else:
            price += n*a
    else:
        price = n*a
    print(price)

if __name__ == "__main__":
    main()
