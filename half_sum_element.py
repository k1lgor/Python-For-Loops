import sys

n = int(input())
maxnum = -sys.maxsize
sum = 0
for i in range(n):
    num = int(input())
    sum += num
    if num > maxnum:
        maxnum = num

sum -= maxnum
if sum == maxnum:
    print("Yes")
    print(f'Sum = {maxnum}')
else:
    print("No")
    print(f'Diff = {abs(sum - maxnum)}')
