for t in range(int(input())):
    n = int(input())
    for i in range(n):
        k = n-i
        print("("*k+")"*k+"("*i+")"*i)
