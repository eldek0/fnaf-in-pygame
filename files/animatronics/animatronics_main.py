import os

from files.animatronics.toy_freddy import ToyFreddy
from files.animatronics.puppet import Puppet
from files.animatronics.toy_bonnie import ToyBonnie
from files.animatronics.toy_chica import ToyChica
from files.animatronics.withered_freddy import WitheredFreddy
from files.animatronics.withered_bonnie import WitheredBonnie
from files.animatronics.withered_chica import WitheredChica
from files.animatronics.foxy import Foxy
from files.animatronics.mangle import Mangle
from files.animatronics.baloon_boy import BaloonBoy
from files.animatronics.golden_freddy import GoldenFreddy

class AnimatronicsMain:
    def __init__(self, App):

        self.animatronics_in_game = {
            "TOY_FREDDY":ToyFreddy(App=App, aggresivity=0), 
            "PUPPET":Puppet(App=App, aggresivity=0),
            "TOY_BONNIE":ToyBonnie(App=App, aggresivity=0),
            "TOY_CHICA":ToyChica(App=App, aggresivity=0),
            "WITHERED_BONNIE":WitheredBonnie(App=App, aggresivity=0),
            "WITHERED_CHICA":WitheredChica(App=App, aggresivity=0),
            "WITHERED_FREDDY":WitheredFreddy(App=App, aggresivity=0),
            "FOXY":Foxy(App=App, aggresivity=0),
            "MANGLE":Mangle(App=App, aggresivity=0),
            "BALOON_BOY":BaloonBoy(App=App, aggresivity=0),
            "GOLDEN_FREDDY":GoldenFreddy(App=App, aggresivity=0)
        }
        self.gameOver = False
        self.being_jumpscared = False

        self.update_animatrionic_position()

    def console_animatrionic_position_log(self):
        #os.system("cls")
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
            animatronic = self.animatronics_in_game[keys[j]]
            if not self.being_jumpscared:
                self.update_animatrionic_position()
                animatronic.name_id = keys[j]
                animatronic.update(App)
            animatronic.jumpscare_update(App)
            game_over_ = animatronic.isGameOver()
            jumpscared_ = animatronic.isBeingJumpscared()
            if game_over_:
                self.game_over()
            if jumpscared_:
                self.jumpscared()

        #self.console_animatrionic_position_log()

    def game_over(self):
        self.gameOver = True

    def jumpscared(self):
        self.being_jumpscared = True