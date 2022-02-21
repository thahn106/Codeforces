ref = '01'

for t in range(int(input())):
    n = int(input())
    s = input()
    ans = n
    for i in range(2):
        left = i
        right = 1-i
        start = 0
        end = n-1
        ta = 0
        while start <= end:
            if s[start]==ref[left]:
                start +=1
                left = 1-left
            elif s[end]==ref[right]:
                end -= 1
                right = 1-right
            else:
                left = 1-left
                right = 1-right
                ta+=1
        ans = min(ta,ans)
    print(ans)
