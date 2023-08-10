
from GameFrame import RoomObject, Globals
import random
from Objects.Asteroid import Asteroid,Homing_Asteroid, lazers, Rainbow
from Objects.Nyan import Nyan
class Zork(RoomObject):
    HP = 1000
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
        image = self.load_image("big_boss.png")
        self.set_image(image,340,460)
        self.y_speed = random.choice([-5,5])
        #self.x_speed = random.choice([-3,3])
        asteroid_spawn_time = random.randint(15,150)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        homing_asteroid_spawn_time = random.randint(15,150)
        self.set_timer(homing_asteroid_spawn_time, self.spawn_homing_asteroid)
        self.fire = True
        self.change = 10
        self.num = 1
        self.x = 1000
        self.animate = 1
        self.HP = 1000
        self.dead = False
        self.stage = 150
        self.rate = 75
        self.arg = True
        self.trun = True
        


        
        

    def keep_in_room(self):
        """
        Keeps the Zork inside the top and bottom room limits
        """
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
       
        '''if self.x_speed < 0:
            self.x_speed += 0.25
        if self.x_speed > 0:
            self.x_speed -= 0.25
        if self.x + 50 > Globals.SCREEN_WIDTH:
            self.x_speed -= 0.2
        if self.x + -50 < 0:
            self.x_speed += 0.2
        if self.x_speed == 0:
            self.x_speed = random.choice([-3,3])
        if self.x < 0 or self.x > Globals.SCREEN_WIDTH - self.width:
            self.x_speed *= -1'''
           

            
            
    def step(self):
        """
        Determine what happens to the Dragon on each tick of the game clock
        """
        self.keep_in_room()
        Globals.Zork_x = self.x
        Globals.Zork_y = self.y
        if Globals.Zork_HP <= 0:
            self.y_speed = 0
            self.x_speed = 0
            self.num += 1
        elif Globals.Zork_HP <= 700 and Globals.Zork_HP > 333:
            self.stage = 100
            self.rate = 30
        elif Globals.Zork_HP <= 500 and Globals.Zork_HP > 200:
            self.stage = 50
            self.rate = 15
        if Globals.Zork_HP < 200:
            self.stage = 20
            self.rate = 10
            
            
        if self.num > 50:
            self.image = self.load_image(f"explosion{self.animate}.png")
            self.animate += 1
            self.num = 0
            self.dead = True
            if self.animate == 7:
                self.animate = 0
                self.num = 200

            self.set_image(self.image,340,460)
            if self.num >= 200:
                Globals.Phase = 2
                self.room.delete_object(self)
        
    def spawn_homing_asteroid(self):
        if self.dead == False:
            new_homing_asteroid = Homing_Asteroid(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_homing_asteroid)

            homing_asteroid_spawn_time = random.randint(15,150)
            self.set_timer(homing_asteroid_spawn_time, self.spawn_homing_asteroid)
    def spawn_asteroid(self):
        if self.dead == False:
            """
            Randomly spawns a new Asteroid
            """
            # spawn Asteroid and add to room
            new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
            self.room.add_room_object(new_asteroid)
                    
                    # reset time for next Asteroid spawn\
                    

            asteroid_spawn_time = random.randint(self.rate, self.stage)
            self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
    
        
    

class Health_Bar(RoomObject):
    def __init__(self, room, x, y):
        
        RoomObject.__init__(self, room, x, y)
        
        
        image = self.load_image("HP.png")
        self.set_image(image,Globals.Zork_HP,30)
        self.x = 200
        self.y = 700
    def step(self):
        image = self.load_image("HP.png")
        if Globals.Zork_HP - 10 > 0:
            self.set_image(image,Globals.Zork_HP,30)
        else:
            self.set_image(image,0,0)



    

        

            