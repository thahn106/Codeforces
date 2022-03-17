def fair(n):
    s = set(list(str(n)))
    for c in s:
        if c != '0':
            c = int(c)
            if n%c:
                return False
    return True

for t in range(int(input())):
    n = int(input())
    while not fair(n):
        n+=1
    print(n)
