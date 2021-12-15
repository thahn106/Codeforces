for t in range(int(input())):
    n = int(input())
    words = input().split()
    word = []
    added = False
    for i in range(n-3):
        word.append(words[i][0])
        if words[i][1]!=words[i+1][0]:
            word.append(words[i][1])
            added= True
    word.append(words[-1][0])
    word.append(words[-1][1])
    if not added:
        word.append(words[-1][1])
    print("".join(word))
