class FrontDoor:
    SOUTH = {
        "message":"You head south on the cobblestone path leading down towards the gate.",
        "location":1,
    }
    KNOCK = {
        "message":"Nobody answers, but the door cracks open, seemingly on its own!  You push open the door and enter the dimly lit manor as thunder crackles in the distance.",
        "location":3
    }
    commands = {
        "KNOCK":KNOCK,
        "EXIT SOUTH": SOUTH,
        "ENTER DOOR":"It's locked.",
        "OPEN DOOR":"It's locked.",
    }
    
    intro = "\nFRONT DOOR:\nYou step up to Spooky Manor's imposing front door.  There is a brass knocker here."

    # TODO: If player did not lock bike or rode the bike to the front door, the bike will have to be described as stolen and/or broken, otherwise, the bike stays locked at the GATE until player unlocks it
