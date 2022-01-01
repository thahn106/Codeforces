n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

rd = [0]
run = 0
for i in a:
    run+=i
    rd.append(run)
i = 1
for letter in b:
    while(letter>rd[i]):
        i+=1
    print("{} {}".format(i, letter-rd[i-1]))
