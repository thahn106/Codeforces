residue = [1,2,4,5,7,8,10,11,14,16,17,19,20,22,25,26,28,29]
for t in range(int(input())):
    d, r  = divmod(int(input())-1,18)
    print(d*30+residue[r])
