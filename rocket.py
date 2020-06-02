class Rocket:
    """
    A simple rocket class. The pointy end goes up ^^^
    """

    def __init__(self, name, owner, stages, status="Inert", acceleration=0, velocity=0, orientation=0, altitude=0):
        self.name = name
        self.owner = owner
        self.stages = stages
        self.status = status
        self.acceleration = acceleration
        # self.accelX = accelX
        # self.accelY = accelY
        # self.accelZ = accelZ
        self.velocity = velocity
        self.orientation = orientation
        self.altitude = altitude

    def arm(self):
        # Desc - Arms the rocket for launch

        # Arm the rocket
        self.status = "Armed"
        # Change rocket status to "Armed" and alert owner of status change
        print("Rocket is " + self.status)

    def launch(self):
        # Desc - Launches the rocket

        # Fire electrical charge inside the motor chamber

        # Capture date and time of launch

        # Change rocket status to "Flying" and alert owner of status change
        print("Rocket has launched!")

    def set_acceleration(self):
        # Desc - Sets the rocket's current acceleration... not sure if this is a valuable method yet.
        print("Acceleration set to " + self.acceleration)
        self.acceleration = 1
