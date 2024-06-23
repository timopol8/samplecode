import sweeperlib
import pyglet


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
    inp1 = ' '
    inp2 = ' '
    # input and handling of shit input
    while inp1 == ' ' and inp2 == ' ':
        try:
            inp1 = int(input("Input field width: ").strip())
            inp2 = int(input("Input field height: ").strip())
        except ValueError:
            print('Please input the values again')

    # create field
    field = []
    for row2 in range(inp1):
        field.append([])
        for col in range(inp2):
            field[-1].append(" ")

    available = []
    for x in range(inp1):
        for y in range(inp2):
            available.append((x, y))

    main()
