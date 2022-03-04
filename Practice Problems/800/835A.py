s, v1, v2, t1, t2 = map(int,input().split())
a = s*v1+2*t1
b = s*v2+2*t2
if a>b:
    print("Second")
elif b>a:
    print("First")
else:
    print("Friendship")
