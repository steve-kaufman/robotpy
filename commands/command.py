_commands = []

class Command:
    def __init__(self, robot):
        _commands.append(self)
        self.initialize()
        self.robot = robot
    def initialize(self):
        pass
    def execute(self):
        pass
    def isFinished(self):
        return False

def run_commands():
    for i, command in enumerate(_commands):
        if command.isFinished():
            del _commands[i]
        else:
            command.execute()
