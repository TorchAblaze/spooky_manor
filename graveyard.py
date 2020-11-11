class Graveyard:
    NORTH = {
        "message":"You head north back toward the hedge maze.",
        "location":15,
    }
    # CRYPT = {
    #     "message":"You enter the door of the crypt and walk down the steep stairs into the darkness below.",
    #     "location":17,
    # }
    commands = {
        "EXAMINE CRYPT":"It's covered in mouldering vegetation, marred by time and the elements.  An inscription reads, 'Lady Vanessa Spooky, RIP.'  The birth and death dates on the crypt are scratched out.",
        "ENTER CRYPT":"The stone door's hinges are covered in rust.",
        "EXAMINE SPADE":"The spade is old but sturdy.",
        "DIG GRAVE":"It takes a while, but you manage to dig a pretty impressive hole in the ground.",
        "PRY DOOR":"You pry open the door to the crypt.",
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
        # "CRYPT":CRYPT,
    }

    intro = "You've stumbled into a cemetery.  A few crumbling\ntombstones litter the ground.  There is a crypt here.\nThere is a gravedigger's spade here."