class Rocket:
    """
    A simple rocket class. The pointy end goes up ^^^
    """

    def __init__(self, name, owner, status="Idle", accelX=0, accelY=0, accelZ=0, velocity=0, gyroX=0, gyroY=0, gyroZ=0, altitude=0):
        self.name = name
        self.owner = owner
        self.status = status
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ
        self.velocity = velocity
        self.gyroX = gyroX
        self.gyroY = gyroY
        self.gyroZ = gyroZ
        self.altitude = altitude

    def arm(self):
        # Arms the rocket for launch
        self.status = 'Armed'
        print(self.status)
        print(self.name + ' has been armed')

    def disarm(self):
        # Disarms the rocket
        self.status = 'Idle'
        print(self.status)
        print(self.name + ' has been disarmed')

    def launch(self):
        # Launches the rocket
        self.status = 'Going Up'
        print(self.status)
        print(self.name + ' has launched')
