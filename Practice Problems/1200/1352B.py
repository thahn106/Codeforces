def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n, k = [int(x) for x in input().split()]
        possible = True
        if n<k:
            possible = False
        if n % 2 == 1 and (k % 2 == 0):
            possible = False
        if n%2 == 1 or (n%2 == 0 and k%2==0):
            answer = [1 for i in range(k)]
            answer[0]=n-(k-1)
        if n%2 == 0 and k%2 ==1:
            if n<2*k:
                possible=False
            else:
                answer = [2 for i in range(k)]
                answer[0]=n-2*(k-1)
        if possible:
            print("YES")
            answer = " ".join([str(x) for x in answer])
            print(answer)
        else:
            print("NO")

if __name__ == "__main__":
    main()
