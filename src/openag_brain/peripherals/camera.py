import time
import picamera
import numpy as np

class Camera(object):

    def __init__(self):
        self.width = 640
        self.height = 480
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.width, self.height)
        self.camera.framerate = 24
        self.image = np.empty((self.width*self.height*3,), dtype=np.uint8)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.camera.close()

        
    def capture(self):
        self.image = self.image.reshape((self.width*self.height*3,))
        self.camera.capture(self.image, 'rgb')
        self.image = self.image.reshape((self.height,self.width,3))
        return self.image
