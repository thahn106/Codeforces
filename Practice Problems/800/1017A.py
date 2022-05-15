a = []
for i in range(int(input())):
    s = list(map(int,input().split()))
    a.append((400-sum(s),i+1))
a.sort()
for i in range(len(a)):
    if a[i][1] == 1:
        print(i+1)
        break
