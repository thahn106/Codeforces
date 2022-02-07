for t in range(int(input())):
    n = int(input())
    s = input()
    twos = []
    for i in range(n):
        if s[i]=="2":
            twos.append(i)
    if len(twos)==1 or len(twos)==2:
        print("NO")
    else:
        adj =[]
        for i in range(len(twos)):
            adj.append((twos[i],twos[(i+1)%len(twos)]))
        print("YES")
        for i in range(n):
            row = ""
            for j in range(n):
                if i==j:
                    row+="X"
                else:
                    if (i,j) in adj:
                        row+="+"
                    elif (j,i) in adj:
                        row+="-"
                    else:
                        row+='='
            print(row)
