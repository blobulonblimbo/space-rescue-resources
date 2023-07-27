from GameFrame import Globals, RoomObject
import pygame
from Objects.Asteroid import lazers
import time
class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)

        # register events
        self.handle_key_events = True
        self.fire_rate = 0
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_w]:
            if self.y_speed > -5:
                self.y_speed -= 0.1
        else:
            if self.y_speed < 0:
                self.y_speed += 0.1
        if key[pygame.K_s]:
            if self.y_speed < 5:
                self.y_speed += 0.1
        else:
            if self.y_speed > 0:
                self.y_speed -= 0.1
        if key[pygame.K_a]:
            if self.x_speed > -5:
                self.x_speed -= 0.1
        else:
            if self.x_speed < 0:
                self.x_speed += 0.1
        if key[pygame.K_d]:
            if self.x_speed < 5:
                self.x_speed += 0.1
        else:
            if self.x_speed > 0:
                self.x_speed -= 0.1
    
        if key[pygame.K_SPACE]:
            self.shoot()
        Globals.Ship_x = self.x
        Globals.Ship_y = self.y
        
        
        
    def keep_in_room(self):
        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height
    def step(self):
        """
        Determine what happens to the Ship on each click of the game clock
        """
        self.keep_in_room()
        self.fire_rate += 1
    def shoot(self):
        if self.fire_rate > 10:
            new_lazer = lazers(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_lazer)
            self.fire_rate = 0
        
        
        