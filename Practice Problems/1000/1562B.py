for t in range(int(input())):
    k = int(input())
    s = input()
    counts = [0 for i in range(10)]
    for i in s:
        counts[int(i)]+=1
    if '1' in s:
        print(1)
        print(1)
    elif '4' in s:
        print(1)
        print(4)
    elif '6' in s:
        print(1)
        print(6)
    elif '8' in s:
        print(1)
        print(8)
    elif '9' in s:
        print(1)
        print(9)
    elif '2' in s[1:]:
        print(2)
        print(s[0]+'2')
    elif '5' in s[1:]:
        print(2)
        print(s[0]+'5')
    elif counts[3]>1:
        print(2)
        print(33)
    elif counts[7]>1:
        print(2)
        print(77)
    elif counts[2] and counts[7]:
        print(2)
        print(27)
    elif counts[5] and counts[7]:
        print(2)
        print(57)
    else:
        while True:
            pass
