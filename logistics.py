cargo = int(input())
bus = 0
truck = 0
train = 0
ttl_tonnage = 0.0
avr = 0.0
for i in range(1, cargo + 1):
    tonnage = int(input())
    ttl_tonnage += tonnage
    if tonnage <= 3:
        bus += tonnage
    elif 4 <= tonnage <= 11:
        truck += tonnage
    elif 12 <= tonnage:
        train += tonnage
avr = (bus * 200 + truck * 175 + train * 120) / ttl_tonnage
print(f'{(avr):.2f}')
print(f'{(bus / ttl_tonnage * 100):.2f}%')
print(f'{(truck / ttl_tonnage * 100):.2f}%')
print(f'{(train / ttl_tonnage * 100):.2f}%')
