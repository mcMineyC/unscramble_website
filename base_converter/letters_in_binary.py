#takes a string and converts each letter to five-digit binary

letters = tuple(" abcdefghijklmnopqrstuvwxyz") #includes a space at [0]

message = "Connor William Mullarky".lower()

def str_to_bin(stbInput):
    stbOutput = ""
    for letter in stbInput:
        if letter in letters:
            stbOutput += letter + "  " + str(bin(letters.index(letter)))[2:].zfill(5) + "\n"
    return stbOutput

print(str_to_bin(message))

def bin_to_str(btsInput): #TODO I don't remember if this actually works
    btsOutput = ""
    for start in range(0, len(btsInput), 5):
        setO5 = btsInput[start, start+5]
        print(setO5)

#bin_to_str(str(111110001101111011100111001111110010))