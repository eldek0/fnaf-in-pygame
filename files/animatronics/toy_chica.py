import pygame

from files.animatronics.animatronic_base import Animatronic

class ToyChica(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity, 9, App.animations.toy_chica_jump, 4, custom_index, img_show=img_show)

    def movement(self, App):
        toy_bonnie = App.objects.Animatronics.animatronics_in_game["TOY_BONNIE"]

        match self.locationId:
            case 9:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    if toy_bonnie.locationId != 9 or App.menu.nightToPlay == 7:
                        self.change_location_id(App, 7)
                    else:
                        self.timer = pygame.time.get_ticks()

            case 7:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 4)

            case 4:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 101)

            case 101:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 1)

            case 1:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 5)

            case 5:
                if pygame.time.get_ticks() - self.timer > self.movement_time / self.aggresivity:
                    self.change_location_id(App, 103)

            case 103:
                if pygame.time.get_ticks() - self.timer > self.vent_time_to_scare and App.objects.open_monitor_button.inCamera:
                    self.jumpscare(App, force=True)
                if App.objects.mask_button.inMask:
                    self.time_with_mask += 1 * App.deltaTime
                if self.time_with_mask >= self.time_with_mask_goal:
                    self.return_to_rest_room(App)