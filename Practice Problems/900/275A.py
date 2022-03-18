a = [list(map(int,input().split())) for i in range(3)]
for i in range(3):
    row = ""
    for j in range(3):
        temp = 0
        for x in range(3):
            for y in range(3):
                if abs(i-x)+abs(j-y)<2:
                    temp += a[x][y]
        row+=str((temp+1)%2)
    print(row)
