# problem: display increasing if length of each word is more than the prev

input1 = input("input word 1: ")
input2 = input("input word 2: ")
input3 = input("input word 3: ")

if len(input1) < len(input2) and len(input2) < len(input3):
        print("Increasing")
elif len(input1) > len(input2) and len(input2) > len(input3):
        print("Decreasing")
else:
    print("Neither")