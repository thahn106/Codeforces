for t in range(int(input())):
    s = input()
    i = 0
    while i < len(s):
        if s[i] != "314159265358979323846264338327"[i]:
            break
        i += 1
    print(i)
