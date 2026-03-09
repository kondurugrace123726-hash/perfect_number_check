
n = int(input().strip())

sum_val = 0

# find factors
for i in range(1, n):
    if n % i == 0:
        sum_val += i

# check perfect number
if sum_val == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")