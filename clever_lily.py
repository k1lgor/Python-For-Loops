age = int(input())
wash_machine = float(input())
price_toy = int(input())
money_per_birth = 0.00
ttl_sum = 0.00
toy = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toy += 1
    else:
        money_per_birth += 10
        ttl_sum += money_per_birth - 1
ttl_sum += toy * price_toy
if ttl_sum >= wash_machine:
    print(f'Yes! {abs(ttl_sum - wash_machine):.2f}')
else:
    print(f'No! {abs(ttl_sum - wash_machine):.2f}')
