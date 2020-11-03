class SpookyManor:
    exits: []
    
    def __init__(self, room, objects, exits, **kwargs):
        self.room = room
        self.objects = objects
        self.exits = exits

        for key, value in kwargs.items():
            setattr(self, key, value)  

inventory = ['Raincoat (worn)', 'Padlock key']

def show_help():
        print("Welcome to Spooky Manor...")
        print("""
Enter a verb such as: 'go', 'shake', 'open', 'examine', 'use', 'talk', 'take', 'eat', 'drink', 'give', 'read', 'play', 'look', 'enter', and enter a noun that you would like to interact with. 
Enter 'inventory' to view your inventory.
Enter 'points' to view your point total.
Enter 'help' for this help.
Enter 'save' to save the game.
""")

gate = SpookyManor("The Gate", "Parcel, Padlock key, Raincoat (worn)", "North or East/West")



verbs = ['go', 'shake', 'open', 'examine', 'use', 'talk', 'take', 'eat', 'drink', 'give', 'read', 'play', 'look', 'enter', 'knock', 'break', 'stop']

points = 0

print("You stop your bicycle by a forbidding wrought-iron gate.\nA cobblestone path winds its way to the north.  To the east\nand west streatches a dark and lonely road.  It is raining.\n\nThe player starts the game wearing a ranincoat and riding a bike.")

while True:    
    command = input(" >  ").upper
    if command() == 'HELP':
        show_help()
        continue
    elif command() == 'POINTS':
        print("Points:", points)
    elif command() == 'INVENTORY':
        for item in inventory:
            print(item)
    elif command() == 'SAVE':
        pass
    elif command() == 'EXAMINE BIKE':
        print("The basket contains a small parcel. A heavy chain and padlock are wrapped around the bike's frame. You are currently on the bicycle.")
    elif command() == 'EXAMINE PARCEL':
        print("A box wrapped in paper and tied with twine.  It's addressed to 'Lord Alastair Spooky.")
    elif command() == 'SHAKE PARCEL':
        print("It rattles.")
    elif command() == 'OPEN PARCEL':
        print("It's not yours to open!")
    elif command() == 'EXAMINE RAINCOAT':
        print("Your dark-green raincoat marks you as a courier for Parcel-E-Delivery. There is a padlock key in the pocket. You are wearing the raincoat.")
    elif command() == 'EXAMINE GATE':
        print("The wrought-iron gate features the Spooky family crest. It's closed.")
    elif command() == 'EXAMINE PATH':
        print("The neglected path looks hazardous to your bike's fragile tires.")
    elif command() == 'LOCK BIKE' or 'USE PADLOCK':
        print('You locked your bike.')
        points += 5
    else:
        print("Hmm, I'm not sure what you mean.  Please enter a verb and a noun to interect with.")

print(points)