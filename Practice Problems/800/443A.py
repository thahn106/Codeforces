def main():
    string = input()[1:-1].split(', ')
    string.sort()
    count=0
    if not string[0]=='':
        count+=1
    for i in range(len(string)-1):
        if not string[i]==string[i+1]:
            count+=1
    print(count)

if __name__ == "__main__":
    main()
