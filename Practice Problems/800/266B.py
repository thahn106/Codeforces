def main():
    n,t = [int(x) for x in input().split()]
    word = [char for char in input()]
    for time in range(t):
        i = 0
        while i < n-1:
            if word[i]=="B" and word[i+1]=="G":
                word[i]="G"
                word[i+1]="B"
                i+=1
            i+=1
    print("".join(word))

if __name__ == "__main__":
    main()
