# use a for loop when u know the finish line before the start of the race. 
# use a while loop when the finish line is a mystery, and they just have to keep running until they hit a specific condition.

for i in range (5,0,4):
    print(f"{i} more bites left")

print(f"you finished eating your rice! good job!")

# ============== 
# sendokMakan = 0
# while sendokMakan < 10:
#     print(f"yummy soup! this is my {sendokMakan}st bite")
#     sendokMakan+=1

# print(f"you finished your soup in {sendokMakan} bites")

# ============== (same as above but with suffix)
def get_suffix(number):
    duaDigitTerakhir = number % 100
    if duaDigitTerakhir == 11 or duaDigitTerakhir == 12 or duaDigitTerakhir == 13:
        return f"{number}th"
    
    satuDigitTerakhir = number % 10
    if satuDigitTerakhir ==  1:
        return f"{number}st"
    elif satuDigitTerakhir == 2:
        return f"{number}nd"
    elif satuDigitTerakhir == 3:
        return f"{number}rd"
    else:
        return f"{number}th"
    
sendokMakan = 1
while sendokMakan <= 10:
    sendokMakan_plusSuffix = get_suffix(sendokMakan)
    print(f"yummy soup! this is my {sendokMakan_plusSuffix} bite")
    sendokMakan+=1

print(f"you finished your soup in {sendokMakan - 1} bites")


# =========== for loop for lists in python
inventory = ["Potion", "Bandage", "Mega Pokeball"]

for item in inventory: 
    print(f"I am carrying a {item}")

for i in range(len(inventory)):
    print(f"Slot {i} contains: {inventory[i]}")

for i, item in enumerate(inventory):
    print(f"Slot {i} contains: {item}")

