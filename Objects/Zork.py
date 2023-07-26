from GameFrame import RoomObject, Globals
import random
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

    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
       
        if self.x_speed < 3:
            self.x_speed += 0.25
        if self.x_speed > -3:
            self.x_speed -= 0.25
        
        if self.x_speed == 0:
            self.x_speed = random.choice([-3,3])
           

            
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
            