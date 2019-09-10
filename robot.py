import wpilib
from commands import command
from oi import Oi
from subsystems.driver import Driver

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.oi = Oi()
        self.driver = Driver(self)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        command.run_commands()

if __name__ == "__main__":
    wpilib.run(MyRobot)
