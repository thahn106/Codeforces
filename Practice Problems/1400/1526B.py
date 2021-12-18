for t in range(int(input())):
    n = int(input())
    possible = False
    for i in range(11):
         k = n - i*111
         if k>=0 and k%11==0:
             possible=True
    if possible:
        print("YES")
    else:
        print("NO")
