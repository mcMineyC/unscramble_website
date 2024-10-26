import random

sharps = tuple('AEFHIKLMNTVWXYZ')
rounds = tuple('BCDGJOPQRSU')
everything = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

sharps_copy = list(sharps) + list('AEFHIKLMNTVWXYZ'.lower())
random.shuffle(sharps_copy)
print(sharps_copy, len(sharps_copy))



key = ['k', 'w', 'E', 'K', 'y', 'N', 'x', 'v', 'Y', 'L', 'V', 'i', 'h', 'm', 'e', 'F', 'Z', 'f', 'I', 'X', 'H', 'W', 'A', 'M', 'l', 'T', 'n', 'a', 't', 'z']