s = input()
dif = 0
for i in range(len(s)//2):
    if s[i]!=s[-(i+1)]:
        dif+=1
if dif == 1 or (dif == 0 and len(s)%2):
    print("YES")
else:
    print("NO")
