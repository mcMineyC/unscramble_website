import constants
import re

with open('./Sharp_cipher/input.txt', 'r') as myFile:
    message = myFile.read()

#remove spaces
message = message.replace(' ', '')

#remove double rounds
doubles = re.compile('[{%s}]{2}' % constants.str_rounds)
message = doubles.sub('', message)

#find pieces
bits_regex = re.compile(f'[{constants.str_rounds}]?[{constants.str_sharps}]')
bits = bits_regex.findall(message)

#replace rounds with '0'
for index, bit in enumerate(bits):
    if len(bit) == 2: bits[index] = '0'+bit[1]

#substitute
output = ''

for bit in bits:
    output += constants.decrypted[constants.encrypted.index(bit)]

with open('./Sharp_cipher/output.txt', 'w') as myFile:
    myFile.write(output)