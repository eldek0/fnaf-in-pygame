import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyFreddy(Animatronic):
    def __init__(self, App, activated=True):
        super().__init__(activated=activated, locationId=9, jumpscare_animation=None, rest_room=9)

    def movement(self, App):
        if self.locationId == 9:
            if pygame.time.get_ticks() - self.timer > 5000:
                # Moves to Game Area
                self.change_location_id(App, 10)

        if self.locationId == 10:
            if pygame.time.get_ticks() - self.timer > 3000:
                self.change_office_position(1)

        if self.officeLocation == 1:
            if pygame.time.get_ticks() - self.timer > 2000:
                self.change_location_id(App, 2)

        
                
