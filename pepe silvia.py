from datetime import date

namePepe = "Pepe Silvia"
species = ["human", "cow", "pig", "robot"]
datebirth = date(1993, 3, 15)
age = 28

today = date.today()
datetoday = today.strftime("%B %d, %Y")

robot = True

if robot == True: 
    actualspecies = species[3]
else:
    actualspecies = species[0]

print("My name is " + namePepe + ".")
print(f"Hello, I am {age+1} today, " + datetoday + "!")

print("I'm also a " + species[0] + "! Definitely not a " + actualspecies + ".")