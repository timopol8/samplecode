MESSAGES = {
    "outside": "The tile is outside the field.",
    "corner": "The tile is in the corner of the field.",
    "edge": "The tile is on the edge of the field.",
    "middle": "The tile is in the middle of the field."
}

    
def print_position(pos):
    print(MESSAGES[pos])


def position_in_field(x, y, width, height):
    if x >= width or y >= height or x < 0 or y < 0:
        pos = 'outside'

    elif x == width - 1 and y == height - 1:
        pos = 'corner'
    elif x == width - 1 and y == 0:
        pos = 'corner'        
    elif x == 0 and y == height - 1:
        pos = 'corner'
    elif x == 0 and y == 0:
        pos = 'corner'   
        
    elif x in range(0, width - 1) and y == 0 or y == height - 1:
        pos = 'edge'
    elif x == 0 or x == width - 1 and y in range(0, height - 1):
        pos = 'edge'  
        
    else:
        pos = 'middle'  
        
    return pos
    
w = int(input('Input field width: '))
h = int(input('Input field height: '))
if w <= 0 or h <= 0:
    print('You cant fit a single tile on a field that small!')
else:   
    x1 = int(input('Input x coordinate: '))
    y1 = int(input('Input y coordinate: '))
    print_position(position_in_field(x1,y1, w, h))
    