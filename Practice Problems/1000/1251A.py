for t in range(int(input())):
    s = input()
    working = [False for i in range(26)]
    cur = ""
    count = 0
    for c in s:
        if c == cur:
            count+=1
        else:
            if count%2:
                working[ord(cur)-97]=True
            cur = c
            count = 1
    if count%2:
        working[ord(cur)-97]=True

    ans=""
    for i in range(26):
        if working[i]:
            ans += chr(i+97)
    print(ans)
