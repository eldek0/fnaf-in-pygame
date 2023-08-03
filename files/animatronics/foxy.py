import pygame

from files.animatronics.animatronic_base import Animatronic

class Foxy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int):
        super().__init__(aggresivity, 8, App.animations.foxy_jump, 8, custom_index)
        self._light = 100
        self.movement_time = 140_000
        

    def movement(self, App): 
        match self.locationId:
            case 8:
                if pygame.time.get_ticks() - self.timer > self.movement_time / ((self.aggresivity + 1)*2):
                    self.change_location_id(App, 101)

            case 101:
                if not App.objects.office.hallway_on:
                    if not App.objects.office.occupied_office[0]:
                        self._light -= 0.15 * ((self.aggresivity + 1)/5)
                        if self._light < 0:
                            self._light = 0
                else:
                    self._light += 0.20 * ((self.aggresivity + 1)/1.4)
                    if self._light > 100:
                        self._light = 100

                if self._light == 0:
                    self.jumpscare(App)

                # "Get scared"
                if pygame.time.get_ticks() - self.timer > 10000*(self.aggresivity/2.34):
                    self.return_to_rest_room(App)
                    self._light = 100