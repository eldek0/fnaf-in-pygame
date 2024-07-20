# Nights controller

import pygame, random

class NightAIChanger:
    def __init__(self, App):
        self.animatronics_ai = {}
        self.animatronics = App.objects.Animatronics.animatronics_in_game
        self.animatronics_keys = self.animatronics.keys()
        self.get_ais()
        self.time = 0

    def get_ais(self):
        for key in self.animatronics_keys:
            self.animatronics_ai[key] = self.animatronics[key].aggresivity

    def update_ai(self):
        for key in self.animatronics_keys:
            self.animatronics[key].aggresivity = self.animatronics_ai[key]

    def update(self, App, nightToPlay:int, realTimeMode:bool=False):
        self.time = App.objects.gameTimer.times[0]
        if not realTimeMode:
            match nightToPlay:
                case 1:
                    self.night_1()
                case 2:
                    self.night_2()
                case 3:
                    self.night_3()
                case 4:
                    self.night_4()
                case 5:
                    self.night_5()
                case 6:
                    self.night_6()
                case 7:
                    self.night_7(App)
                case _:
                    print("No AI configured!")
        else:
            self.real_time_night()

        self.update_ai()

    def night_1(self):

        match self.time:
            case 12:
                pass

            case 1: 
                self.animatronics_ai["TOY_BONNIE"] = 2

            case 2:
                self.animatronics_ai["TOY_FREDDY"] = 1
                self.animatronics_ai["TOY_CHICA"] = 2
                self.animatronics_ai["PUPPET"] = 1

            case 3:
                self.animatronics_ai["TOY_BONNIE"] = 3

            case 4: pass

            case 5: pass

    def night_2(self):
        self.animatronics_ai["PUPPET"] = 5
        self.animatronics_ai["MANGLE"] = 3
        self.animatronics_ai["TOY_CHICA"] = 3
        self.animatronics_ai["TOY_BONNIE"] = 3
        self.animatronics_ai["TOY_FREDDY"] = 2
        self.animatronics_ai["BALOON_BOY"] = 3
        self.animatronics_ai["FOXY"] = 1

    def night_3(self):

        match self.time:
            case 12:
                self.animatronics_ai["WITHERED_BONNIE"] = 1
                self.animatronics_ai["WITHERED_CHICA"] = 1
                self.animatronics_ai["FOXY"] = 2
                self.animatronics_ai["BALOON_BOY"] = 1
                self.animatronics_ai["PUPPET"] = 8

            case 1: 
                self.animatronics_ai["WITHERED_FREDDY"] = 2
                self.animatronics_ai["WITHERED_BONNIE"] = 3
                self.animatronics_ai["WITHERED_CHICA"] = 2
                self.animatronics_ai["FOXY"] = 3
                self.animatronics_ai["BALOON_BOY"] = 2
                self.animatronics_ai["TOY_BONNIE"] = 1
                self.animatronics_ai["TOY_CHICA"] = 1

            case 2:
                pass

            case 3:
                pass

            case 4: pass

            case 5: pass

    def night_4(self):

        match self.time:
            case 12:
                self.animatronics_ai["WITHERED_BONNIE"] = 1
                self.animatronics_ai["FOXY"] = 7
                self.animatronics_ai["BALOON_BOY"] = 3
                self.animatronics_ai["MANGLE"] = 5
                self.animatronics_ai["PUPPET"] = 9

            case 1: 
                pass

            case 2:
                self.animatronics_ai["WITHERED_FREDDY"] = 3
                self.animatronics_ai["WITHERED_CHICA"] = 4
                self.animatronics_ai["WITHERED_BONNIE"] = 4
                self.animatronics_ai["TOY_BONNIE"] = 1

            case 3:
                pass

            case 4: pass

            case 5: pass

    def night_5(self):

        match self.time:
            case 12:
                self.animatronics_ai["WITHERED_FREDDY"] = 2
                self.animatronics_ai["WITHERED_BONNIE"] = 2
                self.animatronics_ai["WITHERED_CHICA"] = 2
                self.animatronics_ai["FOXY"] = 5
                self.animatronics_ai["BALOON_BOY"] = 5
                self.animatronics_ai["TOY_FREDDY"] = 5
                self.animatronics_ai["TOY_BONNIE"] = 2
                self.animatronics_ai["TOY_CHICA"] = 2
                self.animatronics_ai["MANGLE"] = 1
                self.animatronics_ai["PUPPET"] = 10

            case 1: 
                self.animatronics_ai["WITHERED_FREDDY"] = 10
                self.animatronics_ai["WITHERED_BONNIE"] = 5
                self.animatronics_ai["WITHERED_CHICA"] = 5
                self.animatronics_ai["FOXY"] = 7
                self.animatronics_ai["TOY_FREDDY"] = 1
                self.animatronics_ai["MANGLE"] = 10

            case 2:
                pass

            case 3:
                pass

            case 4: pass

            case 5: pass

    def night_6(self):

        match self.time:
            case 12:
                self.animatronics_ai["WITHERED_FREDDY"] = 5
                self.animatronics_ai["WITHERED_BONNIE"] = 5
                self.animatronics_ai["WITHERED_CHICA"] = 5
                self.animatronics_ai["FOXY"] = 10
                self.animatronics_ai["BALOON_BOY"] = 5
                self.animatronics_ai["TOY_FREDDY"] = 0
                self.animatronics_ai["TOY_BONNIE"] = 0
                self.animatronics_ai["TOY_CHICA"] = 0
                self.animatronics_ai["MANGLE"] = 3
                self.animatronics_ai["PUPPET"] = 15
                self.animatronics_ai["GOLDEN_FREDDY"] = random.randint(1, 10)

            case 1: 
                self.animatronics_ai["GOLDEN_FREDDY"] = random.randint(1, 10)

            case 2:
                self.animatronics_ai["WITHERED_FREDDY"] = 10
                self.animatronics_ai["WITHERED_BONNIE"] = 10
                self.animatronics_ai["WITHERED_CHICA"] = 10
                self.animatronics_ai["FOXY"] = 15
                self.animatronics_ai["BALOON_BOY"] = 9
                self.animatronics_ai["TOY_FREDDY"] = 5
                self.animatronics_ai["TOY_BONNIE"] = 5
                self.animatronics_ai["TOY_CHICA"] = 5
                self.animatronics_ai["MANGLE"] = 10
                self.animatronics_ai["GOLDEN_FREDDY"] = 3

            case 3:
                pass

            case 4: pass

            case 5: pass

    def real_time_night(self):
        match self.time:
            case 12:
                self.animatronics_ai["WITHERED_FREDDY"] = 6
                self.animatronics_ai["WITHERED_BONNIE"] = 5
                self.animatronics_ai["WITHERED_CHICA"] = 6
                self.animatronics_ai["FOXY"] = 6
                self.animatronics_ai["BALOON_BOY"] = 6
                self.animatronics_ai["TOY_FREDDY"] = 6
                self.animatronics_ai["TOY_BONNIE"] = 6
                self.animatronics_ai["TOY_CHICA"] = 4
                self.animatronics_ai["MANGLE"] = 5
                self.animatronics_ai["PUPPET"] = 6
                self.animatronics_ai["GOLDEN_FREDDY"] = random.randint(3, 10)
            case 1:
                self.animatronics_ai["WITHERED_FREDDY"] = 8
                self.animatronics_ai["WITHERED_BONNIE"] = 6
                self.animatronics_ai["WITHERED_CHICA"] = 7
                self.animatronics_ai["FOXY"] = 10
                self.animatronics_ai["BALOON_BOY"] = 11
                self.animatronics_ai["TOY_FREDDY"] = 8
                self.animatronics_ai["TOY_BONNIE"] = 7
                self.animatronics_ai["TOY_CHICA"] = 9
                self.animatronics_ai["MANGLE"] = 7
                self.animatronics_ai["PUPPET"] = 8
                self.animatronics_ai["GOLDEN_FREDDY"] = 10
            case 2:
                self.animatronics_ai["WITHERED_FREDDY"] = 12
                self.animatronics_ai["WITHERED_BONNIE"] = 13
                self.animatronics_ai["WITHERED_CHICA"] = 14
                self.animatronics_ai["FOXY"] = 12
                self.animatronics_ai["BALOON_BOY"] = 12
                self.animatronics_ai["TOY_FREDDY"] = 12
                self.animatronics_ai["TOY_BONNIE"] = 11
                self.animatronics_ai["TOY_CHICA"] = 12
                self.animatronics_ai["MANGLE"] = 12
                self.animatronics_ai["PUPPET"] = 12
                self.animatronics_ai["GOLDEN_FREDDY"] = 11
            case 3:
                self.animatronics_ai["WITHERED_FREDDY"] = 15
                self.animatronics_ai["WITHERED_BONNIE"] = 15
                self.animatronics_ai["WITHERED_CHICA"] = 15
                self.animatronics_ai["FOXY"] = 12
                self.animatronics_ai["BALOON_BOY"] = 12
                self.animatronics_ai["TOY_FREDDY"] = 15
                self.animatronics_ai["TOY_BONNIE"] = 15
                self.animatronics_ai["TOY_CHICA"] = 15
                self.animatronics_ai["MANGLE"] = 15
                self.animatronics_ai["PUPPET"] = 20
                self.animatronics_ai["GOLDEN_FREDDY"] = 15
            case 4:
                pass
            case 5:
                pass

    def night_7(self, App):
        """ Get the data from custom night """
        for key in self.animatronics_keys:
            try:
                self.animatronics_ai[key] = App.menu.custom_night_menu.animatrionics_data[key]["aggresive"]
            except KeyError as e:
                self.animatronics_ai[key] = 20 # change
        