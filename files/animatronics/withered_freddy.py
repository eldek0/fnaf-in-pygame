import pygame
from files.animatronics.animatronic_base import Animatronic

class WitheredFreddy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity, 8, App.animations.withered_freddy_jump, 7, custom_index, img_show=img_show)

    def movement(self, App):
        withered_chica = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]
        withered_bonnie = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    if (withered_chica.locationId != 8 and withered_bonnie.locationId != 8) or App.menu.nightToPlay == 7:
                        self.change_location_id(App, 7)
                    else:
                        self.timer = pygame.time.get_ticks()

            case 7:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 3)

            case 3:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 101)

            case 101:
                self.interrupt_in_office(App)