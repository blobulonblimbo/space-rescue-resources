from GameFrame import RoomObject, Globals
import random
from Objects.Asteroid import Asteroid,Homing_Asteroid
class Zork(RoomObject):
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
        image = self.load_image("Zork.png")
        self.set_image(image,135,165)
        self.y_speed = random.choice([-5,5])
        self.x_speed = random.choice([-3,3])

        asteroid_spawn_time = random.randint(15,150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        homing_asteroid_spawn_time = random.randint(15,150)
        self.set_timer(homing_asteroid_spawn_time, self.spawn_homing_asteroid)
        

    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
       
        if self.x_speed < 0:
            self.x_speed += 0.25
        if self.x_speed > 0:
            self.x_speed -= 0.25
        
        if self.x_speed == 0:
            self.x_speed = random.choice([-3,3])
        if self.x < 1000 or self.x > Globals.SCREEN_WIDTH - self.width:
            self.x_speed *= -1
           

            
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
    def spawn_homing_asteroid(self):
        new_homing_asteroid = Homing_Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_homing_asteroid)

        homing_asteroid_spawn_time = random.randint(15,150)
        self.set_timer(homing_asteroid_spawn_time, self.spawn_homing_asteroid)
    def spawn_asteroid(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        
        # reset time for next Asteroid spawn\
        

        asteroid_spawn_time = random.randint(15, 150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)

    

        

            