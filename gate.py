class Gate:
    NORTH = {
        "message": "Eager to get out of the pouring rain, you hurry north up the dark cobblestone path towards the front door of the manor.",
        "points":0,
        "location":2,
        
    }
    BIKE = {
        "message":"You get off your bike, put the kick stand down and lock your bike on the metal fencing next to the gate.",
        "points":5,
    }
    commands = {
        "EXAMINE BIKE":"The basket contains a small parcel. A heavy chain and padlock are wrapped around the bike's frame. You are currently on the bicycle.",
        "EXAMINE PARCEL":"A box wrapped in paper and tied with twine.  It's addressed to 'Lord Alastair Spooky.'",
        "SHAKE PARCEL":"It rattles.",
        "OPEN PARCEL":"It's not yours to open!",
        "EXAMINE RAINCOAT":"Your dark-green raincoat marks you as a courier for Parcel-E-Delivery. There is a padlock key in the pocket. You are wearing the raincoat.",
        "EXAMINE GATE":"The wrought-iron gate features the Spooky family crest. It's closed.",
        "EXAMINE PATH":"The neglected path looks hazardous to your bike's fragile tires.",
        "USE PADLOCK":BIKE,
        "LOCK BIKE":BIKE,
        "DROP PARCEL":"That's not proper couriership :(",
        "GET OFF BIKE":"You get off your bike.",
        "EXAMINE COBBLESTONE":"The neglected path looks hazardous to your bike's fragile tires.",
        # "EXIT EAST": ,
        # "EXIT WEST": ,
        "EXIT NORTH":NORTH,
        "NORTH":NORTH,
        "GO NORTH":NORTH,
    }

    intro = "\nTHE GATE:\nYou stop your bicycle by a forbidding wrought-iron gate.\nA cobblestone path winds its way to the north.  To the east\nand west streatches a dark and lonely road.  It is raining.\n\nYou are wearing a ranincoat and riding a bike.\n"

    # def __init__(self, commands_list):
    #     self.commands = commands_list

