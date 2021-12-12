n,m = [int(x) for x in input().split()]
a = {}
for i in range(m):
    word1, word2 = input().split()
    if len(word2)<len(word1):
        a[word1] = word2
    else:
        a[word1] = word1
words = input().split()
output = []
for word in words:
    output.append(a[word])
print(" ".join(output))
