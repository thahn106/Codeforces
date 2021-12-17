n = int(input())
nums = input()
digits = [0 for i in range(8)]
for char in nums:
    a = int(char)
    if a ==9:
        digits[7]+=1
        digits[3]+=2
        digits[2]+=1
    elif a == 8:
        digits[7]+=1
        digits[2]+=3
    elif a == 7:
        digits[7]+=1
    elif a == 6:
        digits[5]+=1
        digits[3]+=1
    elif a == 5:
        digits[5]+=1
    elif a == 4:
        digits[3]+=1
        digits[2]+=2
    elif a == 3:
        digits[3]+=1
    elif a == 2:
        digits[2]+=1

ans = ""
for i in range(7,1,-1):
    ans += str(i)*digits[i]
print(ans)
