import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyChica(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 9, App.animations.toy_chica_jump)

    def movement(self, App):
        match self.locationId:
            case 9:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 7)

            case 7:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 4)

            case 4:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 1)

            case 1:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 101)

            case 101:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 103)

            case 103:
                if pygame.time.get_ticks() - self.timer > 5000 and App.objects.open_monitor_button.inCamera:
                    self.jumpscare()
                if App.objects.mask_button.inMask:
                    self.time_with_mask += 1
                    print(self.time_with_mask)
                if self.time_with_mask >= self.time_with_mask_goal:
                    self.change_location_id(App, 4)