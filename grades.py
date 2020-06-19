students = int(input())
avr_grade = 0.0
g1 = 0.0
g2 = 0.0
g3 = 0.0
g4 = 0.0
for i in range(1, students + 1):
    grade = float(input())
    if 2 <= grade <= 2.99:
        g1 += 1
    elif 3 <= grade <= 3.99:
        g2 += 1
    elif 4 <= grade <= 4.99:
        g3 += 1
    elif 5 <= grade:
        g4 += 1
    avr_grade += grade / students
print(f'Top students: {(g4 / students * 100):.2f}%')
print(f'Between 4.00 and 4.99: {(g3 / students * 100):.2f}%')
print(f'Between 3.00 and 3.99: {(g2 / students * 100):.2f}%')
print(f'Fail: {(g1 / students * 100):.2f}%')
print(f'Average: {avr_grade:.2f}')
