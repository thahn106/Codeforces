n,k = map(int,input().split())

cvs = []
for i in list(map(int,input().split())):
    if i not in cvs:
        if len(cvs)>=k:
            cvs.pop(0)
        cvs.append(i)

print(len(cvs))
print(*cvs[::-1])
