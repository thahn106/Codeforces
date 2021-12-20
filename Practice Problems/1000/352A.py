n = int(input())
a = list(map(int,input().split()))
fives = sum(a)//5
zeros = n-fives
if fives >= 9 and zeros>0:
    print("5"*((fives//9)*9)+"0"*zeros)
elif zeros>0:
    print("0")
else:
    print("-1")
