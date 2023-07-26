from GameFrame import RoomObject
import random
from GameFrame import Globals 
class Asteroid(RoomObject):
    """
    A class for Zorks danerous obstacles
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Asteroid object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("asteroid.png")
        self.set_image(image,50,49)
        angle = random.randint(135,225)
        self.set_direction(angle, 10)
class Homing_Asteroid(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Zork.png")
        self.set_image(image,50,49)
        angle = random.randint(135,225) 
        #self.x = Globals.Ship_x
        self.set_direction(angle, 10)


        def step(self):
            self.y = Globals.Ship_y

class lazers(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Zork.png")
        self.set_image(image,5,10)
        angle = random.randint(135,225) 
        #self.x = Globals.Ship_x
        self.set_direction(0, 10)
