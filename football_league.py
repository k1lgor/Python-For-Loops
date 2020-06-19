capacity = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
avr = 0.0
for i in range(1, fans + 1):
    sector = str(input())
    if sector == 'A':
        a += 1
    elif sector == 'B':
        b += 1
    elif sector == 'V':
        v += 1
    elif sector == 'G':
        g += 1
avr = (a + b + v + g) / capacity * 100
a = a / fans * 100
b = b / fans * 100
v = v / fans * 100
g = g / fans * 100
print(f'{a:.2f}%')
print(f'{b:.2f}%')
print(f'{v:.2f}%')
print(f'{g:.2f}%')
print(f'{avr:.2f}%')
