myFile = open('./Pi_cipher/Pi_Digits.txt', 'r')
Pi = myFile.read()
myFile.close()

myFile = open('./Pi_cipher/input.txt', 'r')
message = myFile.read()
myFile.close()

lower_let = tuple('abcdefghijklmnopqrstuvwxyz')
upper_let = tuple('abcdefghijklmnopqrstuvwxyz'.upper())


assert len(message) <= len(Pi)

output = ''
counter = 0
for char in message:
    if char in lower_let:
        output += lower_let[(lower_let.index(char)+int(Pi[counter]))%26] #this is the magic!
        counter += 1
    elif char in upper_let:
        output += upper_let[(upper_let.index(char)+int(Pi[counter]))%26]
        counter += 1
    else:
        output += char


myFile = open('./Pi_cipher/output.txt', 'w')
myFile.write(output)
myFile.close()