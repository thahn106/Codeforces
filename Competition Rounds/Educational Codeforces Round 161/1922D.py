import sys

input = sys.stdin.readline


for t in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))

    monsters = {}
    for i in range(N):
        a = A[i]
        d = D[i]
        if i == 0:
            left = None
        else:
            left = i - 1
        if i == N - 1:
            right = None
        else:
            right = i + 1
        monsters[i] = [a, d, left, right]

    alive = set(range(N))
    active = set(range(N))
    deaths = [0] * N
    for i in range(N):
        next_active = set()
        cur_deaths = 0
        to_die = set()
        for j in active:
            if j not in alive:
                continue
            a, d, left, right = monsters[j]
            damage_taken = 0
            if left is not None:
                damage_taken += monsters[left][0]
            if right is not None:
                damage_taken += monsters[right][0]
            if damage_taken > d:
                to_die.add(j)
                cur_deaths += 1

        for j in to_die:
            alive.remove(j)
            a, d, left, right = monsters[j]
            if left is not None:
                monsters[left][3] = right
                next_active.add(left)
            if right is not None:
                monsters[right][2] = left
                next_active.add(right)

        deaths[i] = cur_deaths
        active = next_active
    print(*deaths)
