import sys

for t in range(int(input())):
    n, H = map(int, sys.stdin.readline().strip().split())
    a = sorted(list(map(int, sys.stdin.readline().strip().split())))
    A = a[-1]
    B = a[-2]
    d, r = divmod(H, A+B)
    if r == 0:
        sys.stdout.write(str(2*d))
    elif r <= A:
        sys.stdout.write(str(2*d+1))
    else:
        sys.stdout.write(str(2*d+2))
    sys.stdout.write('\n')
sys.stdout.flush()
