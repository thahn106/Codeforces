for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    B = a[1::2]
    C = a[0::2]
    odd = sum([i%2 for i in B]) % len(B)
    even = sum([i%2 for i in C]) % len(C)
    if not (odd or even):
        print("YES")
    else:
        print("NO")
