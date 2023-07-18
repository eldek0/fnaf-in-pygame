import pygame

from files.animatronics.animatronic_base import Animatronic

class WitheredBonnie(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 101, App.animations.toy_bunny_jump)

    def movement(self, App):
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 7)

            case 7:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 101)

            case 101:
                if self.secondPositionId == 1:
                    if pygame.time.get_ticks() - self.timer > 5000:
                        self.change_location_id(App, 101, secondPositionId=2)
                elif self.secondPositionId == 2:
                    if pygame.time.get_ticks() - self.timer > 5000 and App.objects.open_monitor_button.inCamera:
                        self.change_location_id(App, 104)