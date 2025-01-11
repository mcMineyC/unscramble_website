#takes a string and converts each letter to five-digit binary

letters = tuple(" abcdefghijklmnopqrstuvwxyz") #includes a space at [0]

message = "Hello world!".lower()

for letter in message:
    if letter in letters:
        print(letter + "  " + str(bin(letters.index(letter)))[2:].zfill(5))
