import math
from GameFrame import RoomObject
import random
from GameFrame import Globals 
from Objects import Ship
import time
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
        image = self.load_image("Bomb1.png")
        self.set_image(image,50,49)
        angle = random.randint(135,225)
        self.set_direction(angle, 10)
        self.listy = 0
        self.damage = 1
        self.register_collision_object("Ship")

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            Globals.Ship_HP -= 1
            if Globals.Ship_HP < 1:
                self.room.running = False
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1

    def step(self):
        self.keep_in_room()
        if self.x < Globals.Ship_x + 50 and self.y >= Globals.Ship_y - 50 and self.y <= Globals.Ship_y + 100:
            self.listy += 1
            self.image = self.load_image("Bomb2.png")
            self.set_image(self.image,60,50)
            self.x_speed = 0
            if self.listy > 2:
                self.room.delete_object(self)
class Homing_Asteroid(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Homing_eye.png")
        self.set_image(image,50,49)
        angle = self.curr_rotation
        #self.x = Globals.Ship_x
        self.set_direction(angle, 10)
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            print("J")


    def step(self):
        self.rotate_to_coordinate(Globals.Ship_x,Globals.Ship_y)
        self.set_direction(self.curr_rotation,10)
class lazers(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("bullet1.png")
        self.set_image(image,30,15)
        #self.x = Globals.Ship_x
        self.set_direction(0, 50)
        self.damage = 10
        self.listy = 0
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.room.delete_object(self)
    def step(self):
        if self.x > Globals.Zork_x and self.y >= Globals.Zork_y - 0 and self.y <= Globals.Zork_y + 350:
            self.listy += 1
            self.image = self.load_image("bullet2.png")
            self.set_image(self.image,40,40)
            Globals.Zork_HP -= self.damage
            self.x_speed = 0
            if self.listy > 2:
                self.room.delete_object(self)
            