#simple prompt example
name = input("What's the person's name?: ")
funnyguy = True
while(funnyguy):
    try:
        age = int(input("What year was this person born?: "))
        age = 2024 - age
        print(f"\nName: {name}\nAge: {age}")
        funnyguy = False
    except:
        print("not funny")