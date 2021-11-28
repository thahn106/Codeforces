def main():
    answer = 0
    for j in range(5):
        line=input().split()
        for i in range(5):
            if line[i] == '1':
                answer += abs(2-i)+abs(2-j)
    print(answer)

if __name__ == "__main__":
    main()
