import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyBunny(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 9, App.animations.toy_bunny_jump, 3)

    def movement(self, App):
        match self.locationId:
            case 9:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 3)

            case 3:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 4)

            case 4:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 2)

            case 2:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 6)

            case 6:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 102)

            case 102:
                if pygame.time.get_ticks() - self.timer > 5000 and (App.objects.open_monitor_button.inCamera or App.objects.mask_button.inMask):
                    self.change_location_id(App, 104)
                    