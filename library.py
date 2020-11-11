class Library:
    NORTH = {
        "message":"You walk through the library and head north.",
        "location":11,
    }
    SOUTH = {
        "message":"You head south through the secret door of the sarcophagus.",
        "points":10,
        "location":10,
    }
    WEST = {
        "message":"You head south toward the Great Hall.",
        "location":4
    }
    commands = {
        "EXAMINE BOOKS":"Most of the library books are covered in dust.  A few catch your eye: 'Herbalism for Beginners,' 'Mysteries of Ancient Egypt,' and a first edition of Dante's 'Inferno.'",
        "EXAMINE SARCOPHAGUS":"The heavy sarcophagus is either an antique or a clever copy.",
        "READ HERBALISM FOR BEGINNERS":"You read the first entry: 'Aconitum vulparia, a poisonous plant known as wolfsbane, is rumored to cure lycanthropy.'  Yawn, boooring.",
        "TAKE MYSTERIES OF ANCIENT EGYPT":"The sarcophagus slides open, revealing a seret door to the south.",
        "TAKE DANTE'S INFERNO":"A trapdoor opens up beneath your feet, sending you down a chute into the manor's incinerator.\n\n\n Wait, the wha-?!",  # THE GHOST ending, also see VAMPIRE in TODO
        "TAKE HERBALISM FOR BEGINNERS":"You took 'Herbalism for Beginners.'",  # Add to inventory
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
        "SOUTH":SOUTH,  # TODO: Only available if player takes MYSTERIES OF ANCIENT EGYPT
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
        "WEST":WEST,
        "EXIT WEST":WEST,
        "GO WEST":WEST,
    }

    intro = "\nLIBRARY:\nThe library is home to many old books.  An Egyptian\nsarcophagus stands in the corner.  Exits are to the north\nand west."

    # TODO: if player takes HERBALISM FOR BEGINNERS, they should be able to read it as long as it's in their inventory
    # TODO: ITEMS: HERBALISM FOR BEGINNERS
    # TODO: VAMPIRE: If VAMPIRE picks up DANTE'S 'INFERNO': You're immolated in the fire and turn to ash.  THE END.
    # EXITS: NORTH: BILLARD ROOM, SOUTH: SECRET STUDY (if open), WEST: GREAT HALL