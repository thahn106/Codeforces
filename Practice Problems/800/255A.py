n = int(input())
a = list(map(int,input().split()))
ch = sum(a[0::3])
bi = sum(a[1::3])
ba = sum(a[2::3])

if ch>bi and ch>ba:
    print("chest")
elif bi>ba:
    print("biceps")
else:
    print("back")
