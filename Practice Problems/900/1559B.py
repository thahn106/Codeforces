for t in range(int(input())):
    n = int(input())
    s = list(input())
    first = "B"
    for i, c in enumerate(s):
        if c != "?":
            if i % 2:
                first = "R" if c == "B" else "B"
            else:
                first = c
            break
    for i, c in enumerate(s):
        if c == "?":
            if i:
                if s[i - 1] == "B":
                    s[i] = "R"
                else:
                    s[i] = "B"
            else:
                s[i] = first

    print("".join(s))
