def main():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    dx = x2-x1
    dy = y2-y1
    side = max(abs(dx),abs(dy))
    if not(abs(dx) == 0 or abs(dx)==side) or not(abs(dy) == 0 or abs(dy)==side):
        print(-1)
    else:
        if dx == 0:
            x3 = x1+side
            x4 = x2+side
            y3 = y1
            y4 = y2
        else:
            if dy == 0:
                x3 = x1
                x4 = x2
                y3 = y1+side
                y4 = y2+side
            else:
                x3 = x1
                y3 = y2
                x4 = x2
                y4 = y1
        print("{} {} {} {}".format(x3,y3,x4,y4))

if __name__ == "__main__":
    main()
