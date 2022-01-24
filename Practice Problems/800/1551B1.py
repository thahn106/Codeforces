for t in range(int(input())):
    counts = [0 for i in range(26)]
    for c in input():
        counts[ord(c)-97] = min(counts[ord(c)-97]+1,2)
    print(sum(counts)//2)
