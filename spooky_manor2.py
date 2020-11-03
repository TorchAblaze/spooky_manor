class Game:
    inventory = ['Raincoat (worn)', 'Padlock key', 'Parcel']
    points = 0
    commands = {}
    plus_five = {}
    intro = ""

    @staticmethod
    def show_help():
        print("""
HOW TO PLAY:
Enter a verb (such as: 'go', 'shake', 'open', 'examine', 'use', 'talk', 'take', 'eat', 'drink', 'give', 'read', 'play', 'look', 'enter') and a noun that you would like to interact with. 
Enter 'inventory' to view your inventory.
Enter 'points' to view your point total.
Enter 'help' for this help.
Enter 'save' to save the game.
Enter 'quit' to exit the game.
""")

    def take(self, item):
        pass
        # inventory.append(item)

    @classmethod
    def game_play(cls):
        print(cls.intro)
        while True:
            command = input("\n >  ").upper()
            if command in cls.commands.keys():
                    print(cls.commands[command])
                    if command in cls.plus_five:
                        Game.points += 5
                    continue
            elif command not in cls.commands.keys():
                if command == 'HELP':
                    Game.show_help()
                    continue
                elif command == 'POINTS':
                    print("Points:", Game.points)
                elif command == 'INVENTORY':
                    for item in Game.inventory:
                        print(item)
                elif command == 'SAVE':
                    pass
                elif command == 'LOOK':
                    print(cls.intro)
                elif command == 'QUIT':
                    break
                elif command == 'RESTART':
                    restart = input("Are you sure you want to restart the game? ('yes' or 'no')\n >  ")
                    if restart == 'YES':
                        pass
                    else:
                        continue
                else:
                    print("Hmm, I'm not sure what you mean.  Please enter a verb and a noun to interect with your surroundings.")

    ending = "Enter 'quit' to quit, enter 'save' to save or enter 'restart' to restart."
    
    @staticmethod
    def victory():
        return "\nYou leave behind the manor and its secrets--another job well done.\nPerhaps one day you may pay another visit to Lord Spooky and Manfred,\nbut until then, only in your darkest dreams and nightmares will you return... \n\nto Spoooky Manor!\n\nTHE END."
        # points += 5
    
class Intro(Game):
    commands = {
        "EXAMINE BIKE":"The basket contains a small parcel. A heavy chain and padlock are wrapped around the bike's frame. You are currently on the bicycle.",
        "EXAMINE PARCEL":"A box wrapped in paper and tied with twine.  It's addressed to 'Lord Alastair Spooky.'",
        "SHAKE PARCEL":"It rattles.",
        "OPEN PARCEL":"It's not yours to open!",
        "EXAMINE RAINCOAT":"Your dark-green raincoat marks you as a courier for Parcel-E-Delivery. There is a padlock key in the pocket. You are wearing the raincoat.",
        "EXAMINE GATE":"The wrought-iron gate features the Spooky family crest. It's closed.",
        "EXAMINE PATH":"The neglected path looks hazardous to your bike's fragile tires.",
        "USE PADLOCK":"You locked your bike.",
        "LOCK BIKE":"You locked your bike.",
        "DROP PARCEL":"That's not proper couriership :(",
        "EXIT EAST": Game.victory(),
        "EXIT WEST": Game.victory(),
    }

    intro = "\nYou stop your bicycle by a forbidding wrought-iron gate.\nA cobblestone path winds its way to the north.  To the east\nand west streatches a dark and lonely road.  It is raining.\n\nThe player starts the game wearing a ranincoat and riding a bike.\n"

    # def __init__(self, commands_list):
    #     self.commands = commands_list
    
    def start_prompt(self):
        print("\nWELCOME TO SPOOKY MANOR...")
        Game.show_help()

        Intro.game_play()

    plus_five = ["USE PADLOCK", "LOCK BIKE", "EXIT EAST/WEST", "EXIT EAST", "EXIT WEST"]

    @classmethod
    def game_play(cls):
        super().game_play()

intro = Intro()
intro.start_prompt()

    
    



