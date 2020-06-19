dr = 7
period = int(input())
tr = 0
untr = 0
for i in range(1, period + 1):
    patient = int(input())
    if i % 3 == 0 and untr > tr:
        dr += 1
    if dr > patient:
        tr += patient
    else:
        untr += patient - dr
        tr += dr
print(f'Treated patients: {tr}.')
print(f'Untreated patients: {untr}.')
