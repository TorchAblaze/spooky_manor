class BilliardRoom:
    NORTH = {
        "message":"You follow the moonlight north.",
        "location":12,
    }
    SOUTH ={
        "message":"You head south to the Library.",
        "location":9,
    }
    commands = {
        "EXAMINE TABLE":"Billiard balls are scattered across the table.  It looks like a game is underway.",
        "PLAY BILLIARDS":"It would be rude to disturb the game in progress.",
        "EXAMINE POOL CUE":"It's made of fine hardwood and tipped with a blunt brass cap.",
        "USE CLEAVER ON CUE":"You hack off the brass tip and whittle the cue down until it has a sharp point.",
        "USE SHEARS ON CUE":"You hack off the brass tip and whittle the cue down until it has a sharp point.",
        "EXAMINE TROPHIES":"You see a variety of trophy animal heads, skulls, stuffed pheasants and a shaggy wolf pelt.",
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
    }

    intro = "\nBILLIARD ROOM:\nThe billiard room contains a rack of pool cues and a large\nbilliard table.  Trophy heads and stuffed animals are\nstrewn about in a grim display of hunting prowess.\nMoonlight streams in from the north."

    # In a pinch, the wolf pelt can be used to recover from the cold or to clothe Manfred.

    # TODO: ITEMS: pool cues, wolf pelt
    # TODO: USE CLEAVERS/USE SHEARS should only work if you have those things in your inventory
    # TODO: WEREWOLF: You detect fresh air from the north.
    # EXITS: NORTH: CONSERVATORY, SOUTH: LIBRARY
