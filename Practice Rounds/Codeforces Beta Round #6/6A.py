a,b,c,d = sorted(list(map(int, input().split())))
if a+b >c or b+c>d:
    print("TRIANGLE")
elif a+b==c or b+c==d:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")