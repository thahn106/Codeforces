colors = list(map(int,input().split()))
colors.sort()
colors[2] = min(colors[2], 2*(colors[1]+colors[0]))
print(sum(colors)//3)
