def test():
    word = input()
    last = [-1, -1, -1]
    ans = len(word)+1
    for i in range(len(word)):
        num = int(word[i])
        last[num-1] = i
        if min(last)>=0:
            ans = min(max(last)-min(last)+1,ans)
    if ans > len(word):
        ans = 0
    print(ans)

def main():
    test_cases = int(input())
    for t in range(test_cases):
        test()

if __name__ == "__main__":
    main()
