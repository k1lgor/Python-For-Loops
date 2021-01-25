inheritage = float(input())
year = int(input())
yold = 18
for i in range(1800, year + 1):
    if i % 2 == 0:
        inheritage -= 12000
    else:
        inheritage -= 12000 + 50 * yold
    yold += 1
if inheritage < 0:
    print(f'He will need {abs(inheritage):.2f} dollars to survive.')
else:
    print(
        f'Yes! He will live a carefree life and will have {inheritage:.2f} dollars left.')
