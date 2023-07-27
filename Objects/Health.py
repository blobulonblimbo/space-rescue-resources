from GameFrame import Globals
from GameFrame import RoomObject
class Health_Bar(RoomObject):
    def __init__(self, room, x, y):
        
        RoomObject.__init__(self, room, x, y)
        
        
        image = self.load_image("HP.png")
        self.set_image(image,Globals.Zork_HP,30)
        self.x = 200
        self.y = 700
    def step(self):
        image = self.load_image("HP.png")
        self.set_image(image,Globals.Zork_HP,30)