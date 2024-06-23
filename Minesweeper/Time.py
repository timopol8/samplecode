import sweeperlib

MOUSE_BUTTONS = {sweeperlib.MOUSE_LEFT : 'left', sweeperlib.MOUSE_RIGHT : 'right',
                 sweeperlib.MOUSE_MIDDLE : 'middle'}

def handle_mouse(x,y,mbutton,pressed_modifier_keys):
    """
    This function is called when a mouse button is clicked inside the game window.
    Prints the position and clicked button of the mouse to the terminal.
    """

    print(f'The {MOUSE_BUTTONS[mbutton]} mouse button was pressed at {x}, {y}')


def main():
    """
    Creates a game window and sets a handler for mouse clicks.
    Starts the game.
    """
    sweeperlib.create_window()
    sweeperlib.set_mouse_handler(handle_mouse)
    sweeperlib.start()


if __name__ == "__main__":
    main()
