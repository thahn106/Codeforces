import sys
import random


input = sys.stdin.readline

sys.setrecursionlimit(10000)


for t in range(int(input())):
    n = int(input())
    a = [0] * (n + 1)

    query_count = 0
    curx = None

    def update(res):
        global curx
        if curx is None:
            return
        if res == "<":
            curx -= 1
        elif res == ">":
            curx += 1
        return

    def query(a):
        global query_count
        sys.stdout.write(f"? {a}\n")
        sys.stdout.flush()
        query_count += 1
        response = input().strip()
        update(response)
        return response

    def solve(indices, smallest, largest):
        # print(f"solving {indices} {smallest} {largest}")
        global curx
        if len(indices) == 0:
            return
        if len(indices) == 1:
            a[indices[0]] = smallest
            return

        ind = random.randrange(0, len(indices))
        pivot = indices[ind]
        while True:
            res = query(pivot)
            if res == "=":
                break

        smaller = []
        small_count = 0
        larger = []
        large_count = 0

        for i in indices:
            if i == pivot:
                continue
            if curx is not None:
                if curx - smallest + 1 == small_count:
                    larger.append(i)
                    large_count += 1
                    continue
                if largest - curx + 1 == large_count:
                    smaller.append(i)
                    small_count += 1
                    continue
            if query(i) == "<":
                smaller.append(i)
                small_count += 1
            else:
                larger.append(i)
                large_count += 1
            query(pivot)

        pivot_val = smallest + len(smaller)
        if curx is None:
            curx = pivot_val

        a[pivot] = pivot_val
        solve(smaller, smallest, pivot_val - 1)
        solve(larger, pivot_val + 1, largest)

    solve(list(range(1, n + 1)), 1, n)
    ans = "! " + " ".join(map(str, a[1:])) + "\n"
    sys.stdout.write(ans)
    sys.stdout.flush()
