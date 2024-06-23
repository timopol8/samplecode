import random
import sweeperlib

state = {
    "field": [],
    "real_field": [],
}

MOUSE_BUTTONS = {sweeperlib.MOUSE_LEFT: 'left', sweeperlib.MOUSE_RIGHT: 'right',
                 sweeperlib.MOUSE_MIDDLE: 'middle'}


def place_mines(field_to, tiles, N):
    """
    Places N mines to a field in random tiles.
    """
    for nuu in range(N):
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


def count_ninjas(x5, y5, roomi):  # find the number
    """
    Counts the ninjas surrounding one tile in the given room and
    returns the result. The function assumes the selected tile does
    not have a ninja in it - if it does, it counts that one as well.
    """
    num = 0  # j - x coor; i = y coor. Starts from top left
    for i, rows in enumerate(roomi):
        if i in range(y5 - 1, y5 + 2):
            for j, cell in enumerate(rows):
                if j in range(x5 - 1, x5 + 2):
                    if cell == 'x':
                        num += 1
                        roomi[y5][x5] = f'{num}'
    return str(int(num))


def win_check():
    if field.count(' ') == inp_m:
        print('YOU WON, COMRADE.')
        # GOTOSTATS
        endgame()

def endgame():
    inpuuuu = str((input('Back to (M)enu? Type m :   ')).strip().lower())
    if inpuuuu == 'm':
        sweeperlib.close()
        gamemenu()


def handle_mouse(x4, y4, mbutton, pressed_modifier_keys):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    """
    #print(f'The {MOUSE_BUTTONS[mbutton]} mouse button was pressed at {x}, {y}')
    mine_counter = int(inp_m)
    click = (y4, x4)
    real_coor = (click[0] // 40, click[1] // 40)
    x_real = real_coor[1]
    y_real = real_coor[0]

    if mbutton == sweeperlib.MOUSE_LEFT:
        field[y_real][x_real] = real_field[y_real][x_real]
        if real_field[y_real][x_real] == 'x':
            for j, k in enumerate(real_field):
                for i, tile in enumerate(k):
                    if tile == 'x':
                        field[j][i] = real_field[j][i]
            print('         GAME OVER. YOU LOST.        ')
            endgame()

        if real_field[y_real][x_real] == '0':
            open_surrounding_tiles(x_real, y_real, real_field)
            win_check()

        else:
            field[y_real][x_real] = real_field[y_real][x_real]
            win_check()

    elif mbutton == sweeperlib.MOUSE_MIDDLE:
        pass

    else:           #right button
        if field[y_real][x_real] == ' ':
            field[y_real][x_real] = 'f'
            mine_counter -= 1
        elif field[y_real][x_real] == 'f':
            field[y_real][x_real] = ' '
            mine_counter += 1
        else:
            pass

def open_surrounding_tiles(x7, y7, listi):
    """
        This function is called when you open an empty tile.
        It goes through the surrounding tiles, like "count ninjas" and opens all empty tiles,
        then does the same for these opened tiles.
        """
    togo = []
    visited_empty = set()
    togo.append((x7, y7))
    field_width = len(listi[0])
    field_height = len(listi)
    while len(togo) > 0:
        tup_x, tup_y = togo.pop()
        visited_empty.add((tup_x, tup_y))
        for i in range(max(0, tup_x - 1), min(tup_x + 2, field_width)):
            for j in range(max(0, tup_y - 1), min(tup_y + 2, field_height)):
                cell = listi[j][i]
                field[j][i] = cell
                if cell == '0' and (i, j) not in visited_empty:
                    togo.append((i, j))


def explore_field(fi):
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field.
    """
    tile_to_check_inner = []

    for y3, row in enumerate(fi):
        for x3, tile in enumerate(row):
            if tile == 'x':
                pass
            elif tile == ' ':
                tile_to_check_inner.append((x3, y3))
                fi[y3][x3] = '0'
    return tile_to_check_inner


def gamemenu():

    inpu = '04'
    while not inpu.isalpha() or not inpu == 'q' and not inpu == 'p' and not inpu == 's':
        inpu = str((input('Select an option from the menu: (P)lay, (S)tats, (Q)uit: ')).strip().lower())

    if inpu == 'q':
        print('You`ve exited the game.')
        quit()
    elif inpu == 'p':
        pass
    #elif inpu == 's':
    #     ADD STATS


if __name__ == "__main__":
    print('Minesweeper. By Anatolii and Timofei.')
    gamemenu()
    # game starts

    inp_x = ' '
    inp_y = ' '
    inp_m = ' '
    while not inp_x.isdigit() or not inp_y.isdigit() or not inp_m.isdigit() or not (int(inp_m) < (int(inp_x) * int(inp_y))):
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
        count_ninjas(n[0], n[1], real_field)

    main()
    # first click
