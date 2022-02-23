for t in range(int(input())):
    s = input()
    if list(set(list(s))) == ['a']:
        print("NO")
    else:
        s = list(s)
        for i,c in enumerate(s):
            if c != 'a':
                s.insert(len(s)-i, 'a')
                print("YES")
                print("".join(s))
                break
