class ReflectingPool:
    SOUTH = {
        "message":"You head back to the garden to the south.",
        "location":13,
    }
    commands = {
        "EXAMINE POOL":"You see some gardening shears in the middle of the reflecting pool.",
        "DIVE":"You hit your head and drown.  THE END.",  # GHOST ending
        "DIVE IN POOL":"You hit your head and drown.  THE END.",
        "DIVE INTO POOL":"You hit your head and drown.  THE END.",
        "EXAMINE SHEARS":"They're old and rusted.",
        "ENTER POOL":"The water is cold and you're soon soaked to the bone.  Achoo!",  # see TODO
        "EXAMINE FOUNTAIN":"You see an elaborate marble sculpture of a wolf baying at the moon.  Water spouts from the wolf's jaws and splashes down into the pool.  The Spooky motto is inscribed here: 'Mors Certa, Hora Incerta.'",
        "SOUTH":SOUTH,
        "EXIT SOUTH":SOUTH,
        "GO SOUTH":SOUTH,
    }

    intro = "You've come to a marble-tiled reflecting pool.  There's a\nfountain here.  You smell pungent herbs to the south."

# TODO: ENTER POOL: The player becomes sick and cannot perform strenuous activity, such as digging or prying open the crypt door.  This may be cured by recuperating in the LOUNGE with a snifter of brandy, dry clothing and a warm fire.  Until then, remind the player they're a shivering wreck!
# TODO: VAMPIRE: The vampire may not enter the running water
# TODO: ITEMS: gardening shears
# EXITS: SOUTH: GARDEN