import json

sharps = tuple('AEFHIKLMNTVWXYZ')
rounds = tuple('BCDGJOPQRSU')
everything = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

encrypted = ('K', 'W', '0E', '0K', 'Y', '0N', 'X', 'V', '0Y', '0L', '0V', 'I', 'H', 'M', 'E', '0F', '0Z', 'F', '0I', '0X', '0H', '0W', '0A', '0M', 'L', '0T', 'N', 'A', 'T', 'Z')
decrypted = tuple('abcdefghijklmnopqrstuvwxyz.,! ')

file_obj = open("./Sharp_cipher/frequency.json", "r")
word_sizes = json.load(file_obj)
file_obj.close()