import pygame
from files.animatronics.animatronic_base import Animatronic

class WitheredFreddy(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 8, App.animations.withered_freddy_jump, 7)

    def movement(self, App):
        withered_chica = App.objects.Animatronics.animatronics_in_game["WITHERED_CHICA"]
        withered_bonnie = App.objects.Animatronics.animatronics_in_game["WITHERED_BONNIE"]

        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > 5000:
                    if withered_chica.locationId != 8 and withered_bonnie.locationId != 8:
                        self.change_location_id(App, 7)
                    else:
                        self.timer = pygame.time.get_ticks()

            case 7:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 3)

            case 3:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 101)

            case 101:
                if pygame.time.get_ticks() - self.timer > 5000 and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, 104)