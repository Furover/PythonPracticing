#showing how many days a person has been alive
name = input("What's the person's name?: ")
funnyguy = True
while(funnyguy):
    try:
        age = int(input("What's your age in years? "))
        agem = int(input("What month is it (1-12)?: "))
        aged = int(input("What day is it (1-31)?: "))
        if agem < 1 or agem > 12 or aged < 1 or aged > 31 or age < 0:
            print("not funny")
        else:
            aget = (age * 365) + (agem * 30) + aged
            print(f"\nName: {name}\nYour age in days: {aget}")
        funnyguy = False
    except:
        print("not funny")