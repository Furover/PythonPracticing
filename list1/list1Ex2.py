funnyguy = True
while(funnyguy):
    try:
        age = int(input("What's your age in days? "))
        if age < 0 :
            print("not funny")
        else:
            print(f"\nYears: {(age // 365)}\nMonths: {(age % 365) // 30 }\nDays: {(age % 365) % 30 }")
        funnyguy = False
    except:
        print("not funny")