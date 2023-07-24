import pygame, random

from files.animatronics.animatronic_base import Animatronic

class BaloonBoy(Animatronic):
    def __init__(self, App, activated:int=True):
        super().__init__(activated, 10, None, 10)
        self.time_to_scare = random.randint(12000, 30000)

    def movement(self, App):
        match self.locationId:
            case 10:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > 5000:
                    self.change_location_id(App, 103)

            case 103:
                if pygame.time.get_ticks() - self.timer > 7000 and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, -1, forced=True)

                if App.objects.mask_button.inMask:
                    self.time_with_mask += 1
                if self.time_with_mask >= self.time_with_mask_goal:
                    self.change_location_id(App, self.rest_room)

            case -1:
                if pygame.time.get_ticks() - self.timer > 10 and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, 0, forced=True)