import math

def main():
    a,b = [int(x) for x in input().split()]
    print(math.floor(math.log(b/a,1.5))+1)

if __name__ == "__main__":
    main()
