ans = 0
run = 0
for n in range(int(input())):
    h,m = input().split()
    cur_time = (h,m)
    if n == 0:
        past_time = cur_time
        run = 1
    elif past_time == cur_time:
        run +=1
        ans = max(run,ans)
    else:
        past_time = cur_time
        run = 1

ans = max(run,ans)
print(ans)
