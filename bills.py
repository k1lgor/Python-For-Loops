months = int(input())
elec = 0.0
water = 0.0
net = 0.0

for i in range(1, months + 1):
    elec_bill = float(input())
    elec += elec_bill

water = 20 * months
net = 15 * months
other = (water + elec + net) * 1.2
avr = (elec + water + net + other) / months
print(f'Electricity: {elec:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {net:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {avr:.2f} lv')