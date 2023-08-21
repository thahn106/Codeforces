import sys

input = sys.stdin.readline

def ask(l,r):
    if l == r:
        return 0
    sys.stdout.write(f"? {l} {r}\n")
    sys.stdout.flush()
    x = int(input())
    if x == -1:
        exit()
    return x
def answer(x):
    sys.stdout.write(f"! {x}\n")
    sys.stdout.flush()
def find_max(l,r):
    if l == r:
        return l
    if l + 1 == r:
        if ask(l,r) == 1:
            return l
        else:
            return r
    mid = (l+r)//2
    cand_1 = find_max(l,mid)
    cand_2 = find_max(mid+1,r)
    # first check
    ans = cand_1

    if cand_1 != l:
        a = ask(l,cand_1-1)
        b = ask(l,cand_1)
        if a != b:
            ans = cand_2
    if cand_1 != r:
        a = ask(cand_1,r)
        b = ask(cand_1+1,r)
        if a - b != r-cand_1:
            ans = cand_2
    return ans    
for t in range(int(input())):
    n = int(input())
    ans = find_max(1,n)
    answer(ans)
