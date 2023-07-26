import pygame

from files.animatronics.animatronic_base import Animatronic

class Foxy(Animatronic):
    def __init__(self, App, aggresivity:int):
        super().__init__(aggresivity, 8, App.animations.foxy_jump, 8)
        self._light = 100
        

    def movement(self, App): 
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 101)

            case 101:
                if not App.objects.office.hallway_on:
                    self._light -= 0.05 * (self.aggresivity/12)
                    if self._light < 0:
                        self._light = 0
                else:
                    self._light += 0.1 * (self.aggresivity/6)
                    if self._light > 100:
                        self._light = 100

                if self._light == 0:
                    self.jumpscare(App)

                # "Get scared"
                if pygame.time.get_ticks() - self.timer > 20000:
                    self.change_location_id(App, 8, forced=True)
                    self._light = 100
                
                print(self._light)