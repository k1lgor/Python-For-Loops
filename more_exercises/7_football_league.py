capacity = int(input())
fans = int(input())
a = 0
b = 0
v = 0
g = 0
for i in range(1, fans + 1):
    stage = str(input())
    if stage == 'A':
        a += 1
    if stage == 'B':
        b += 1
    if stage == 'V':
        v += 1
    if stage == 'G':
        g += 1
print(f'{(a / fans * 100):.2f}%\n{(b / fans * 100):.2f}%\n{(v / fans * 100):.2f}%\n{(g / fans * 100):.2f}%\n{(fans / capacity * 100):.2f}%')
