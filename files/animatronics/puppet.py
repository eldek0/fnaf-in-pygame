import pygame

from files.animatronics.animatronic_base import Animatronic

class Puppet(Animatronic):
    def __init__(self, App, activated=True):
        super().__init__(activated=activated, locationId=11, jumpscare_animation=App.animations.puppet_jump, rest_room=None)

    def movement(self, App):
        if App.objects.music_box.charge == 0:
            if self.secondPositionId == 1:
                self.change_location_id(App, 11, secondPositionId=2)
                    
            elif self.secondPositionId == 2:
                if pygame.time.get_ticks() - self.timer > 4000:
                    self.change_location_id(App, 11, secondPositionId=3)

            elif self.secondPositionId == 3:
                if pygame.time.get_ticks() - self.timer > 4000:
                    self.jumpscare(App)

        elif App.objects.music_box.charge != 0:
            self.timer = pygame.time.get_ticks()
        