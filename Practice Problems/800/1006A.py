n = int(input())
a = list(map(int,input().split()))
print(*[ i-int(i%2==0) for i in a])
