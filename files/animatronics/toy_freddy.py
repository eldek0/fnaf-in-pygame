import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyFreddy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity=aggresivity, locationId=9, jumpscare_animation=App.animations.toy_freddy_jump, rest_room=10, custom_index=custom_index, img_show=img_show)

    def movement(self, App):
        toy_bonnie = App.objects.Animatronics.animatronics_in_game["TOY_BONNIE"]
        toy_chica = App.objects.Animatronics.animatronics_in_game["TOY_CHICA"]

        match self.locationId:
            case 9:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    if (toy_bonnie.locationId != 9 and toy_chica.locationId != 9) or App.menu.nightToPlay == 7:
                        # Moves to Game Area
                        self.change_location_id(App, 10)
                    else:
                        self.timer = pygame.time.get_ticks()

            case 10:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 101, secondPositionId=1)

            case 101:
                if self.secondPositionId == 1:
                    if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                        self.change_location_id(App, 101, secondPositionId=2)
                elif self.secondPositionId == 2:
                    self.interrupt_in_office(App)
        
                
