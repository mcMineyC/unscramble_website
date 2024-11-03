#In all code, upper case letters represent English, and lower case letters correspond to symbols in the cipher

import re, pprint

letters = 'abcdefghijklmnopqrstuvwxyz'
char_keys = tuple(_ for _ in letters + '!@#$%^&*()`~-_=+[]{} ')

re.compile(r'^[A-Z]\t', re.MULTILINE)
frequency = []

with open('Eli_cipher/message.txt', 'r') as my_file:
    message = my_file.read()

'''
trash = {}
for ih in char_keys:
    trash[ih] = ''
pprint.pprint(trash)
'''

#this is not a definite list
cipher = {
 ' ': '-',
 '!': 'O', #copy error?
 '#': 'N', #copy error?
 '$': '',
 '%': '-',
 '&': ',', #double char, include space?
 '(': '-',
 ')': '-',
 '*': '-',
 '+': '-',
 '-': '-',
 '=': '-',
 '@': 'N', #copy error?
 '[': '-',
 ']': '',
 '^': '-',
 '_': '-',
 '`': '-',
 'a': 'I',
 'b': ' ',
 'c': 'W',
 'd': 'L',
 'e': 'A',
 'f': '-',
 'g': 'U',
 'h': 'Y',
 'i': 'B',
 'j': 'E',
 'k': 'V',
 'l': 'R',
 'm': 'S',
 'n': 'O',
 'o': 'C',
 'p': 'D', #D and P?
 'q': 'N',
 'r': 'T',
 's': 'M',
 't': 'G',
 'u': ':',
 'v': '-',
 'w': '-',
 'x': '-',
 'y': '-',
 'z': 'H',
 '{': '',
 '}': '',
 '~': '-'
 }

#need F, J, K, P, Q, X, Z