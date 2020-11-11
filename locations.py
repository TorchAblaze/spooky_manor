inventory = ['Raincoat (worn)', 'Padlock key', 'Parcel']



# GATE
GATE_NORTH = {
    "message": "Eager to get out of the pouring rain, you hurry north up the dark cobblestone path towards the front door of the manor.",
    "points":0,
    "location":2,
    
}

BIKE = {
    "message":"You get off your bike, put the kick stand down and lock your bike on the metal fencing next to the gate.",
    "points":5,
}

GATE_COMMANDS = {
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
    "EXIT NORTH":GATE_NORTH,
    "NORTH":GATE_NORTH,
    "GO NORTH":GATE_NORTH,
}

GATE_INTRO = "\nTHE GATE:\nYou stop your bicycle by a forbidding wrought-iron gate.\nA cobblestone path winds its way to the north.  To the east\nand west streatches a dark and lonely road.  It is raining.\n\nYou are wearing a ranincoat and riding a bike."

# TODO: ALL ROOM INTROS (including this one) NEED TO BE CHANGED depending on how the player interacts their surroundings (taking things, missing things, using things, etc.)
# EXITS: NORTH: FRONT DOOR, EAST/WEST: ENDING



# FRONT DOOR
FDOOR_SOUTH = {
    "message":"You head south on the cobblestone path leading down towards the gate.",
    "location":1,
}
KNOCK = {
    "message":"Nobody answers, but the door cracks open, seemingly on its own!  You push the door inward and enter the dimly lit manor as lightning cracks in the distance.",
    "location":3
}
FRONT_DOOR_COMMANDS = {
    "KNOCK":KNOCK,
    "KNOCK DOOR":KNOCK,
    "KNOCK ON DOOR":KNOCK,
    "SOUTH":FDOOR_SOUTH,
    "GO SOUTH":FDOOR_SOUTH,
    "EXIT SOUTH": FDOOR_SOUTH,
    "ENTER DOOR":"It's locked.",
    "OPEN DOOR":"It's locked.",
}

FRONT_DOOR_INTRO = "\nFRONT DOOR:\nYou step up to Spooky Manor's imposing front door.  There is a brass knocker here."

# TODO: If player did not lock bike or rode the bike to the front door, the bike will have to be described as stolen and/or broken, otherwise, the bike stays locked at the GATE until player unlocks it
# TODO: After player knocks, let the player decide if they want to enter the door or not


# VESTIBULE
COAT = {
    "message":"You hang your coat on the coat tree.",
    "remove":"Raincoat (worn)",
}
VESTIBULE_NORTH = {
    "restriction in":"Raincoat (worn)",
    "message1":"And drip water all over the floor?  Perhaps it would be polite to hang up your raincoat?",
    "message2":"You walk north toward the great hall.  The front door swings shut and locks behind you, which offers this chilling challenge: find a way out!",
    "new location":4
}
VESTIBULE_COMMANDS = {
    "GO NORTH":VESTIBULE_NORTH,
    "NORTH":VESTIBULE_NORTH,
    "EXAMINE COAT TREE":"It's currently empty.",
    "HANG COAT":COAT,
    "HANG RAINCOAT":COAT,
    "HANG RAINCOAT ON COAT TREE":COAT,
    "HANG COAT ON COAT TREE":COAT,
}

VESTIBULE_INTRO = "\nVESTIBULE:\nYou are standing in a vestibule.  Rain drips from your coat onto the floor.  To the north is the manor's great hall.  There is a coat tree here."

# TODO: Have the raincoat be dry if the player explores a few rooms, FRONT DOOR option not available only after player hangs coat, player won't be able to open it until player has key
# TODO: Because hanging the coat it what prompts the player to go north, every time the player reenters this room, they will have to hang their raincoat even if they don't have one :(


# GREAT HALL
GREAT_HALL_SOUTH = {
    "message":"You head south toward the vestibule.",
    "location":3,
}
GREAT_HALL_EAST = {
    "message":"You walk toward the east wing of the manor.  You feel as though the eyes of the people in the portrait follow you.",
    "location":9,
}
GREAT_HALL_WEST = {
    "message":"You walk to the west wing of the manor, the old floor creaking beneath your feet.",
    "location":5
}
GREAT_HALL_UP = {
    "message":"You walk past the portraits and up the carpeted steps to the second floor.",
    "location":18,
}
GREAT_HALL_COMMANDS = {
    "EXAMINE PAINTINGS":"You see portraits of a distinguished-looking man and a pale-skinned woman.",
    "EXAMINE MIRROR":"You can see yourself.",  # TODO: add{wearing a smoking jacket/a wolf pelt} if they are in the inventory
    "SOUTH":GREAT_HALL_SOUTH,
    "EXIT SOUTH":GREAT_HALL_SOUTH,
    "GO SOUTH":GREAT_HALL_SOUTH,
    "EAST":GREAT_HALL_EAST,
    "EXIT EAST":GREAT_HALL_EAST,
    "GO EAST":GREAT_HALL_EAST,
    "WEST":GREAT_HALL_WEST,
    "EXIT WEST":GREAT_HALL_WEST,
    "UP":GREAT_HALL_UP,
    "GO UP":GREAT_HALL_UP,
    "EXIT UP":GREAT_HALL_UP,
    "GO UP STAIRS":GREAT_HALL_UP,
    "GO UP STAIRCASE":GREAT_HALL_UP,
}

GREAT_HALL_INTRO = "\nGREAT HALL:\nArchways lead to the east and west wings of the manor.\nThere are some oil paintings and a large mirror hanging\non the wall.  A staircase leads up to the second floor.  The\nvestibule is to the south."

# TODO: Add options to "examine mirror": WEREWOLF(You notice you have pointy ears, sharp teeth and hair covering most of your face.) VAMPIRE(You can't see your reflection in the mirror!)
# EXITS: SOUTH: VESTIBULE, EAST: LIBRARY, WEST: DINING ROOM, UP: HALLWAY



# DINING ROOM
DINING_ROOM_NORTH = {
    "message":"You head north to leave the dining room.",
    "location":7,
}
DINING_ROOM_SOUTH =  {
    "message":"You walk south out of the dining room.",
    "location":6,
}
DINING_ROOM_EAST = {
    "message":"You head east back to the Great Hall.",
    "location":4,
}
PHEASANT = {
    "restriction out":"Meat cleaver",
    "message1":"It's still attached.",
    "message2":"You take the drumstick.  Oof, it's kind of heavy, you don't think you can carry more than one.",
}
DINING_ROOM_COMMANDS = {
    "EXAMINE PHEASANT":"The meat looks to be cold and unappetizing.",
    "TAKE PHEASANT":"You ponder carrying around a whole roast pheasant and decide against it.",
    "TAKE DRUMSTICK":PHEASANT,
    "USE CLEAVER ON PHEASANT":"You hack off one of the drumsticks to carry around with you, county fair-style.",
    "EAT DRUMSTICK":"You're not hungry.",
    "NORTH":DINING_ROOM_NORTH,
    "EXIT NORTH":DINING_ROOM_NORTH,
    "GO NORTH":DINING_ROOM_NORTH,
    "SOUTH":DINING_ROOM_SOUTH,
    "EXIT SOUTH":DINING_ROOM_SOUTH,
    "GO SOUTH":DINING_ROOM_SOUTH,
    "EAST":DINING_ROOM_EAST,
    "EXIT EAST":DINING_ROOM_EAST,
    "GO EAST":DINING_ROOM_EAST,
}

DINING_ROOM_INTRO = "\nDINING ROOM:\nThe dining room contains a long banquet table.  A whole\nroast pheasant, complete with drumsticks, rests in the\ncenter of the table.  Exits are to the north, south and east."

# TODO: WEREWOLF: "You smell wolf to the north and smoke to the\nsouth.  The meat on the table smells delicious!"
# TODO: Player can only carry one drumstick at a time
# TODO: Drumsticks can be eaten by werewolf players
# TODO: USE CLEAVER ON PHEASANT can only work if player has cleaver in their inventory and EAT DRUMSTICK should only work if player cut the pheasant with cleaver and/or has DRUMSTICK already in their inventory
# TODO: Player should be allowed to TAKE DRUMSTICK if they used the cleaver on the phesant
# TODO: There are only two drumsticks in this game. After they are succesfully eaten, they should no longer be available.
# EXITS: NORTH: KITCHEN, SOUTH: LOUNGE, EAST: GREAT HALL


# LOUNGE
LOUNGE_NORTH = {
    "message":"You walk out back toward the Dining Room.",
    "location":5,
}
TAKE_SMOKING_JACKET = {
    "message":"You take the smoking jacket.",
    "add":"Smoking Jacket (worn)",
}
LOUNGE_COMMANDS = {
    "EXAMINE JACKET":"The red satin jacket bears the Spooky family crest.",
    "DRINK BRANDY":"No drinking on the job!",
    "TAKE BRANDY":"You'll spill it.",
    "EXAMINE CHAIR":"A compfy-looking overstuffed chair with wooden legs.  There is a smoking jacket folded over on one of its arm.",
    "EXAMINE FIRE":"The fire brightens up the room, casting shadows along the wall.  The cackling sound and warmth are welcoming in an otherwise quiet and drafty manor.",
    "EXAMINE HEARTH":"The fire brightens up the room, casting shadows along the wall.  The cackling sound and warmth are welcoming in an otherwise quiet and drafty manor.",
    "EXAMINE BRANDY":"A footed glass filled with some type of alcohol.",
    "EXAMINE SNITFTER":"A footed glass filled with some type of alcohol.",
    "TAKE SMOKING JACKET":TAKE_SMOKING_JACKET,
    "TAKE JACKET":TAKE_SMOKING_JACKET,
    "NORTH":LOUNGE_NORTH,
    "EXIT NORTH":LOUNGE_NORTH,
    "GO NORTH":LOUNGE_NORTH,
}

LOUNGE_INTRO = "\nLOUNGE:\nYou enter the lounge, where a fire is roaring in the hearth.\nA smoking jacket rests on the arm of an overstuffed chair.\nThere is a snifter of brandy here."

# TODO: WEREWOLF: You smell meat to the north
# TODO: VAMPIRE: Panicked by the sight of an open flame, you flee the fire! ~Vampires retreat north to the DINING ROOM
# TODO: WET PLAYER: To recover from being cold and wet, the player must WEAR JACKET or WEAR WOLF PELT, then SIT BY FIRE and DRINK BRANDY (Player must be allowed to DRINK BRANDY in this case)
# TODO: ITEMS: if player takes smoking jacket, smoking jacket comments should be removed
# EXITS: NORTH: DINING ROOM



# KITCHEN
KITCHEN_SOUTH = {
    "message":"You walk toward the dining room.",
    "location":5,
}
KITCHEN_DOWN = {
    "message":"You open the cellar door and down a dark set of stairs.  You hear the sound of low growls coming from below....",
    "location":8,
}
OLIVE_OIL = {
    "message":"You take the olive oil.",
    "add":"Olive oil",
}
MEAT_CLEAVER = {
    "message":"You take the meat cleaver.",
    "add":"Meat cleaver",
}
KITCHEN_COMMANDS = {
    "EXAMINE OLIVE OIL":"The bottle is almost empty.",
    "EXAMINE OIL":"The bottle is almost empty.",
    "EXAMINE CELLAR DOOR":"A closed wooden door with a handle.  It doesn't appear to be locked and you can hear rustling through the door.",
    "EXAMINE MEAT CLEAVER":"A cutting utensil...for meat.",
    "SOUTH":KITCHEN_SOUTH,
    "EXIT SOUTH":KITCHEN_SOUTH,
    "GO SOUTH":KITCHEN_SOUTH,
    "DOWN":KITCHEN_DOWN,
    "EXIT DOWN":KITCHEN_DOWN,
    "GO DOWN":KITCHEN_DOWN,
    "ENTER CELLAR DOOR":KITCHEN_DOWN,
    "TAKE OLIVE OIL":OLIVE_OIL,
    "TAKE OIL":OLIVE_OIL,
    "TAKE MEAT CLEAVER":MEAT_CLEAVER,
    "TAKE CLEAVER":MEAT_CLEAVER,
    "DRINK OLIVE OIL":"Uh...You don't exactly find these things appetizing.  You don't know why you would come up with such a silly idea."
}

KITCHEN_INTRO = "\nKITCHEN:\nThe kitchen is old-fashioned, devoid of most modern\nconviences.  There is a meat cleaver here.  There is a\nsmall bottle of olive oil here.  A cellar door leads down."

# TODO: WEREWOLF: "You smell meat to the south and wolf downstairs."
# EXITS: SOUTH: DINING ROOM, DOWN: DARK CELLAR



# DARK CELLAR
DARK_CELLAR_UP = {
    "message":"Unbeliving of what you just saw, you head back up the dark cellar stairs questioning why you ever took this job.",
    "location":7,
}
GARLIC = {
    "message":"You take the garlic cloves.",
    "add":"Garlic cloves",
}
DARK_CELLAR_COMMANDS = {
    "EXAMINE WOLF":"The savage beast strains at the chain around its neck.",
    "USE WOLFSBANE ON DRUMSTICK":"You rub the herb onto the meat.",
    "EXAMINE MAN":"A tall, gaunt man with thinning hair and a penchil-thin mustache.  He's currently covering his naked body with a large tin of peaches he took from a shelf.",
    "TALK TO MAN":"The man replies 'I was attacked while hunting with Lord Spooky last week.  Everything after that is just a blur.'",
    "DROP PARCEL":"Pretty sure the parcel isn't addressed to a wolf.",
    "THROW PARCEL":"You ponder throwing the parcel at the beast, but delivering the parcel to the right person is why you entered this wretched place.  Don't lose hope now.",
    "TAKE CLOVES OF GARLIC":GARLIC,
    "TAKE CLOVES":GARLIC,
    "TAKE GARLIC":GARLIC,
    "TAKE GARLIC CLOVES":GARLIC,
    "UP":DARK_CELLAR_UP,
    "EXIT UP":DARK_CELLAR_UP,
    "GO UP":DARK_CELLAR_UP,
    "EXIT CELLAR":DARK_CELLAR_UP,
}

DARK_CELLAR_INTRO = "\nDARK CELLAR:\nYou enter the dark cellar and see a monstrous wolf\nchained to the wall!  There are cloves of garlic here."

# TODO: ITEMS: Garlic(see VAMPIRE)

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
