
"""
day 1 = variables
                                  .-.
     (___________________________()6 `-,
     (   ______________________   /''"`
     //\\                      //\\
  "" ""                     "" ""
"""

# ==01. basic print==
print("Hello " + input("Siapa anjing terlucu?") + " <3")

nama = input("Siapa anjing ternakal?")

print(nama + " nakal")

# ==02. calculate name length==
nama2 = input("Siapa anjing penakut?")

print(nama2 + ", " + "panjang nama: " + str(len(nama2)))

# ==03. band name generator==
print("Welcome to the Band Name Generator.")
bandname1 = input("What's the name of the city you grew up in?\n")
bandname2 = input("What's your pet's name?\n")
print("Your band name could be " + bandname1 + " " + bandname2)



"""
day 2 = data types

                                                        (\
                                                       (\_\_^__o
                                                ___     `-'/ `_/
                                               '`--\______/  |
                                          '        /         |
                                     `    .  ' `-`/.------'\^-'

"""


# ==DATA TYPES==
# string
print("Hello"[0]) 
print("Hello"[-1]) 
print("123" + "345")

# integer, float, boolean
print(123 + 345)
print(1_000_000)
print(3.14159)
print(True)
print(False)

# ===bill calculator===
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $ ")
tips = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

math = float(bill) * (1 + 0.01 * int(tips)) / int(split)   
print(f"Each person should pay: {math:.2f}")


