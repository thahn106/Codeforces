def main():
    test_cases = int(input())
    for t in range(test_cases):
        n,x = [int(x) for x in input().split()]
        nums = [int(x) for x in input().split()]

        evens = 0
        for num in nums:
            if num % 2 ==0:
                evens +=1
        odds = n-evens
        possible = True
        if odds>0:
            odds-=1
            x-=1
            x -= 2*min(x//2, odds//2)
            if x > evens:
                possible = False                
        else:
            possible = False
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
