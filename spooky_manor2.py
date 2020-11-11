from room import Room
import locations

def show_help():
    print("""
HOW TO PLAY:
Enter a verb (such as: 'take/get', 'drop', 'talk', 'kill', 'light', 'wear', 'use',
'enter/exit', 'go (direction)', 'north', 'south', 'east', 'west', 'up/down',
'shake', 'open', 'examine', 'eat', 'drink', 'give', 'read', 'play', 'look')
and a noun that you would like to interact with. 

Enter 'inventory' to view your inventory.
Enter 'score' to view your point total.
Enter 'location' to view your current location.
Enter 'help' for this help.
Enter 'save' to save the game.
Enter 'quit' to exit the game.
""")

ending = "Enter 'quit' to quit, enter 'save' to save or enter 'restart' to restart the game."
    
# victory(end):
#     print("\nYou leave behind the manor and its secrets--another job well done.\nPerhaps one day you may pay another visit to Lord Spooky and Manfred,\nbut until then, only in your darkest dreams and nightmares will you return... \n\nto Spoooky Manor!\n\nTHE END.")
#     return end 
    # points += 5

GATE = Room(
    "Gate",
    locations.GATE_COMMANDS,
    locations.GATE_INTRO
    )
FRONT_DOOR = Room(
    "Front Door",
    locations.FRONT_DOOR_COMMANDS,
    locations.FRONT_DOOR_INTRO
    )
VESTIBULE = Room(
    "Vestibule",
    locations.VESTIBULE_COMMANDS,
    locations.VESTIBULE_INTRO
    )
GREAT_HALL = Room(
    "Great Hall",
    locations.GREAT_HALL_COMMANDS,
    locations.GREAT_HALL_INTRO
)
DINING_ROOM = Room(
    "Dining Room",
    locations.DINING_ROOM_COMMANDS,
    locations.DINING_ROOM_INTRO
)
LOUNGE = Room(
    "Lounge",
    locations.LOUNGE_COMMANDS,
    locations.LOUNGE_INTRO
)
KITCHEN = Room(
    "Kitchen",
    locations.KITCHEN_COMMANDS,
    locations.KITCHEN_INTRO
)
DARK_CELLAR = Room(
    "Dark Cellar",
    locations.DARK_CELLAR_COMMANDS,
    locations.DARK_CELLAR_INTRO
)
rooms = {
    1: GATE,
    2: FRONT_DOOR,
    3: VESTIBULE,
    4: GREAT_HALL,
    5: DINING_ROOM,
    6: LOUNGE,
    7: KITCHEN,
    8: DARK_CELLAR,
    # 9: Library(),
    # 10: SecretStudy(),
    # 11: BilliardRoom(),
    # 12: Conservatory(),
    # 13: Garden(),
    # 14: ReflectingPool(),
    # 15: HedgeMaze(),
    # 16: Graveyard(),
    # 17: FamilyCrypt(),
    # 18: Hallway(),
    # 19: Attic(),
    # 20: ServantsQuarters(),
    # 21: MasterSuite(),
}
game_name = "SPOOKY MANOR"
print(f"\nWELCOME TO:\n{game_name}...")
show_help()

player_location = 1
points = 0

print(rooms[player_location].intro)

while True:
    room_name = rooms[player_location]
    command = input("\n >  ").upper()
    try:
        result = room_name.commands
        if type(result[command]) == dict:
            for key, value in result[command].items():
                if key == "restriction in":
                    if value in locations.inventory:
                        print(result.get(command)["message1"])
                    elif value not in locations.inventory:
                        print(result.get(command)["message2"])
                        player_location = result.get(command)["new location"]
                        room_name = rooms[player_location]
                        print(room_name.intro)
                    continue
                elif key == "restriction out":
                    if value not in locations.inventory:
                        print(result.get(command)["message1"])
                    elif value in locations.inventory:
                        print(result.get(command)["message2"])
                        player_location = result.get(command)["new location"]
                        room_name = rooms[player_location]
                        print(room_name.intro)
                    continue
                elif key == "message":
                    print(result.get(command)["message"])
                elif key == "points":
                    points += result.get(command)["points"]
                elif key == "add":
                    if value not in locations.inventory:
                        locations.inventory.append(value)
                    elif value in locations.inventory:
                        print("You already have that.")
                elif key == "remove":
                    if value in locations.inventory:
                        locations.inventory.remove(value)
                    elif value not in locations.inventory:
                        print("You don't have that.")
                elif key == "location":
                    player_location = result.get(command)["location"]
                    room_name = rooms[player_location]
                    print(room_name.intro)
                continue
        elif command in result.keys():
            print(result[command])    
            continue
    except KeyError as err:
        if command == 'HELP':
            show_help()
            continue
        elif command == 'SCORE':
            print("Score:", points)
            continue
        elif command == 'INVENTORY':
            for item in locations.inventory:
                print(item)
                continue
        elif command == 'SAVE':
            pass  # Find way to save game
        elif command == 'LOOK':
            print(room_name.intro)
            continue
        elif command == 'QUIT':
            break
        elif command == 'LOCATION':
            room_name.print_location()
            continue
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
    