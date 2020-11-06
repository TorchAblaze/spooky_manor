class Lounge:
    NORTH = {
        "message":"You walk out back toward the Dining Room.",
        "location":5,
    }
    commands = {
        "EXAMINE JACKET":"The red satin jacket bears the Spooky family crest.",
        "DRINK BRANDY":"No drinking on the job!",
        "TAKE BRANDY":"You'll spill it.",
        "EXAMINE CHAIR":"A compfy-looking overstuffed chair with wooden legs.  There is a smoking jacket folded over on one of its arm.",
        "EXAMINE FIRE":"The fire brightens up the room, casting shadows along the wall.  The cackling sound and warmth are welcoming in an otherwise quiet and drafty manor.",
        "EXAMINE HEARTH":"The fire brightens up the room, casting shadows along the wall.  The cackling sound and warmth are welcoming in an otherwise quiet and drafty manor.",
        "EXAMINE BRANDY":"A footed glass filled with some type of alcohol.",
        "EXAMINE SNITFTER":"A footed glass filled with some type of alcohol.",
        "TAKE SMOKING JACKET":"You take the smoking jacket.",  # Add to inventory
        "TAKE JACKET":"You take the smoking jacket.",  # Add to inventory
        "NORTH":NORTH,
        "EXIT NORTH":NORTH,
        "GO NORTH":NORTH,
    }

    intro = "\nLOUNGE:\nYou enter the lounge, where a fire is roaring in the hearth.\nA smoking jacket rests on the arm of an overstuffed chair.\nThere is a snifter of brandy here."

    # TODO: WEREWOLF: You smell meat to the north
    # TODO: VAMPIRE: Panicked by the sight of an open flame, you flee the fire! ~Vampires retreat north to the DINING ROOM
    # TODO: WET PLAYER: To recover from being cold and wet, the player must WEAR JACKET or WEAR WOLF PELT, then SIT BY FIRE and DRINK BRANDY (Player must be allowed to DRINK BRANDY in this case)
    # TODO: ITEMS: if player takes smoking jacket, smoking jacket comments should be removed
    # EXITS: NORTH: DINING ROOM