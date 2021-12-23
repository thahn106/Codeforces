n = int(input())
if n%2:
    a,b  = 9, n-9
else:
    a,b = 4,n-4
print("{} {}".format(a,b))
