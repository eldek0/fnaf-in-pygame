import pygame
from files.animatronics.animatronic_base import Animatronic

class WitheredFreddy(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 8, App.animations.toy_chica_jump)

    def movement(self, App):
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 7)

            case 7:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 3)

            case 3:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 101)

            case 101:
                if pygame.time.get_ticks() - self.timer > 5000 and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, 104)