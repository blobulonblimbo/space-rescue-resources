
from GameFrame import RoomObject, Globals
from Objects.Asteroid import Rainbow, Bouncing_Rainbow
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
        self.HP = 50
        self.stage = 1
        self.met = 0
        self.yes = False
        self.rate = 50
        self.wiper = True
        
        #self.x_speed = random.choice([-3,3])
        
        rainbow_spawn_time = 50
        bouncing_rainbow_spawn_time = 100
        self.set_timer(rainbow_spawn_time, self.spawn_rainbow)
        self.set_timer(bouncing_rainbow_spawn_time, self.spawn_bouncing_rainbow)
        



    def step(self):
        self.keep_in_room()
        
        
        self.Wiper()
        if Globals.Nyan_HP <= 0:
            self.room.delete_object(self)
        
    def Wiper(self):
        
        if self.wiper == True:
            self.met = random.choice([0,Globals.SCREEN_HEIGHT - self.height])
            self.y = self.met
            if self.y == 0:
                self.y_speed = 5
            if self.y == Globals.SCREEN_HEIGHT - self.height:
                self.y_speed = -5
            self.rate = 3
            self.wiper = False
            self.set_timer(random.randint(300,1000),self.reset)
    
        
    def reset(self):
        self.wiper = True
    def reset_rate(self):
        self.rate = 50
        

        

    def spawn_rainbow(self):
        
            new_rainbow = Rainbow(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_rainbow)
            
            # reset time for next Asteroid spawn\
            

            asteroid_spawn_time = random.randint(2,self.rate)
            self.set_timer(asteroid_spawn_time, self.spawn_rainbow)
    def spawn_bouncing_rainbow(self):
        
            new_bouncing_rainbow = Bouncing_Rainbow(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_bouncing_rainbow)
            
            # reset time for next Asteroid spawn\
            

            asteroid_spawn_time = random.randint(50,100)
            self.set_timer(asteroid_spawn_time, self.spawn_bouncing_rainbow)
    def keep_in_room(self):
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
            self.reset_rate()
            self.go = self.y_speed
    
       