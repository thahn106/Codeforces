n,M = map(int, input().split())

def fac(n):
    ans = 1
    for i in range(n):
        ans = (ans*(i+1))%1000000000007
    return ans

## AAAAA BBBBB CCCCC
# All sorted 1, 0 moves

#1 move cases: C in C, sorted, A in A, sorted, both

# A only in A, sorted, 2n! - 1, 1 move
# A only in A or B, (2nCn), C only in C:
fn = fac(n)
ftn = fac(2*n)
tncn = (ftn//fn)//fn #2nCn


print(fac(6))

ans = 3*(fac(3*n))-1*((tncn-1)*fn*(ftn-fn) + (fac(2*n)-fac(n)*fac(n))*(fac(n)-1)+(tncn-1)*fac(n)*(ftn-1)+(fac(n)-1)*(fac(2*n)-1)+(fn-1)*(ftn-fn))-2*(ftn-fn*fn+(fn-1)*fn+ftn-1)-3
print(ans)