import pygame

from files.animatronics.animatronic_base import Animatronic

class Puppet(Animatronic):
    def __init__(self, App, activated=True):
        super().__init__(activated=activated, locationId=11, jumpscare_animation=App.animations.puppet_jump)

    def movement(self, App):
        if self.locationId == 11:
            if App.objects.music_box.charge == 0:
                if pygame.time.get_ticks() - self.timer > 8000:
                    self.jumpscare()
            elif App.objects.music_box.charge != 0:
                self.timer = pygame.time.get_ticks()