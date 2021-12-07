def main():
    n, m = [int(x) for x in input().split()]
    for i in range(n):
        case = i%4

        if case ==0 or case == 2:
            line = ['#' for char in range(m)]
        elif case ==1:
            line = ['.' for char in range(m)]
            line[-1]='#'
        else:
            line = ['.' for char in range(m)]
            line[0]='#'
        print("".join(line))

if __name__ == "__main__":
    main()
