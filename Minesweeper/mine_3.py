room = [
    ['N', ' ', ' ', ' ', ' '],
    ['N', 'N', 'N', 'N', ' '],
    ['N', ' ', 'N', ' ', ' '],
    ['N', 'N', 'N', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ']
]

def count_ninjas(x,y,roomi):
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
    """
    num = 0             #j - x coor; i = y coor. Starts from top left
    for i, rows in enumerate(roomi):
        if i in range(y-1, y+2):
            for j, cell in enumerate(rows):
                if j in range(x-1, x+2):
                    if cell == 'N':
                        num += 1
    return int(num)


#print room
print(" ", "- " * 5)
for row in room:
    print("|", " ".join(row), "|")
print(" ", "- " * 5)

column = int(input('Input x coordinate: '))
rowi = int(input('Input y coordinate: '))
print(f'The tile is surrounded by {count_ninjas(column, rowi, room)} ninjas')
