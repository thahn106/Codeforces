dict = {}
for n in range(int(input())):
    s = input()
    if s in dict:
        dict[s]+=1
        print(s+str(dict[s]))
    else:
        dict[s]=0
        print('OK')
