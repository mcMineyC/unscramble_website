#takes a string and converts each letter to five-digit binary

letters = tuple(" abcdefghijklmnopqrstuvwxyz") #includes a space at [0]

message = "Billy Bob Joe".lower()

def str_to_bin(stbInput):
    stbOutput = ""
    for letter in stbInput:
        if letter in letters:
            stbOutput += letter + "  " + str(bin(letters.index(letter)))[2:].zfill(5) + "\n"
    return stbOutput

def bin_to_str(btsInput): #TODO I don't remember if this actually works
    btsOutput = ""
    for start in range(0, len(btsInput), 5):
        setO5 = btsInput[start, start+5]
        print(setO5)
