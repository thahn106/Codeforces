def binary_search(list, k):
    n = len(list)
    ref = list[k]
    start =  k
    end = n-1
    if not ref>0:
        ref = 1
        start = 0
    cut =  (end-start)//2
    if list[end] == ref:
        return end
    while(end-start>1):
        if (list[cut]<ref):
            end = cut
        else:
            start = cut
        cut =  (end+start)//2
    if list[end]<ref:
        cut = start
    else:
        cut = end
    return  cut

def main():
    n,k = input().split()
    n = int(n)
    k = int(k)-1
    scores = [int(x) for x in input().split()]
    passes =  binary_search(scores, k)
    if (scores[passes]>0):
        passes+=1
    print(passes)

if __name__ == "__main__":
    main()
