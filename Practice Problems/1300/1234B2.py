n,k = map(int,input().split())

count = 0
start = 0
cvs = []
di = {}
for i in list(map(int,input().split())):
    if i not in di:
        if count>=k:
            p = cvs[start]
            start+=1
            count-=1
            del di[p]
        cvs.append(i)
        di[i] = True
        count+=1
print(count)
print(*cvs[start:start+count][::-1])
