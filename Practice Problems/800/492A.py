N = int(input())
i=0
while N >= (i+1)*(i+2)//2:
    N -= (i+1)*(i+2)//2
    i+=1
print(i)
