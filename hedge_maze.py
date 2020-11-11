class HedgeMaze:
    WEST =  {
        "message":"You walk back west towards the garden.",
        "location":13,
    }
    SOUTH = {
        "message":"Thanks to your handy dandy hedge master cutting skills, you follow the new path south.",
        "location":16,
    }
    commands = {
        "USE SHEARS":"The shears are rusty and difficult to use.",
        "OIL SHEARS":"The oil allows you to smoothly open and close the shears.",
        "USE [OILED] SHEARS ON HEDGE":"\nSNIP SNIP SNIP\nYou begin to clear a path south through the hedges to bypass the maze.",
        "WEST":WEST,
        "EXIT WEST":WEST,
        "GO WEST":WEST,
        "SOUTH":SOUTH,  # see TODO
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
}

intro = "You take a step inside the hedge maze but then retreat\nback to the garden.  It wouldn't do to get lost, especially\nat night."

# TODO: WEREWOLF: The werewolf may sniff its way through the maze to the smouldering decay of the Graveyard, or back to the pungent stench of the Garden.
# TODO: VAMPIRE: The vampire may simply fly up to the Attic and reenter the manor through the broken window.
# TODO: OIL SHEARS: The player may use the oiled shears to clear a path through the hedges.  Once a path is cleared, the player can bypass the maze.
# EXITS: WEST: GARDEN, SOUTH: GRAVEYARD