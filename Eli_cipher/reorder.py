import re

line_regex = re.compile('.+')

my_message = """S WHEN YOU
UBUT I WI 
OULD BE LS
LEUW I SLO
UROO_ISU L
DOWNN APBV
EN I DIREE
REB DESI  
CNI ETIUOT
RONNOC SIH"""

grid =  line_regex.findall(my_message)

def get_coord(gcX, gcY, inputGrid):
    return inputGrid[gcY][gcX]

#print(get_coord(0, 9, grid))

#assemble order:
order = []
"""
for Y in range(9, -1, -1):
    coord = [0, Y]
    for X in range(10 - Y):
        order.append((X, Y + X))"""

#order = [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(5,5),(4,5),(3,5),(2,5),(1,5),(0,5),(0,3)]
top = 4
side = 5
for thing in range(4):
    daY = top

    print('moving to the right')
    for thisX in range(side):
        order.append((thisX, daY))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))

    print('moving downward')
    for thisY in range(top, (5-top)*2):
        order.append((thisX, thisY))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))

    print('moving to the left')
    for thisX in range(side, -1, -1):
        order.append((thisX, (5-top)*2))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))


    top += 1
    side += 1





new_message = ''
for char in order:
    new_message += get_coord(char[0], char[1], grid)
print('\n' + new_message + '\n')