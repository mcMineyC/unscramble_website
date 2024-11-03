import constants

output = ''
for letter in constants.message:
    if not letter in constants.char_keys:
        output += letter
        continue
    if letter in constants.cipher.keys():
        if constants.cipher[letter] != '':
            output += constants.cipher[letter]
            continue
    output += "_"
    #output += letter

with open('./Eli_cipher/translated.txt', 'w') as afile:
    afile.write(output)