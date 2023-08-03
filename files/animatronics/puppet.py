import pygame, math

from files.animatronics.animatronic_base import Animatronic

class Puppet(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int):
        super().__init__(aggresivity=aggresivity, locationId=11, jumpscare_animation=App.animations.puppet_jump, rest_room=None, custom_index=custom_index)

    def movement(self, App):
        if App.objects.music_box.times_out:
            self.secondPositionId = 3
            if self.secondPositionId == 1:
                self.change_location_id(App, 11, secondPositionId=2)
                    
            elif self.secondPositionId == 2:
                if pygame.time.get_ticks() - self.timer > 10000:
                    self.change_location_id(App, 11, secondPositionId=3)

            elif self.secondPositionId == 3:
                if pygame.time.get_ticks() - self.timer > 9000:
                    self.jumpscare(App)

        elif not App.objects.music_box.times_out:
            self.timer = pygame.time.get_ticks()

        App.objects.music_box.descharge_ticks = 17800/(math.log((self.aggresivity + 2)**6))
        App.objects.music_box.run_time(App)
        