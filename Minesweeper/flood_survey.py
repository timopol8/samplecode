import sweeperlib

planet = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]


def draw_field():
    """
    A handler function that draws a field represented by a two-dim         ensional list
    into a game window. This function is called whenever the game engine requests
    a screen update.
    """
    field_to_draw = planet
    sweeperlib.clear_window()
    sweeperlib.draw_background()
    sweeperlib.begin_sprite_draw()

    for row_number, row in enumerate(field_to_draw):
        for column_number, key in enumerate(row):
            sweeperlib.prepare_sprite(key, column_number * 40, row_number * 40)

    sweeperlib.draw_sprites()


def main(field_to_explore):
    """
    Loads the game graphics, creates a game window, and sets a draw handler
    """
    sweeperlib.load_sprites("C:\\Users\\Timofei\\Desktop\\lovelace\\Minesweeper\\sprites")
    sweeperlib.create_window(len(field_to_explore[0])*40, len(field_to_explore)*40)
    sweeperlib.set_draw_handler(draw_field)
    sweeperlib.start()


def floodfill(field_to_explore, x0, y0):
    """
    Marks previously unknown connected areas as safe, starting from the given
    x, y coordinates.
    """
    check_list = [(x0, y0)]
    x = len(field_to_explore[0])
    y = len(field_to_explore)

    while len(check_list) > 0:
        if field_to_explore[y0][x0] == 'x':
            return
        x0, y0 = check_list.pop(-1)
        if y0 <= y and (y0 or x0 > -1) and x0 <= x and field_to_explore[y0][x0] == " ":
            field_to_explore[y0][x0] = "0"
            for i, rows in enumerate(field_to_explore):
                if i in range(y0 - 1, y0 + 2):
                    for j, cell in enumerate(rows):
                        if j in range(x0-1, x0+2) and cell == ' ':
                            check_list.append((j, i))


floodfill(planet, 5, 1)
main(planet)
