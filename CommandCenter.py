class CommandCenter():

    def __init__(self):
        self.commands = []

    def add(self,string):
        self.commands.append(string)

uusi = CommandCenter()
uusi.add("Kissa")
print(uusi.commands)