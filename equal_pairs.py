n = int(input())
curr_sum = 0
prev_sum = 0
diff = 0
max_diff = 0
for i in range(n):
    prev_sum = curr_sum
    curr_sum = 0
    curr_sum += int(input())
    curr_sum += int(input())
    if i != 0:
        diff = abs(curr_sum - prev_sum)
        if diff != 0 and diff > max_diff:
            max_diff = diff
if prev_sum == curr_sum or n == 1:
    print(f'Yes, value={curr_sum}')
else:
    print(f'No, maxdiff={max_diff}')