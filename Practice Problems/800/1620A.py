for t in range(int(input())):
    count = 0
    for c in input():
        if c == 'N':
            count +=1
    if count !=1:
        print("YES")
    else:
        print("NO")
