n = int(input())
a = sorted(list(set(list(map(int, input().split())))))
if len(a)>1:
    print(a[1])
else:
    print("NO")
