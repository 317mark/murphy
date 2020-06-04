from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip = True


class Camera:
    """

    """

    def __init__(self, resolution, vflip=False, hflip=False)
