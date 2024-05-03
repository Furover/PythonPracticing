try:
    continued = True
    while(continued):
        age = int(input("What's the swimmer's age?: "))
        if(age < 5):
            print("Swimmer is too young!")
        elif(age <= 7):
            print("Swimmer is in group Infatile A")
        elif(age <= 11):
            print("Swimmer is in group infatile B")
        elif(age <= 13):
            print("Swimmer is in group Juvenile A")
        elif(age <= 17):
            print("Swimmer is in group Juvenile B")
        elif(age >= 18):
            print("Swimmer is in group Adult")
        question = True
        while True:
            response = input("\nContinue?(Y/N): ")
            if(response == "y" or response == "Y"):
                break
            elif(response == "N" or response == "n"):
                continued = False
                break
            else:
                print("Type again.")
except:
    print("Not funny...")