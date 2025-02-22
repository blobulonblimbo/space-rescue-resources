from GameFrame import Level
from Objects.Ship import Ship
from Objects.Zork import Zork, Health_Bar
from Objects.Nyan import Nyan
from GameFrame import Globals
from Objects.Hud import Score
class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Background.png")

        # add objects
        self.add_room_object(Ship(self, 25, 50))
        self.add_room_object(Zork(self,1120, 50))
        self.add_room_object(Health_Bar(self,Globals.Zork_HP,20))
    # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)
    
