import random

# ====random number from 1 to 100===
# randomInteger = random.randint(1, 100) 
# print (randomInteger)

heads_or_tails = random.randint(0, 1)

if heads_or_tails == 1:
    print("heads")
else:
    print("tails")