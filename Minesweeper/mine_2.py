ANIMALS = {
    "s": "sloth",
    "d": "doggo",
    "@": "cat",
    "m": "moogle",
    "c": "chocobo"
}


field = [
    [" ", "s", " ", " ", "m"],
    [" ", "d", "@", "d", " "],
    ["c", " ", "s", "d", " "]
]


def explore_tile(animal, y, x):
    """
    Explore a tile - if there is an animal, prints the
    location and name of the animal
    """
    for key in ANIMALS:
        if key == animal:
            print(f"Tile ({x}, {y}) contains {ANIMALS[animal]}")


def explore_field(fi): 
    """
    This function explores an entire field by calling the explore_tile
    function for each tile in the field.
    """
    for x, row in enumerate(fi):
        for y, tile in enumerate(row):
            explore_tile(tile, x, y)

explore_field(field)
