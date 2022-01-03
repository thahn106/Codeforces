num = [str(min(int(c),9-int(c))) for c in input()]
if num[0]== '0':
    num[0] = '9'
print("".join(num))
