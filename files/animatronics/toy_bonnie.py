import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyBonnie(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int):
        super().__init__(aggresivity, 9, App.animations.toy_bunny_jump, 3, custom_index)
        self.mask_timer = pygame.time.get_ticks()

    def movement(self, App):

        match self.locationId:
            case 9:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 3)

            case 3:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 4)

            case 4:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 2)

            case 2:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 6)

            case 6:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 102)

            case 102:
                if (pygame.time.get_ticks() - self.timer > self.vent_time_to_scare and App.objects.open_monitor_button.inCamera):
                    self.change_location_id(App, 104)
                if App.objects.mask_button.inMask:
                    if (pygame.time.get_ticks() - self.mask_timer > 1500):
                        self.change_location_id(App, 104)
                else:
                    self.mask_timer = pygame.time.get_ticks()
                    