import os

from files.animatronics.toy_freddy import ToyFreddy
from files.animatronics.puppet import Puppet
from files.animatronics.toy_bunny import ToyBunny
from files.animatronics.toy_chica import ToyChica
from files.animatronics.withered_freddy import WitheredFreddy
from files.animatronics.withered_bonnie import WitheredBonnie
from files.animatronics.withered_chica import WitheredChica

class AnimatronicsMain:
    def __init__(self, App):

        self.animatronics_in_game = {
            "TOY_FREDDY":ToyFreddy(App, activated=True), 
            "PUPPET":Puppet(App, activated=True),
            "TOY_BUNNY":ToyBunny(App, activated=True),
            "TOY_CHICA":ToyChica(App, activated=True),
            "WITHERED_BONNIE":WitheredBonnie(App, activated=True),
            "WITHERED_CHICA":WitheredChica(App, activated=True),
            "WITHERED_FREDDY":WitheredFreddy(App, activated=True)
        }
        self.gameOver = False

    def console_animatrionic_position_log(self):
        os.system("cls")
        keys = list(self.every_animatrionic_position.keys())
        for i in range(len(self.every_animatrionic_position)):
            animatrionics_in_position = self.every_animatrionic_position[keys[i]]
            anim_in_position_name = ""
            for anim in animatrionics_in_position:
                anim_in_position_name += f"{anim.name_id} / {anim.rest_room}"
                if anim.changing_position:
                    anim_in_position_name += " (changing)"

                anim_in_position_name += " - "

            print(f"{keys[i]} : {anim_in_position_name}")

    def update_animatrionic_position(self):
        self.every_animatrionic_position = {
            -1:[],0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[],
            8:[], 9:[], 10:[], 11:[], 12:[], 101:[], 102:[],
            103:[], 104:[]
        }

        keys = list(self.animatronics_in_game.keys())

        # Add every animatrionic to the "every _animatrionic_position" list
        for i in range(len(self.animatronics_in_game)):
            animatronic = self.animatronics_in_game[keys[i]]
            self.every_animatrionic_position[animatronic.locationId].append(animatronic)

    def update(self, App):
        keys = list(self.animatronics_in_game.keys())
        # Update the animatrionics
        for j in range(len(self.animatronics_in_game)):
            self.update_animatrionic_position()
            animatronic = self.animatronics_in_game[keys[j]]
            animatronic.name_id = keys[j]
            animatronic.update(App)
            game_over= animatronic.isGameOver()
            if game_over:
                self.game_over()

        self.console_animatrionic_position_log()

    def game_over(self):
        self.gameOver = True