import sys

input = sys.stdin.readline

for t in range(int(input())):
    n,k=map(int, input().split())
    a = list(map(int, input().split()))
    ans = max(a)
    for i in range(n):
        cost = 1
        target = a[i]+1
        for j in range(i+1,n):
            if a[j] < target - (j-i):
                cost += target - (j-i) - a[j]
            else:
                cap_room_cost = (k-cost) // (j-i)
                cap_room_cur= a[j] - (target - (j-i))
                target = target + min(cap_room_cost, cap_room_cur)
                cost += min(cap_room_cost, cap_room_cur)*(j-i)
                ans = max(ans, target)
            if cost > k:
                break
    print(ans)


            


