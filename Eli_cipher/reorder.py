import constants
import re

line_regex = re.compile('.+')

my_message = """
B---------
GI--------
RRL-------
D AI------
M CYT-----
EDARHI----
ARRTYIE---
UMYE DCS--
OI  SYT  -
WW VIEOOA """

grid =  line_regex.findall(my_message)

def get_coord(gcX, gcY, inputGrid):
    return inputGrid[gcY][gcX]

#print(get_coord(0, 9, grid))

#assemble order:
order = []
for Y in range(9, -1, -1):
    coord = [0, Y]
    for X in range(10 - Y):
        order.append((X, Y + X))

new_message = ''
for char in order:
    new_message += get_coord(char[0], char[1], grid)
print(new_message)