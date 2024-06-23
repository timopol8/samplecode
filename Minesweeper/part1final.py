#draw field(put mines, cover up, non mine tiles have numbers(count mines))


import random
import sweeperlib


state = {
    "field": [],
    "real_field" : [],
}

MOUSE_BUTTONS = {sweeperlib.MOUSE_LEFT : 'left', sweeperlib.MOUSE_RIGHT : 'right',
                 sweeperlib.MOUSE_MIDDLE : 'middle'}


def place_mines(field_to, tiles, N):
    """
    Places N mines to a field in random tiles.
    """
    for n in range(N):
        (column1, row1) = random.choice(tiles)
        try:
            while field_to[row1][column1] == 'x':
                (column1, row1) = random.choice(tiles)
        except IndexError:
            print("\n")

        tiles.remove((column1, row1))
        field_to[row1][column1] = 'x'
    return field_to


def draw_field():
    """
    A handler function that draws a field represented by a two-dimensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    field_to_draw = state["field"]
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()

    for row_number, row in enumerate(field_to_draw):
        for column_number, key in enumerate(row):
            sweeperlib.prepare_sprite(key, column_number * 40, row_number * 40)

    sweeperlib.draw_sprites()


def main():
    """
    Loads the game graphics, creates a game window and sets a draw handler for it.
    """
    sweeperlib.load_sprites('C:\\Users\\Timofei\\Desktop\\lovelace\\Minesweeper\\sprites')
    sweeperlib.create_window(inp_x * 40, inp_y * 40)
    sweeperlib.set_draw_handler(draw_field)
    sweeperlib.set_mouse_handler(handle_mouse)
    sweeperlib.start()


def count_ninjas(x,y,roomi): #find the number
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
                    if cell == 'x':
                        num += 1
                        roomi[x][y] = num
    return str(int(num))

def handle_mouse(x,y,mbutton,pressed_modifier_keys):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    """
    #print(f'The {MOUSE_BUTTONS[mbutton]} mouse button was pressed at {x}, {y}')

    click = (x,y)
    real_coor = (click[0]//40, click[1]//40)
    #print(real_coor)
    # which button
    if mbutton == sweeperlib.MOUSE_LEFT:

        #lose if mine
        if real_field[real_coor[1]][real_coor[0]] == 'x':
            field[real_coor[1]][real_coor[0]] = 'x'
            print('\nYOU LOST.')
            quit()
            # ADD go bACK TO MENU
            #ADD STOP THE GAME

        #open tile. #show numbers too
        elif real_field[real_coor[1]][real_coor[0]] == '0':
            field[real_coor[1]][real_coor[0]] = '0'

            #create list of surroundings
            # ADD open adjacent if empty
        else:
            field[real_coor[1]][real_coor[0]] = real_field[real_coor[0]][real_coor[1]]


    print(field)
    # elif mbutton == MOUSE_BUTTONS['right']:         #flag square?? use state["real_field"]


def explore_field(fi):
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field.
    """
    tile_to_check = []

    for x, row in enumerate(fi):
        for y, tile in enumerate(row):
                if tile == 'x':
                    pass
                elif tile != 'x':
                    tile_to_check.append([x,y])

    return tile_to_check


if __name__ == "__main__":
    print('Minesweeper. By Anatolii and Timofei.')
    # print('Select an option from the menu: ')
    # # inpu = str((input('(P)lay, (S)tats, (Q)uit: ')).strip().lower())
    # # if inpu == 'q':
    # #     quit()
    # # elif inpu == 'p':
    # #     pass
    # # elif inpu == 's':
    # #     #ADD STATS
    # #     pass

    #game starts

    inp_x = ' '
    inp_y = ' '
    inp_m = ' '
    while not inp_x.isdigit() or not inp_y.isdigit() or not inp_m.isdigit():
        try:
            print('Please input field dimensions.')
            inp_x = input("Input field width: ").strip()
            inp_y = input("Input field height: ").strip()
            inp_m = input("Input number of mines: ").strip()

        except ValueError:
            print('Please input the values again')
        except TypeError:
            print('Please input the values again')

    # create field
    field = []
    state["field"] = field
    inp_x = int(inp_x)
    inp_y = int(inp_y)
    inp_m = int(inp_m)
    for row2 in range(inp_y):
        field.append([])
        for col in range(inp_x):
            field[-1].append(" ")

    real_field = []
    state["real_field"] = real_field
    inp_x = int(inp_x)
    inp_y = int(inp_y)
    inp_m = int(inp_m)
    for row2 in range(inp_y):
        real_field.append([])
        for col in range(inp_x):
            real_field[-1].append(" ")

    available = []
    for x in range(inp_y):
        for y in range(inp_x):
            available.append((x, y))


    place_mines(real_field, available, inp_m)
    tile_to_check = explore_field(real_field)
    # ninjas (find the number for each empty tile)
    for n in tile_to_check:
        num_on_tile = count_ninjas(n[0], n[1], real_field)
        real_field[n[1]][n[0]] = f'{num_on_tile}'

    print(field)

    main()
    #first click

