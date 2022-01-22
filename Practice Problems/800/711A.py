n = int(input())

found =  False
rows = []
for i in range(n):
    row = input()
    if not found:
        if row[0:2]=="OO":
            row = "++"+row[2:]
            found = True
        elif row[3:]=="OO":
            row = row[:3]+"++"
            found = True
    rows.append(row)

if found:
    print("YES")
    for row in rows:
        print(row)
else:
    print("NO")
