import pygame

from files.animatronics.animatronic_base import Animatronic

class WitheredBonnie(Animatronic):
    def __init__(self, App, aggresivity:int):
        super().__init__(aggresivity, 8, App.animations.withered_bonnie_jump, 7)

    def movement(self, App):
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 7)

            case 7:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 101)

            case 101:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity and App.objects.open_monitor_button.inCamera:
                    self.change_location_id(App, 104)