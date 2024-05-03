try:
    x = int(input("Type a number: "))
    print(x)
    while(x < 100):
        x = x * 3
        print(x)
except:
    print("no")