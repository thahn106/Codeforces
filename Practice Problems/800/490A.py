n = int(input())
nums = list(map(int,input().split()))
a,b,c = 0,0,0
d=[]
e=[]
f=[]
for i in range(n):
    num = nums[i]
    if num==1:
        a+=1
        d.append(i+1)
    elif num==2:
        b+=1
        e.append(i+1)
    else:
        c+=1
        f.append(i+1)
m = min(a,b,c)
print(m)
for i in range(m):
    print("{} {} {}".format(d[i],e[i],f[i]))
