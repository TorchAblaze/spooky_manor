class Garden:
    NORTH = {
        "message":"You follow the sound of running water to the north.",
        "location":14,
    }
    EAST = {
        "message":"You go east toward the hedge maze.",
        "location":15,
    }
    WEST = {
        "message":"You head back inside to the conservatory.",
        "location":12,
    }
    commands = {
        "EXAMINE PLANTS":"Gardening isn't your area of expertise.",  # see TODO
        "EXAMINE WOLFSBANE":"You recall it's poisonous, but rumored to have a curative effect on lycanthropes.",  # see TODO
        "EAT WOLFSBANE":"You're no expert, but you think that would kill you!",  # see TODO
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
        "EAST":EAST,
        "EXIT EAST":EAST,
        "GO EAST":EAST,
        "WEST":WEST,
        "EXIT WEST":WEST,
        "GO WEST":WEST,
    }

    intro = "\nGARDEN:\nYou are in the garden.  There are unusual plants here. A\nhedge maze is to the east.  You hear running water to the north."

    # TODO: ITEMS: Wolfsbane
    # TODO: WOLFSBANE, EAT WOLFSBANE, and EXAMINE WOLFSBANE should only be available if player read book on Herbalism
    # TODO: EXAMINE PLANTS: If the player read the book on herbalism, they will recognize one of the plants as wolfsbane.

    # TODO: WEREWOLF: Something here smells repugnant.  You detect fresh air to the west and mouldering decay to the south.
    # EXITS: NORTH: REFLECTING POOL, EAST: HEDGE MAZE, WEST: CONSERVATORY 