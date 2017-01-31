import readline
import CommandCenter

class UI():
    def __init__(self):
        pass

cc = CommandCenter


ehto = True
while ehto:
    output = raw_input("Command: ").lower()
    #for value in cc.commands
    if output == "quit":
        ehto = False