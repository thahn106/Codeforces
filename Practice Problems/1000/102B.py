n = list(map(int,list(input())))
ans = 0
while len(n)>1:
    ans +=1
    n = list(map(int,list(str(sum(n)))))
print(ans)
