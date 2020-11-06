class Vestibule:
    COAT = {
        "message":"You hang your coat on the coat tree and walk north toward the great hall.  The front door swings shut and locks behind you, which offers this chilling challenge: find a way out!",
        "location":4
    }
    commands = {
        "GO NORTH":"And drip water all over the floor?  Perhaps it would be polite to hang up your raincoat?",
        "EXAMINE COAT TREE":"It's currently empty.",
        "HANG COAT":COAT,
    }
    
    intro = "\nVESTIBULE:\nYou are standing in a vestibule.  Rain drips from your coat onto the floor.  To the north is the manor's great hall.  There is a coat tree here."

    # TODO: Remove raincoat from inventory, and have the raincoat be dry if the player explores a few rooms, FRONT DOOR option not available only after player hangs coat until player has key