import pygame, random

from files.animatronics.animatronic_base import Animatronic

class BaloonBoy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int):
        super().__init__(aggresivity, 10, None, 10, custom_index)

    def movement(self, App):
        match self.locationId:
            case 10:
                if pygame.time.get_ticks() - self.timer > (self.movement_time + 96_000) / self.aggresivity:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 103)

            case 103:
                if pygame.time.get_ticks() - self.timer > self.vent_time_to_scare and App.objects.open_monitor_button.inCamera and not App.objects.office.animatronic_in_office:
                    self.change_location_id(App, -1, forced=True)

                if App.objects.mask_button.inMask:
                    self.time_with_mask += 1
                if self.time_with_mask >= self.time_with_mask_goal:
                    self.return_to_rest_room(App)

            case -1:
                if pygame.time.get_ticks() - self.timer > 10000 + (self.aggresivity*150) and App.objects.open_monitor_button.inCamera:
                    self.return_to_rest_room(App)