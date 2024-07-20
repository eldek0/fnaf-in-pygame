import pygame

from files.animatronics.animatronic_base import Animatronic

class WitheredBonnie(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity, 8, App.animations.withered_bonnie_jump, 7, custom_index, img_show=img_show)
        self.withered_timer = pygame.time.get_ticks()

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
                self.interrupt_in_office(App)