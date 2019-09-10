from commands.command import Command

class Drive(Command):
    def execute(self):
        driver = self.robot.driver

        y = self.robot.oi.stick.getY()
        x = self.robot.oi.stick.getX()

        driver.drive(y, x)
