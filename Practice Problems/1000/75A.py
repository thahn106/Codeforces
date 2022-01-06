def rz(N):
    return int("".join(str(N).split("0")))

A = int(input())
B = int(input())
C = A+B
if rz(A)+rz(B)==rz(C):
    print("YES")
else:
    print("NO")
