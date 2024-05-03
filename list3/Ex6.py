try:
    x = int(input("Type a number in your keyboard: "))
    y = 0
    z = 0
    while True:
        if y < x:
            y += 1
            z += y
        else:
            break
    print(f"Sum: {z}")
except:
    print("no")