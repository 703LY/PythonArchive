# problem: check same or different

word1, word2 = input ("word1, word2: ").split()

if(word1.capitalize() == word2.capitalize()):
    print("Same")
else:
    print("Different")