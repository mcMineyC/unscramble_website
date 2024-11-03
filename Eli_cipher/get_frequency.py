import constants
import pprint

char_frequencies = {}
for letter in constants.message:
    if letter not in constants.char_keys:
        #print('skipping "%s"' % letter)
        continue
    if letter in char_frequencies.keys():
        char_frequencies[letter] += 1
    else:
        char_frequencies[letter] = 1

ordered_frequencies = []
for _ in range(len(constants.char_keys)): ordered_frequencies.append([])
for letter in char_frequencies:
    ordered_frequencies[char_frequencies[letter]].append(letter)
while ordered_frequencies[-1] == []:
    del ordered_frequencies[-1]
del ordered_frequencies[0]

"""
pprint.pprint(char_frequencies)
print()
pprint.pprint(ordered_frequencies)
"""

with open('Misc_projects/unscramble/Eli_cipher/message_frequencies.txt', 'w') as somefile:
    somefile.write(pprint.pformat(ordered_frequencies))