s = 1
n = int(input())
while n>5*s:
    n-=5*s
    s*=2
print(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"][(n-1)//s])
