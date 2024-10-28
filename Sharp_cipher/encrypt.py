import constants
import random

myFile = open('./Sharp_cipher/input.txt', 'r')
message = myFile.read().lower()
myFile.close()

output = ''

#encrypt
for letter in message:
    code_letter = constants.encrypted[constants.decrypted.index(letter)]
    if len(code_letter) == 2:
#        code_letter = random.choice(constants.rounds) + code_letter[1]
        code_letter = '0' + code_letter[1]
    output += code_letter




#add bonus characters








myFile = open('./Sharp_cipher/output.txt', 'w')
myFile.write(output) #TODO fill
myFile.close()