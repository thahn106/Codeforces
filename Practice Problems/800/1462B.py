for t in range(int(input())):
    n = int(input())
    s = input()
    a = "2020"
    if s[:4] == a or s[:3]+s[-1:] == a or s[:2]+s[-2:]==a or s[:1]+s[-3:]==a  or s[-4:]==a:
        print("YES")
    else:
        print("NO")
