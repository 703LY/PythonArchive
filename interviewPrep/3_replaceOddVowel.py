# problem: replace odd-numbered vowels in the string with an underscore

# my solution:

# inputstring = (input(" Input String: "))

# vowels = ['a', 'i', 'u' , 'e' , 'o', 'A', 'I', 'U', 'E', 'O']
# s_split = [char for char in inputstring]
# s_new = []

# print(s_split)

# pointer1 = 0
# pointer2 = len(inputstring)-1

# while pointer1 <= pointer2:
#     if s_split[pointer1] in vowels:
#         if pointer1 % 2 == 1:
#             s_split[pointer1] = '_'
#             s_new.append(s_split[pointer1])
#             pointer1 += 1
#         else:
#             s_new.append(s_split[pointer1])
#             pointer1 += 1
#     else:
#         s_new.append(s_split[pointer1])
#         pointer1 += 1

# print(''.join(s_new))

# ======== correct solution ==========
inputstring = (input(" Input String: "))

vowels = ['a', 'i', 'u' , 'e' , 'o', 'A', 'I', 'U', 'E', 'O']
s_split = [char for char in inputstring]
s_new = []

vowel_count = 0

for char in inputstring:
    if char in vowels:
        vowel_count += 1
        if vowel_count % 2 != 0:
            s_new.append('_')
        else:
            s_new.append(char)
    else:
        s_new.append(char)

print(''.join(s_new))
