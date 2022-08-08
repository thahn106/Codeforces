for t in range(int(input())):
    min = 0
    minc = "z"
    s = input()
    for i, c in enumerate(s):
        if c <= minc:
            min = i
            minc = c
    print(minc, s[:min]+s[min+1:])
