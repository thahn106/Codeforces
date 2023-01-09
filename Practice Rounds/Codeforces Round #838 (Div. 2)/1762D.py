import sys

input = sys.stdin.readline

def query(a,b):
    sys.stdout.write(f"? {a} {b}\n")
    sys.stdout.flush()
    return int(input())

for t in range(int(input())):
    n = int(input())
    i = 1
    j = 2
    for k in range(3,n+1):
        first = query(i,k)
        second = query(j,k)
        if first>second:
            j = k
        elif first<second:
            i = k
    sys.stdout.write(f"! {i} {j}\n")
    sys.stdout.flush()
    if int(input()) == 1:
        continue
    else:
        break