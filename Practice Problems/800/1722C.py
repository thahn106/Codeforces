for t in range(int(input())):
    n = int(input())
    scores = {}
    words = [input().split() for _ in range(3)]
    for i in range(3):
        for c in words[i]:
            if c in scores:
                scores[c] += 1
            else:
                scores[c] = 1
    ans = []
    ref = [0, 3, 1, 0]
    for i in range(3):
        cur = 0
        for word in words[i]:
            cur += ref[scores[word]]
        ans.append(cur)
    print(*ans)
