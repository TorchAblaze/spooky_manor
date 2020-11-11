class Room():
    def __init__(self, name, commands, intro):
        self.name = name
        self.commands = commands
        self.intro = intro

    def print_location(self):
        print(f"You are at: {self.name}.")