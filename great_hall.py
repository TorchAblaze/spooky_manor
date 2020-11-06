class GreatHall:
    SOUTH = {
        "message":"You head south toward the vestibule.",
        "location":3,
    }
    EAST = {
        "message":"You walk toward the east wing of the manor.  You feel as though the eyes of the people in the portrait follow you.",
        "location":9,
    }
    WEST = {
        "message":"You walk to the west wing of the manor, the old floor creaking beneath your feet",
        "location":5
    }
    UP = {
        "message":"You walk past the portraits and up the carpeted steps to the second floor.",
        "location":18,
    }
    commands = {
        "EXAMINE PAINTINGS":"You see portraits of a distinguished-looking man and a pale-skinned woman.",
        "EXAMINE MIRROR":"You can see yourself.",  # TODO: add{wearing a smoking jacket/a wolf pelt} if they are in the inventory
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
        "EAST":EAST,
        "EXIT EAST":EAST,
        "GO EAST":EAST,
        "WEST":WEST,
        "EXIT WEST":WEST,
        "UP":UP,
        "GO UP":UP,
        "EXIT UP":UP,
        "GO UP STAIRS":UP,
        "GO UP STAIRCASE":UP,
    }

    intro = "\nGREAT HALL:\nArchways lead to the east and west wings of the manor.\nThere are some oil paintings and a large mirror hanging on the wall.  A staircase leads up to the second floor.  The\nvestibule is to the south."
    
    # TODO: Add options to "examine mirror": WEREWOLF(You notice you have pointy ears, sharp teeth and hair covering most of your face.) VAMPIRE(You can't see your reflection in the mirror!)
    # EXITS: SOUTH: VESTIBULE, EAST: LIBRARY, WEST: DINING ROOM, UP: HALLWAY
