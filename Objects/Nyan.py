
from GameFrame import RoomObject, Globals
from Objects.Asteroid import Rainbow
import random

class Nyan(RoomObject):
    """
    A class for the game's antagoist
    """
    def __init__(self, room, x, y):
        """
        Initialise the Boss object
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Nyan_Cat.png")
        self.set_image(image,340,260)
        self.y_speed = 5
        self.x = 1000
        self.HP = 10000
        #self.x_speed = random.choice([-3,3])
        
        rainbow_spawn_time = 50
        self.set_timer(rainbow_spawn_time, self.spawn_rainbow)
        



    def step(self):
         self.keep_in_room()
         if Globals.Phase == 2:
              self.y = 50
              self.x = 1000
              Globals.Phase = 0
        

    def spawn_rainbow(self):
        
            new_rainbow = Rainbow(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_rainbow)
            
            # reset time for next Asteroid spawn\
            

            asteroid_spawn_time = random.randint(2,50)
            self.set_timer(asteroid_spawn_time, self.spawn_rainbow)
    def keep_in_room(self):
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
       