for t in range(int(input())):
    s = input()
    i = 0
    for j in range(1, len(s)-1):
        if s[j] == 'a':
            i = j
            break
    if i:
        print(s[0:i],s[i],s[i+1:])
    else:
        print(s[0], s[1:-1],s[-1])
