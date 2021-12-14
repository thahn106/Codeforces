n = int(input())
exams = []
for i in range(n):
    a,b = map(int, input().split())
    exams.append((a,b))

exams.sort()
day = 0
for exam in exams:
    a, b = exam
    if day <= b:
        day = b
    else:
        day = a
print(day)
