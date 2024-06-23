import random
import sweeperlib


state = {
    "field": []
}


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
            print(row1,column1)

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
    sweeperlib.create_window(600, 400)
    sweeperlib.set_draw_handler(draw_field)
    sweeperlib.start()


if __name__ == "__main__":
    field = []
    for row2 in range(10):
        field.append([])
        for col in range(15):
            field[-1].append(" ")
    state["field"] = field

    available = []
    for x in range(15):
        for y in range(10):
            available.append((x, y))

    place_mines(field, available, 35)
    main()
