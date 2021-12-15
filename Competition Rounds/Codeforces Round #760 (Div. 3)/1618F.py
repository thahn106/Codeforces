x,y = map(int, input().split())
if x == y:
    print("YES")
else:
    # while y%4 == 3:
    #     y = (y-1)//2
    # if y%2 == 1:
    #     y = int(bin(y)[2:][::-1],2)
    #     while y%4 == 3:
    #         y = (y-1)//2
    bx1 = int(bin(x)[2:][::-1],2)
    bx2 = int(bin(bx1)[2:][::-1],2)
    bx3 = int(bin(x)[2:]+"1",2)
    bx4 = int(bin(bx3)[2:][::-1],2)
    bx1 = bin(bx1)[2:]
    bx2 = bin(bx2)[2:]
    bx3 = bin(bx3)[2:]
    bx4 = bin(bx4)[2:]
    # print(bin(y))
    # print("BXi")
    # print(bx1)
    # print(bx2)
    # print(bx3)
    # print(bx4)

    found = False
    if not found and bx1 in bin(y)[2:]:
        temp = bin(y)[2:]
        temp = temp.replace(bx1,"")
        found =True
        for char in temp:
            if char !="1":
                found = False
    if not found and bx2 in bin(y)[2:]:
        temp = bin(y)[2:]
        temp = temp.replace(bx2,"")
        found =True
        for char in temp:
            if char !="1":
                found = False
    if not found and bx3 in bin(y)[2:]:
        temp = bin(y)[2:]
        temp = temp.replace(bx3,"")
        found = True
        for char in temp:
            if char != "1":
                found = False
    if not found and bx4 in bin(y)[2:]:
        temp = bin(y)[2:]
        temp = temp.replace(bx4,"")
        found =True
        for char in temp:
            if char !="1":
                found = False
    if found:
        print("YES")
    else:
        print("NO")
