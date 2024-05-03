avgslry = 0.0
avgkids = 0.0
hslry = 0.0
slry100 = 0.0

try: 
    for x in range(3):
        salary = int(input("What's your salary?"))
        kids = int(input("How many kids do you have?"))
        if salary > hslry:
            hslry = salary
        if salary <= 100:
            slry100 += 1
        avgslry += salary
        avgkids += kids
    avgslry = avgslry / 3
    avgkids = avgkids / 3
    slry100 = slry100 / 3 * 100
    print(f"Data:\nAvg Salary: {avgslry}\nAvg Kids: {avgkids}\nSalaries below USD 100: {slry100:.2f}%\nHighest salary: {hslry}")
except: 
    print("error, try again")