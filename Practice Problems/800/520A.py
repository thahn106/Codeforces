def main():
    n =  int(input())
    word = input().upper()
    ap = [0 for i in range(26)]
    for char in word:
        ap[ord(char)-65]=1
    if min(ap)==0:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
