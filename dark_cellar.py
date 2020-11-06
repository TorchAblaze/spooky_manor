class DarkCellar:
    UP = {
        "message":"Unbeliving of what you just saw, you head back up the dark cellar stairs questioning why you ever took this job.",
        "location":7,
    }
    commands = {
        "EXAMINE WOLF":"The savage beast strains at the chain around its neck.",
        "USE WOLFSBANE ON DRUMSTICK":"You rub the herb onto the meat.",
        "EXAMINE MAN":"A tall, gaunt man with thinning hair and a penchil-thin mustache.  He's currently covering his naked body with a large tin of peaches he took from a shelf.",
        "TALK TO MAN":"The man replies 'I was attacked while hunting with Lord Spooky last week.  Everything after that is just a blur.'",
        "DROP PARCEL":"Pretty sure the parcel isn't addressed to a wolf.",
        "THROW PARCEL":"You ponder throwing the parcel at the beast, but delivering the parcel to the right person is why you entered this wretched place.  Don't lose hope now.",
        "TAKE CLOVES OF GARLIC":"You take the garlic cloves.",  # Add to inventory
        "TAKE CLOVES":"You take the garlic cloves.",  # Add to inventory
        "TAKE GARLIC":"You take the garlic cloves.",  # Add to inventory
        "TAKE GARLIC CLOVES":"You take the garlic cloves.",  # Add to inventory
        "UP":UP,
        "EXIT UP":UP,
        "GO UP":UP,
        "EXIT CELLAR":UP,
    }

    intro = "You enter the dark cellar and see a monstrous wolf\nchained to the wall!  There are cloves of garlic here."

    # TODO: Items: Garlic(see VAMPIRE)

    # TODO: USE WOLFSBANE ON DRUMSTICK should only work if player has WOLFSBANE and DRUMSTICK in inventory
    # TODO: Werewolf will eat DRUMSTICK whether it is covered in WOLFSBANE or not, but it must be covered in WOLFSBANE for werewolf to change back to human form
    # TODO: If the player stays here for too many turns without curing Manfred, or tries to ATTACK WOLF with the MEAT CLEAVER or the SILVER PEN (and if in inventory), the wolf snaps its chain and attacks:
        # The wolf overpowers you, and you feel its sharp teeth and claws savage your flesh.  Hours later, you wake up, uninjured but wearing bloody, torn clothing.  Your senses seeem especially keen, and your fingernails are long and sharp.  The wolf is nowhere to be found.
        # TODO: WEREWOLF: The player is now a werewolf!  The werewolf has a keen sense of smell, is allergic to silver and wolfsbane and has sharp claws.
        # TODO: WEREWOLF: If the player uses WOLFSBANE and DRUMSTICK on themself at any point in the game, so long as they are in his inventory, it will cure them of lycanthropy
        # TODO: VAMPIRE: A vampire player character may not take the garlic.  If attacked by the wolf, the vampire will assume mist form, drift off to the Graveyard and revert back, weak and injured.  A vampire player must return to their grave to rest before continuing.

    # If werewolf is returned to human form:
    # TODO: TALK TO MAN should only work if the werewolf was returned to human form
    # TODO: EXAMINE MAN should only work if the werewolf was returned to human form
    # TODO: Manfred will only leave the cellar once given the SMOKING JACKET, the RAINCOAT, or the WOLF PELT.  Once he has one of these, he will leave and wait for the player by the door to the Master Suite.
    # EXITS: UP: KITCHEN
    