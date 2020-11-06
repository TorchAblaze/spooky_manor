class DiningRoom:
    NORTH = {
        "message":"You head north to leave the dining room.",
        "location":7,
    }
    SOUTH =  {
        "message":"You walk south out of the dining room.",
        "location":6,
    }
    EAST = {
        "message":"You head east back to the Great Hall.",
        "location":4,
    }
    commands = {
        "EXAMINE PHEASANT":"The meat looks to be cold and unappetizing.",
        "TAKE PHEASANT":"You ponder carrying around a whole roast pheasant and decide against it.",
        "TAKE DRUMSTICK":"It's still attached.",
        "USE CLEAVER ON PHEASANT":"You hack off one of the drumsticks to carry around with you, county fair-style.",
        "EAT DRUMSTICK":"You're not hungry.",
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
        "EAST":EAST,
        "EXIT EAST":EAST,
        "GO EAST":EAST,
    }

    intro = "\nDINING ROOM:\nThe dining room contains a long banquet table.  A whole\nroast pheasant, complete with drumsticks, rests in the\ncenter of the table.  Exits are to the north, south and east."

    # TODO: WEREWOLF: "You smell wolf to the north and smoke to the\nsouth.  The meat on the table smells delicious!"
    # TODO: Player can only carry one drumstick at a time
    # TODO: Drumsticks can be eaten by werewolf players
    # TODO: USE CLEAVER ON PHEASANT can only work if player has cleaver in their inventory and EAT DRUMSTICK should only work if player cut the pheasant with cleaver and/or has DRUMSTICK already in their inventory
    # TODO: Player should be allowed to TAKE DRUMSTICK if they used the cleaver on the phesant
    # TODO: There are only two drumsticks in this game. After they are succesfully eaten, they should no longer be available.
    # EXITS: NORTH: KITCHEN, SOUTH: LOUNGE, EAST: GREAT HALL