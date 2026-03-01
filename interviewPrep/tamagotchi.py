import time


# parameter is an input from the outside,
# hunger and happiness doesnt count as a parameter bc we harcoded the standard to be 5
class Tamagotchi:
    def birth(self,name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.alive = True
        return self

    def stats(self):
        print(f"\n--- {self.name}'s stats ^^--- ")
        print(f"Hunger : {self.hunger}/10 ")
        print(f"happiness : {self.happiness}/10")
        print("please dont let my hunger go to 10 ><")
        print("-----------------------------")

    def feed(self):
        print(f"you fed {self.name}")
        self.hunger -= 2
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        print(f"you played with {self.name}")
        self.happiness += 2
        if self.happiness > 10:
            self.happiness = 0
    
    def pass_time(self):
        self.hunger += 1
        self.happiness -= 1
        if self.hunger >= 10 or self.happiness<= 0:
            self.alive = False


# game logic

tama_name = input("hi, will you give me a name please?")

my_tama = Tamagotchi().birth(tama_name)


# my_tama = Tamagotchi()
# my_tama.birth(tama_name)

while my_tama.alive:
    my_tama.stats()
    print(f"what do you want to do with {my_tama.name}?")
    choice = input ("1. Feed    2. Play    3. Do Nothing: ")
    
    if choice == "1":
        my_tama.feed()
    elif choice == "2":
        my_tama.play()

    my_tama.pass_time()
    time.sleep(1)

print(f"Omg! {my_tama.name} has passed away!! please remember to feed and play with tama!!")