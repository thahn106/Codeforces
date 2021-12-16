for t in range(int(input())):
    word = input()
    if len(word)%2==1  or word[0]==")" or word[-1]=="(":
        print("NO")
    else:
        print("YES")
