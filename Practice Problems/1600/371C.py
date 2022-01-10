import sys
input = sys.stdin.readline
def get_ints(): return list(map(int, input().split()))

s = str(input())
rem = get_ints()
price = get_ints()
r = int(input())

cc = [0,0,0]

for c in s:
    if c == 'B':
        cc[0] +=1
    elif c == 'S':
        cc[1] +=1
    elif c == 'C':
        cc[2] +=1

def cost(x):
    ans = 0
    for i in range(3):
        ans += max(0, x*cc[i]-rem[i])*price[i]
    return ans

start = 0
end = 2000000000000

while start < end-1:
    mid = (start+end)//2
    c = cost(mid)
    # print("start: {} end:{} mid: {} c: {}".format(start, end, mid,c))
    if c<=r:
        start = mid
    else:
        end = mid

print(start)
