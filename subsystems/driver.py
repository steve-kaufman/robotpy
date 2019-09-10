import wpilib
import wpilib.drive
import robotmap
from commands.drive import Drive

class Driver:
    def __init__(self, robot):
        Drive(robot)
        self.left_motor = wpilib.Spark(robotmap.LEFT_MOTOR)
        self.right_motor = wpilib.Spark(robotmap.RIGHT_MOTOR)
        self.drive = wpilib.drive.DifferentialDrive(
            self.left_motor,
            self.right_motor
        )
    def drive(y, x):
        self.drive.arcadeDrive(y, x)
