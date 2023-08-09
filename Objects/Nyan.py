
from GameFrame import RoomObject, Globals
from Objects.Asteroid import Rainbow

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
        image = self.load_image("Nyan.png")
        self.set_image(image,340,460)
        self.y_speed = 5
        self.x = 1000
        #self.x_speed = random.choice([-3,3])
        
        rainbow_spawn_time = 5
        self.set_timer(rainbow_spawn_time, self.spawn_rainbow)
        





def spawn_rainbow(self):
        """
        Randomly spawns a new Asteroid
        """
        # spawn Asteroid and add to room
        new_asteroid = Rainbow(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
            
            # reset time for next Asteroid spawn\
            

        asteroid_spawn_time = 2
        self.set_timer(asteroid_spawn_time, self.spawn_rainbow)

   