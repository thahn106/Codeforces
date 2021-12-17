for t in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    seta = set(a)
    if len(seta)>k:
        print(-1)
    else:
        found = set()
        i = 1
        repeat = []
        for num in a:
            if num in found:
                i+=1
            else:
                found.add(num)
                repeat.append(num)
        repeat += [1] *(k-len(repeat))
        print(len(repeat)*i)
        print(*(repeat*i))
