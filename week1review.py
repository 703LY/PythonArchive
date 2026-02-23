# variables

# nama1 = (input("what is your name?"))
# nama2 = (input("what is your last name?"))

# print(f"welcome to the review, {nama1} {nama2}")

# # data types
# print("You are" + " " + input("What is your age?") + " " +"years old")


# def addSuffix(num):
#     digitTerakhir = num % 10
#     if digitTerakhir == 1:
#         return f"{num}st"
#     elif digitTerakhir == 2:
#         return f"{num}nd"
#     elif digitTerakhir == 3:
#         return f"{num}rd"
#     else:
#         return f"{num}th"

# upgradeSword = 1

# while upgradeSword <= 10:
#     upgradeSword_addSuffix = addSuffix(upgradeSword)
#     print(f"you upgraded for the {upgradeSword_addSuffix} time")
#     upgradeSword += 1

# print(f"Congrats! You have upgraded your sword {upgradeSword-1} times!")

# ============tamatama ==================

import time

class Tamagotchi:
    def birth(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.alive = True
        return self
    
    def play(self):
        print(f"you played with {self.name}")
        self.happiness = min(self.happiness + 2, 10)

    def feed(self):
        print(f"you fed {self.name}")
        self.hunger = max(self.hunger -2, 0)

    def printStats(self):
        print(f"====={self.name}'s Stats ====")
        print(f"1. {self.name}'s Happiness : {self.happiness}")
        print(f"2. {self.name}'s Hunger : {self.hunger}")

    def timePass(self):
        self.hunger +=1
        self.happiness -= 1
        if self.hunger >= 10 or self.happiness <=0:
            self.alive = False

myTama = Tamagotchi().birth(input("What do you want to name Tama?"))
    
while myTama.alive:
    myTama.printStats()

    print(f"Hello! What do you want to do with {myTama.name}")
    choice1 = input("1. Feed    2. Play    3. Do Nothing")

    if choice1 == "1":
        myTama.feed()
    elif choice1 == "2":
        myTama.play()

    myTama.timePass()
    time.sleep(1)

print(f"omg {myTama.name} passed out!! game over :(")
    



