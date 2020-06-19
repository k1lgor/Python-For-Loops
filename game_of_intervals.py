moves = int(input())
points = 0.0
p1 = 0.0
p2 = 0.0
p3 = 0.0
p4 = 0.0
p5 = 0.0
p6 = 0.0

for i in range(moves):
    num = int(input())
    if 0 <= num <= 9:
        p1 += 1
        points += num * 0.2
    elif 10 <= num <= 19:
        p2 += 1
        points += num * 0.3
    elif 20 <= num <= 29:
        p3 += 1
        points += num * 0.4
    elif 30 <= num <= 39:
        p4 += 1
        points += 50
    elif 40 <= num <= 50:
        p5 += 1
        points += 100
    else:
        p6 += 1
        points /= 2
print(f'{points:.2f}')
print(f'From 0 to 9: {(p1 / moves * 100):.2f}%')
print(f'From 10 to 19: {(p2 / moves * 100):.2f}%')
print(f'From 20 to 29: {(p3 / moves * 100):.2f}%')
print(f'From 30 to 39: {(p4 / moves * 100):.2f}%')
print(f'From 40 to 50: {(p5 / moves * 100):.2f}%')
print(f'Invalid numbers: {(p6 / moves * 100):.2f}%')
