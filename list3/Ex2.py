sum = 0
for x in range(500):
    if x % 3 == 0 and x % 2 != 0:
        sum += x
print(sum)