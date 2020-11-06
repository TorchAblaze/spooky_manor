from navigation import Navigation
from gate import Gate
from front_door import FrontDoor
from vestibule import Vestibule
from great_hall import GreatHall
from dining_room import DiningRoom
from lounge import Lounge
from kitchen import Kitchen
from dark_cellar import DarkCellar

inventory = ['Raincoat (worn)', 'Padlock key', 'Parcel']

def show_help():
    print("""
HOW TO PLAY:
Enter a verb (such as: 'take/get', 'drop', 'talk', 'kill', 'light', 'wear', 'use',
'enter/exit', 'go (direction)', 'north', 'south', 'east', 'west', 'up/down',
'shake', 'open', 'examine', 'eat', 'drink', 'give', 'read', 'play', 'look')
and a noun that you would like to interact with. 

Enter 'inventory' to view your inventory.
Enter 'score' to view your point total.
Enter 'help' for this help.
Enter 'save' to save the game.
Enter 'quit' to exit the game.
""")

def take(self, item):
    pass
    # inventory.append(item)

ending = "Enter 'quit' to quit, enter 'save' to save or enter 'restart' to restart the game."
    
# victory(end):
#     print("\nYou leave behind the manor and its secrets--another job well done.\nPerhaps one day you may pay another visit to Lord Spooky and Manfred,\nbut until then, only in your darkest dreams and nightmares will you return... \n\nto Spoooky Manor!\n\nTHE END.")
#     return end 
    # points += 5


rooms = {
    1: Gate(),
    2: FrontDoor(),
    3: Vestibule(),
    4: GreatHall(),
    5: DiningRoom(),
    6: Lounge(),
    7: Kitchen(),
    8: DarkCellar(),
    # 9: DarkCellarCont(),
    # 10: Library(),
    # 11: SecretStudy(),
    # 12: BilliardRoom(),
    # 13: Conservatory(),
    # 14: Garden(),
    # 15: ReflectingPool(),
    # 16: HedgeMaze(),
    # 17: Graveyard(),
    # 18: FamilyCrypt(),
    # 19: FamilyCryptCont(),
    # 20: Hallway(),
    # 21: Attic(),
    # 22: ServantsQuarters(),
    # 23: MasterSuite()
}

print("\nWELCOME TO SPOOKY MANOR...")
show_help()
print(Gate.intro)

player_location = 1
points = 0

while True:
    class_name = rooms[player_location]
    command = input("\n >  ").upper()
    try:
        if type(class_name.commands[command]) == dict:
            for key, value in class_name.commands[command].items():
                if key == "message":
                    print(class_name.commands.get(command)["message"])
                elif key == "points":
                    points += class_name.commands.get(command)["points"]
                elif key == "location":
                    player_location = class_name.commands.get(command)["location"]
                    class_name = rooms[player_location]
                    print(class_name.intro)
            continue
        elif command in class_name.commands.keys():
            print(class_name.commands[command])    
            continue
    except KeyError as err:
        if command == 'HELP':
            show_help()
            continue
        elif command == 'SCORE':
            print("Score:", points)
            continue
        elif command == 'INVENTORY':
            for item in inventory:
                print(item)
                continue
        elif command == 'SAVE':
            pass  # Find way to save game
        elif command == 'LOOK':
            print(class_name.intro)
            continue
        elif command == 'QUIT':
            break
        elif command == 'RESTART':
            restart = input("Are you sure you want to restart the game? ('yes' or 'no')\n >  ")
            if restart == 'YES':
                pass  # Find a way to restart the game
            else:
                continue
        else:
            print("Hmm, I'm not sure what you mean.  Please enter a verb and a noun to interect with your surroundings.")
            continue


# class JoesPlace:
#     NORTH = {
#         "message": "You've gone north. You fool!",
#         "points": 2,
#         "location": 5
#     }
#     commands = {
#         "GO NORTH": NORTH,
#         "GO UP": NORTH,
#         "LOOK FOR LAPTOP": {
#             "message": "You find a laptop. Now you have to do work. -5 points",
#             "points": -5
#         }
#     }

#     # commands = {
#     #     "GO NORTH": Command("You've gone north. You fool!", 2, 5),
#     #     "LOOK FOR LAPTOP": Command("You find a laptop. Now you have to do work. -5 points", -5)
#     # }

#     # commands = [
#     #     Command(["GO NORTH", "GO UP"], "You've gone north. You fool!", 2, 5)
#     # ]

# class Command:
#     def __init__(self, acceptable, message, points, location = 0):
#         self.message = message
#         self.points = points
#         self.location = location
#         self.acceptable_commands = acceptable
    
#     def match(self, input):
#         if input in self.acceptable_commands:
#             return True
    