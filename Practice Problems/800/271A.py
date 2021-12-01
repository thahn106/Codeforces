def distinct(year):
    ys = [char for char in str(year)]
    ys.sort()
    ans = True
    for i in range(len(ys)-1):
        if ys[i]==ys[i+1]:
            ans=False
    return ans

def main():
    y = int(input())
    found = False
    while not found:
        y+=1
        found = distinct(y)
    print(y)

if __name__ == "__main__":
    main()
