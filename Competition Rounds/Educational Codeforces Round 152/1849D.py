import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0 
state = 0 # 0 nothing, 1 push, 2 pull, 3 either

for x in a:
    if x == 0:
        if state == 0:
            state = 2
        elif state == 1:
            state = 0
        elif state == 2:
            ans += 1
            state = 2
        elif state == 3:
            ans += 1
            state = 0
    elif x == 1:
        if state == 0:
            state = 3
        elif state == 1:
            state == 1
        elif state == 2:
            state = 2
        elif state == 3:
            state = 3
    elif x == 2:
        if state == 0:
            ans += 1
            state = 1
        elif state == 1:
            state = 1
        elif state == 2:
            ans += 1
            state = 1
        elif state == 3:
            ans += 1
            state = 1
if state == 2:
    ans += 1
if state == 3:
    ans += 1
print(ans)



        






