class Kitchen:
    SOUTH = {
        "message":"You walk toward the dining room.",
        "location":5,
    }
    DOWN = {
        "message":"You open the cellar door and down a dark set of stairs.  You hear the sound of heavy breathing....",
        "location":8,
    }
    commands = {
        "EXAMINE OLIVE OIL":"The bottle is almost empty.",
        "EXAMINE OIL":"The bottle is almost empty.",
        "EXAMINE CELLAR DOOR":"Through the door you can hear low growls coming from downstairs.",
        "EXAMINE MEAT CLEAVER":"A cutting utensil...for meat.",
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
        "DOWN":DOWN,
        "EXIT DOWN":DOWN,
        "GO DOWN":DOWN,
        "ENTER CELLAR DOOR":DOWN,
        "TAKE OLIVE OIL":"You take the olive oil.",  # Add olive oil to inventory
        "TAKE OIL":"You take the olive oil.",  # Add olive oil to inventory
        "TAKE MEAT CLEAVER":"You take the meat cleaver.",  # Add meat cleaver to inventory
        "TAKE CLEAVER":"You take the meat cleaver.",  # Add meat cleaver to inventory
    }

    intro = "\nKITCHEN:\nThe kitchen is old-fashioned, devoid of most modern\nconviences.  There is a meat cleaver here.  There is a\nsmall bottle of olive oil here.  A cellar door leads down."

    # TODO: WEREWOLF: "You smell meat to the south and wolf downstairs."
    # TODO: ITEMS: Player can take OLIVE OIL and  MEAT CLEAVER
    # EXITS: SOUTH: DINING ROOM, DOWN: DARK CELLAR
