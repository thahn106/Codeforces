def main():
    n =  int(input())
    bills = [100,20,10,5,1]
    i=0
    count=0
    while n>0:
        c, n = divmod(n,bills[i])
        count += c
        i+=1
    print(count)

if __name__ == "__main__":
    main()
