sum = 0
count = 0
try:
    while True:
        x = int(input("Type a number: "))
        if x >= 0:
            sum += x
            count += 1
        else:
            break
    print(f"Sum: {sum}\nAvg: {(sum / count)}\nCounted: {count}")
except:
    print(f"Sum: {sum}\nAvg: {(sum / count)}\nCounted: {count}")
