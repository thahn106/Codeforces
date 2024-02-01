import sys

input = sys.stdin.readline

for t in range(int(input())):
    a, b, r = map(int, input().split())
    A = []
    B = []
    R = []
    while a or b or r:
        A.append(a % 2)
        B.append(b % 2)
        R.append(r % 2)
        a //= 2
        b //= 2
        r //= 2

    A.reverse()
    B.reverse()
    R.reverse()

    d = len(A)
    capped = True
    ans = 0
    for i in range(d):
        if A[i] == B[i]:
            if R[i] == 1:
                capped = False
            continue
        cur = 2 ** (d - 1 - i)
        if capped:
            if R[i] == 0:
                # only pick 0
                if A[i] == 1:
                    # B[i] == 0
                    ans += cur
                else:
                    # A[i] == 0, B[i] == 1
                    ans -= cur
            else:
                if A[i] == 1:
                    # B[i] == 0
                    if ans > 0:
                        # pick 1
                        ans -= cur
                    else:
                        # pick 0
                        ans += cur
                        capped = False
                else:
                    # A[i] == 0, B[i] == 1
                    if ans < 0:
                        ans += cur
                    else:
                        ans -= cur
                        capped = False
        else:
            if A[i] == 1:
                # B[i] == 0
                if ans >= 0:
                    ans -= cur
                else:
                    ans += cur
            else:
                # A[i] == 0, B[i] == 1
                if ans <= 0:
                    ans += cur
                else:
                    ans -= cur

    sys.stdout.write(str(abs(ans)) + "\n")
