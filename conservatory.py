class Conservatory:
    SOUTH = {
        "message":"You head south back to the billiard room.",
        "location":11,
    }
    EAST = {
        "message":"You walk through the open set of glass double doors into the crisp night air.",
        "location":13,
    }
    commands = {
        "EXAMINE SKY":"The rain has stopped and a full moon is out.",
        "LOOK OUTSIDE":"You see the garden, a fountain and a hedge maze.",
        "LOOK GROUNDS":"You see the garden, a fountain and a hedge maze.",
        "LOOK AT GROUNDS":"You see the garden, a fountain and a hedge maze.",
        "EXAMINE MANOR GROUNDS":"You see the garden, a fountain and a hedge maze.",
        "EXAMINE GROUNDS":"You see the garden, a fountain and a hedge maze.",
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
        "EAST":EAST,
        "EXIT EAST":EAST,
        "GO EAST":EAST,
    }

    intro = "\nCONSERVATORY:\nThis glass-enclosed room affords you a view of the night\nsky and the manor grounds.  A set of double doors is open\nto the outside."

    # TODO: WEREWOLF: You smell wolf to the south and pungent herbs to the east.
    # EXITS: SOUTH: BILLIARD ROOM, EAST: GARDEN