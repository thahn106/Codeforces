first = ""
second = ""
f = 0
s = 0
for n in range(int(input())):
    team = input()
    if n==0:
        first = team
    if team == first:
        f +=1
    else:
        second = team
        s+=1        
if f>s:
    print(first)
else:
    print(second)
