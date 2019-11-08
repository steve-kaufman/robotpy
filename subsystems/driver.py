import wpilib
import wpilib.drive
import robotmap
from commands.drive import Drive

def _process_input(num):
    if(num == 0):
        return 0
    sign = num / abs(num)
    return num * num * sign * 0.65

class Driver:
    def __init__(self, robot):
        Drive(robot)
        self.left_motor = wpilib.Spark(robotmap.LEFT_MOTOR)
        self.right_motor = wpilib.Spark(robotmap.RIGHT_MOTOR)
        self.drive = wpilib.drive.DifferentialDrive(
            self.left_motor,
            self.right_motor
        )
    def drive_robot(self, y, x):
        y = _process_input(y)
        x = _process_input(x)
        self.drive.arcadeDrive(-y, x)
