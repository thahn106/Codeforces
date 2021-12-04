def main():
    s1 = [int(x) for x in input()]
    s2 = [int(x) for x in input()]
    print("".join([str(a^b) for a,b in zip(s1,s2)]))


if __name__ == "__main__":
    main()
