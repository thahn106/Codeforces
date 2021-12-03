import math

err = 0.0000001

def main():
    test_cases = int(input())
    for test_case in range(test_cases):
        x1,p1 = [int(x) for x in input().split()]
        x2,p2 = [int(x) for x in input().split()]
        quantity = math.log(x1)-math.log(x2) + math.log(10)*(p1-p2)
        if quantity > err:
            print(">")
        elif -err < quantity < err:
            print("=")
        else:
            print("<")


if __name__ == "__main__":
    main()
