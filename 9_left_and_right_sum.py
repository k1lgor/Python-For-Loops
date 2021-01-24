n = int(input())
left = 0
right = 0
for i in range(n):
    nn = int(input())
    left += nn
for i in range(n):
    nn = int(input())
    right += nn
if left == right:
    print(f'Yes, sum = {left}')
else:
    print(f'No, diff = {abs(left - right)}')
