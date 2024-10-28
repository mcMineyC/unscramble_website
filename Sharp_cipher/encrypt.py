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
        code_letter = random.choice(constants.rounds) + code_letter[1]
#        code_letter = '0' + code_letter[1]
    output += code_letter

print(len(output))


#add bonus double rounds for "fun"
for i in range(len(output), -1, -1):
    if random.randint(1, 5) == 1:
        #assert output[:i] + output[i:] == output
        output = output[:i] + random.choice(constants.rounds) + random.choice(constants.rounds) + output[i:] #inserts 2 random round chars


print(len(output))

#TODO add bonus spaces for more 'fun'



myFile = open('./Sharp_cipher/output.txt', 'w')
myFile.write(output) #TODO fill
myFile.close()