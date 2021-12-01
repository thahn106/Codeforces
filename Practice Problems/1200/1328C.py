def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        n = int(input())
        k = input()
        one = False
        large = []
        small = []
        for char in k:
            if char=="0":
                large.append("0")
                small.append("0")
            elif char=="1":
                if one:
                    large.append("0")
                    small.append("1")
                else:
                    large.append("1")
                    small.append("0")
                    one = True
            else:
                if one:
                    large.append("0")
                    small.append("2")
                else:
                    large.append("1")
                    small.append("1")

        print("".join(large))
        print("".join(small))

if __name__ == "__main__":
    main()
