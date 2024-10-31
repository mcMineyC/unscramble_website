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
#zig zag pattern
for Y in range(9, -1, -1):
    coord = [0, Y]
    for X in range(10 - Y):
        order.append((X, Y + X))"""

"""
#staple pattern
top = 4
side = 5
for thing in range(5):

    print('moving to the right')
    for thisX in range(side):
        order.append((thisX, top))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))

    print('moving downward')
    for thisY in range(top, 9-top):
        order.append((side, thisY))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))

    print('moving to the left')
    for thisX in range(side, -1, -1):
        order.append((thisX, 9-top))
        print('    ' + str(order[-1]) + get_coord(order[-1][0], order[-1][1], grid))

    top -= 1
    side += 1"""

#spiral pattern
coord = {'x':4,'y':4}#start position
#spiral kickstart
order.append((coord['x'], coord['y']))#center
order.append((coord['x'], coord['y']+1))#move down 1
#order.append((coord['x']-1, coord['y']-1))#move left 1
coord['x'] -= 1
coord['y'] += 1

size = 1
for _ in range(4):
    size += 1
    #up
    for daY in range(coord['y'], coord['y']-size, -1):
        order.append((coord['x'],daY))
    coord['y'] -= size
    #right
    for daX in range(coord['x'], coord['x']+size):
        order.append((daX, coord['y']))
    coord['x'] += size
    size += 1
    #down
    for daY in range(coord['y'], coord['y']+size):
        order.append((coord['x'],daY))
    coord['y'] += size
    #left
    for daX in range(coord['x'], coord['x']-size, -1):
        order.append((daX, coord['y']))
    coord['x'] -= size



print(order)

new_message = ''
for char in order:
    new_message += get_coord(char[0], char[1], grid)
print('\n' + new_message + '\n')