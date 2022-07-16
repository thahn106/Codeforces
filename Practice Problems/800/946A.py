n = int(input())


def a(x):
    return abs(int(x))


print(sum(list(map(a, input().split()))))
