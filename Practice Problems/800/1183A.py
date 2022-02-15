def d(n):
    return sum(list(map(int,list(str(n)))))%4

n = int(input())
while d(n):
    n+=1
print(n)
