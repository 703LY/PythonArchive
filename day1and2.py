
"""
week 1
                                  .-.
     (___________________________()6 `-,
     (   ______________________   /''"`
     //\\                      //\\
  "" ""                     "" ""
"""

# ==01. basic print==
# print("Hello " + input("Siapa anjing terhitam?") + " <3")

# nama = input("Siapa anjing ternakal?")

# print(nama + " nakal")

# ==02. calculate name length==
# nama2 = input("Siapa anjing penakut?")

# print(nama2 + ", " + "panjang nama: " + str(len(nama2)))

# ==03. band name generator==
# print("Welcome to the Band Name Generator.")
# bandname1 = input("What's the name of the city you grew up in?\n")
# bandname2 = input("What's your pet's name?\n")
# print("Your band name could be " + bandname1 + " " + bandname2)



"""
week 2

                                                        (\
                                                       (\_\_^__o
                                                ___     `-'/ `_/
                                               '`--\______/  |
                                          '        /         |
                                     `    .  ' `-`/.------'\^-'

"""


# ==DATA TYPES==
# string
# print("Hello"[0]) 
# print("Hello"[-1]) 
# print("123" + "345")

# integer, float, boolean
# print(123 + 345)
# print(1_000_000)
# print(3.14159)
# print(True)
# print(False)

# ===bill calculator===
# print("Welcome to the tip calculator.")
# bill = input("What was the total bill? $ ")
# tips = input("What percentage tip would you like to give? 10, 12, or 15? ")
# split = input("How many people to split the bill? ")

# math = float(bill) * (1 + 0.01 * int(tips)) / int(split)   
# print(f"Each person should pay: {math:.2f}")

# ==if, elif, else==
# print("Welcome to the rollercoaster!")
# bill = 0 
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:    
#         print("Please pay $5.")
#         bill = 5
#     elif age <= 18:
#         print("Please pay $7.")
#         bill = 7
#     else:
#         print("Please pay $12.")
#         bill = 12
#     wants_photo = input("Do you want a photo taken? y or n. ")
#     if wants_photo == 'y' or wants_photo == 'Y':
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")                

# ==Practice: Ordering pizza ==
print("Welcome to nana pizza^^")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S' or size == 's':
    bill = 15
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 2
elif size == 'M' or size == 'm':
    bill = 20
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
elif size == 'L' or size == 'l':
    bill = 25
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1     
else:
    print("Invalid size selected.")

print(f"Your final bill is: ${bill}.")  

