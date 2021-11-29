def divs(N):
    twos = 0
    fives = 0
    while(N%2==0):
        twos += 1
        N /= 2
    while(N%5==0):
        fives += 1
        N /= 5
    return twos, fives

def main():
    n = int(input())
    # values = [[ 0 for col in range(n) ] for row in range(n)]
    prev_row = ['R'*i for i in range(n)]
    prev_values = ['R'*i for i in range(n)]
    print(prev_row)
    for i in range(n):
        row = [int(x) for x in input.split()]
        for j in range(n):
            if i





if __name__ == "__main__":
    main()
