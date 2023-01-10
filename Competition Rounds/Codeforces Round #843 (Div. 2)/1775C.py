def solve(s = None):
    if s:
        n,x = s
    else:
        n,x = map(int, input().split())
    if n == x:
        return n

    n = bin(n)[2:]
    x = bin(x)[2:]
    if x == '0':
        return 2**len(n)

    if len(n) != len(x):
        return -1

    looking = True
    i = 0
    for a,b in zip(n,x):
        if a == '0' and b== '1':
            return -1
        if looking:
            if a == '1' and b== '0':
                looking = False
                if n[i-1] == '1':
                    return -1
            else:
                i += 1
        else:
            if b == '1':
                return -1

    r = (len(n)-i)
    ans = int(n[:i-1]+'1'+'0'*r, 2)
    return ans

for t in range(int(input())):
    print(solve())


