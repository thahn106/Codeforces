for t in range(int(input())):
    s = input()
    min = True
    ans = ""
    for c in s:
        if min:
            if c=="a":
                ans +="b"
            else:
                ans +="a"
        else:
            if c=="z":
                ans +="y"
            else:
                ans +="z"
        min = 1-min
    print(ans)
