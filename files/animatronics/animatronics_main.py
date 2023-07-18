import os

from files.animatronics.toy_freddy import ToyFreddy
from files.animatronics.puppet import Puppet
from files.animatronics.toy_bunny import ToyBunny
from files.animatronics.toy_chica import ToyChica
from files.animatronics.withered_freddy import WitheredFreddy
from files.animatronics.withered_bonnie import WitheredBonnie

class AnimatronicsMain:
    def __init__(self, App):
        self.animatronics_in_game = {
            "TOY_FREDDY":ToyFreddy(App, activated=False), 
            "PUPPET":Puppet(App, activated=False),
            "TOY_BUNNY":ToyBunny(App, activated=False),
            "TOY_CHICA":ToyChica(App, activated=False),
            "WITHERED_FREDDY":WitheredFreddy(App, activated=True),
            "WITHERED_BONNIE":WitheredBonnie(App, activated=True)
        }
        self.gameOver = False

    def console_animatrionic_position_log(self):
        keys = list(self.every_animatrionic_position.keys())
        for i in range(len(self.every_animatrionic_position)):
            animatrionics_in_position = self.every_animatrionic_position[keys[i]]
            anim_in_position_name = ""
            for anim in animatrionics_in_position:
                anim_in_position_name += anim.name_id 
                if anim.changing_position:
                    anim_in_position_name += " (changing)"

                anim_in_position_name += " - "

            print(f"{keys[i]} : {anim_in_position_name}")

    def update(self, App):
        self.every_animatrionic_position = {
            -1:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[],
            8:[], 9:[], 10:[], 11:[], 12:[], 101:[], 102:[],
            103:[], 104:[]
        }

        keys = list(self.animatronics_in_game.keys())
        for i in range(len(self.animatronics_in_game)):
            animatronic = self.animatronics_in_game[keys[i]]
            animatronic.name_id = keys[i]
            animatronic.update(App)
            game_over= animatronic.isGameOver()
            if game_over:
                self.game_over()

            self.every_animatrionic_position[animatronic.locationId].append(animatronic)

        self.console_animatrionic_position_log()

    def game_over(self):
        self.gameOver = True