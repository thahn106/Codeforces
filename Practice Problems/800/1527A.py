from math import log, floor
for t in range(int(input())):
    print(2**floor(log(int(input()),2))-1)
