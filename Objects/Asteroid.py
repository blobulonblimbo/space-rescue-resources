import math
from GameFrame import RoomObject
import random
from GameFrame import Globals 
Delta = 0
Alpha = 0
angular = 0
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
        image = self.load_image("Homing_eye.png")
        self.set_image(image,50,49)
        angle = random.randint(135,225) 
        #self.x = Globals.Ship_x
        self.set_direction(angle, 10)


    def step(self):
        self.rotate_to_coordinate(Globals.Ship_x,Globals.Ship_y)
        '''if self.x >= Globals.Ship_x - 1000 and self.y >= Globals.Ship_y - 600:
            if self.y < Globals.Ship_y:
                if self.y_speed < 5:
                    self.y_speed += 0.25
            if self.y > Globals.Ship_y:
                if self.y_speed < -5:
                    self.y_speed -= 0.25
            if self.x < Globals.Ship_x:
                if self.x_speed < -15:
                    self.x_speed -= 0.25'''

class lazers(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Zork.png")
        self.set_image(image,5,10)
        #self.x = Globals.Ship_x
        self.set_direction(0, 50)
        self.damage = 10
    def step(self):
        if self.x >= Globals.Zork_x -50 and self.y >= Globals.Zork_y - 50:
            self.room.delete_object(self)
