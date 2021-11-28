def main():
    exp = [int(x) for x in input().split("+")]
    exp.sort()
    exp = [str(x) for x in exp]
    print("+".join(exp))

if __name__ == "__main__":
    main()
