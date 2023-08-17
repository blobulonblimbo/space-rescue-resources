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
        image = self.load_image("Bomb1.png")
        self.set_image(image,50,49)
        angle = random.randint(135,225)
        self.set_direction(angle, 10)
        self.listy = 0
        self.damage = 1
        self.exploded = False
        self.register_collision_object("Ship")
        self.register_collision_object("lazers")


    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            if self.exploded == False:
                other.HP -= 1
                self.image = self.load_image("Bomb2.png")
                self.set_image(self.image,60,50)
                self.exploded = True
                self.x_speed = 0
                self.y_speed = 0
            self.set_timer(10,self.delete_asteroid)
        if other_type == "lazers":
            if self.exploded == False:
                self.image = self.load_image("Bomb2.png")
                self.set_image(self.image,60,50)
                self.exploded = True
                self.x_speed = 0
                self.y_speed = 0
                self.set_timer(10,self.delete_asteroid)
            
            
            #if Globals.Ship_HP < 1:
                #self.room.running = False
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    def delete_asteroid(self):
        self.room.delete_object(self)
    def step(self):
        self.keep_in_room()
        
                     

class Homing_Asteroid(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Homing_eye.png")
        self.set_image(image,50,49)
        angle = self.curr_rotation
        #self.x = Globals.Ship_x
        self.set_direction(angle, 10)
    def keep_in_room(self):
        self.room.delete_object(self)
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
        self.set_direction(0, 50)
        self.damage = 10
        self.listy = 0
        self.exploded = False
        self.register_collision_object("Zork")
        self.register_collision_object("Nyan")
        self.register_collision_object("Asteroid")

    def handle_collision(self, other, other_type):
       
        
        if other_type == "Zork":
            if self.exploded == False:
                self.image = self.load_image("bullet2.png")
                Globals.Zork_HP -= 500
                self.set_image(self.image,40,40)
                self.exploded = True
                self.x_speed = 0
                self.y_speed = 0
        elif other_type == "Nyan":
            if self.exploded == False:
                self.image = self.load_image("bullet2.png")
                Globals.Nyan_HP -= 5000
                self.set_image(self.image,40,40)
                self.exploded = True
                self.x_speed = 0
                self.y_speed = 0
    
        elif other_type == "Asteroid":
            self.room.delete_object(other)
            self.room.score.update_score(5)
            self.room.delete_object(self)
        '''elif other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.score.update_score(-10)'''
        self.image = self.load_image("bullet2.png")
        self.set_image(self.image,40,40)

        self.set_timer(10,self.delete_lazer)

    
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.room.delete_object(self)
    def delete_lazer(self):
        self.room.delete_object(self)
        
    def step(self):

        '''if self.x > Globals.Zork_x and self.y >= Globals.Zork_y - 0 and self.y <= Globals.Zork_y + 350:
            self.listy += 1
            self.image = self.load_image("bullet2.png")
            self.set_image(self.image,40,40)
            Globals.Zork_HP -= self.damage
            self.x_speed = 0
            if self.listy > 2:
                self.room.delete_object(self)'''
class Rainbow(RoomObject):
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
        image = self.load_image("rainbow_trail.png")
        self.set_image(image,150,50)
        angle = 180
        self.set_direction(angle, 10)
        self.damage = 1
        self.exploded = False
        self.register_collision_object("Ship")

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            if self.exploded == False:
                other.HP -= 1
                
                self.exploded = True
            
            #if Globals.Ship_HP < 1:
                #self.room.running = False
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1
    def delete_rainbow(self):
        self.room.delete_object(self)
    def step(self):
        self.keep_in_room()
        if self.x < -100:
            self.room.delete_object(self)
        
class Bouncing_Rainbow(RoomObject):
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
        image = self.load_image("rainbow_trail.png")
        self.set_image(image,150,50)
        angle = 180
        self.set_direction(angle, 1)
        self.damage = 1
        self.exploded = False
        self.register_collision_object("Ship")
        self.big = 1
        self.check = True

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            if self.exploded == False:
                other.HP -= 1
                
                self.exploded = True
            
            #if Globals.Ship_HP < 1:
                #self.room.running = False
    def keep_in_room(self):
        
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed = -5
            self.check = False
            self.set_timer(120,self.reset)
    def delete_rainbow(self):
        self.room.delete_object(self)
    def step(self):
        self.keep_in_room()
        if self.x < -100:
            self.room.delete_object(self)
        self.angle += self.big
        if self.angle >= 360:
            self.big = -5
        self.rotate_to_coordinate(self.angle,self.angle)
        self.x_speed = -10
        if self.check == True:

            self.y_speed += 0.2
        self.x_speed = -3
    def reset(self):
        self.check = True
class Custom_Rainbow(RoomObject):
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
        image = self.load_image("rainbow_trail.png")
        self.set_image(image,150,50)
        angle = 90
        self.set_direction(angle, 0)
        self.damage = 1
        self.exploded = False
        self.register_collision_object("Ship")
        self.rotate(90)
        self.cust = True

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Ship":
            if self.exploded == False:
                other.HP -= 1
                
                self.exploded = True
            
            #if Globals.Ship_HP < 1:
                #self.room.running = False
    
    def delete_rainbow(self):
        self.room.delete_object(self)
    def step(self):
        if self.y_speed != 10 and self.cust == True:
            self.y_speed += 0.2
            print(self.y_speed)
        if self.y_speed == 10:
            self.set_timer(1,self.truth)
        
        if self.cust == False and self.y_speed != 0:
            self.y_speed -= 0.2
        if self.y_speed == 0:
            self.set_timer(1,self.truth)

        if self.x < -100:
            self.room.delete_object(self)
    def truth(self):
        if self.cust == True:
            self.cust = False
        if self.cust == False:
            self.cust = True
        
        
            