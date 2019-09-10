import wpilib
import robotmap

class Oi:
    def __init__(self):
        self.stick = wpilib.Joystick(robotmap.JOYSTICK)
