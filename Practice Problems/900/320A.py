n = input()
i = 0
good = True
while i < len(n):
    if n[i]=="1":
        i+=1
        if i<len(n) and  n[i]=="4":
            i+=1
        if i<len(n) and n[i]=="4":
            i+=1
    else:
        good = False
        break
if good:
    print("YES")
else:
    print("NO")
