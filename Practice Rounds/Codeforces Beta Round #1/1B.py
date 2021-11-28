def main():
    n = int(input())
    for t in range(n):
        line=input()
        first = 0
        change = 0
        for i in range(len(line)-1):
            this = line[i]
            next = line[i+1]
            if this.isnumeric() and next.isalpha():
                change = i
            if this.isalpha() and next.isnumeric():
                if change == 0:
                    first = i
        if change != 0:
            row = line[1:change+1]
            col = line[change+2:]
            colnum = int(col)-1
            p = 1
            while not (colnum < 26**p):
                colnum -= 26**p
                p += 1
            coln = []
            for digit in range(p):
                rem = colnum % 26
                coln.append(chr(65+rem))
                colnum = colnum // 26
            coln.reverse()
            coln = "".join(coln)
            print("{}{}".format(coln,row))
        else:
            row = line[first+1:]
            rownum = int(row)

            col = line[0:first+1]
            p = len(col) -1

            colnum = 0
            for c in col:
                colnum *= 26
                colnum += ord(c)-65
            colnum += 1
            for t in range(p):
                colnum += 26 ** (t+1)
            print("R{}C{}".format(rownum,colnum))

if __name__ == "__main__":
    main()
