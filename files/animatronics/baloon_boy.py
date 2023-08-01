import pygame, random

from files.animatronics.animatronic_base import Animatronic

class BaloonBoy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int):
        super().__init__(aggresivity, 10, None, 10, custom_index)

    def movement(self, App):
        match self.locationId:
            case 10:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 103)

            case 103:
                if self.time_with_mask > self.movement_time / self.aggresivity and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, -1, forced=True)

                if App.objects.mask_button.inMask:
                    self.time_with_mask += 1
                    print(self.time_with_mask)
                if self.time_with_mask >= self.time_with_mask_goal:
                    self.change_location_id(App, self.rest_room)

            case -1:
                if pygame.time.get_ticks() - self.timer > 15000 and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, 0, forced=True)