n,k = map(int,input().split())
S = list(input())
i = 0
while i<n and k:
    if i==0 and n>1:
        if int(S[i])>1:
            S[0]="1"
            k-=1
    else:
        if int(S[i])>0:
            S[i]="0"
            k-=1
    i +=1
print("".join(S))
