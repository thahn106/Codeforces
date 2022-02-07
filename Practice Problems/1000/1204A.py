s = input()
if len(s)==1:
    print(0)
elif len(s)%2==0:
    print(len(s)//2)
else:
    if int(s[1:]):
        print(len(s)//2 +1)
    else:
        print(len(s)//2)
