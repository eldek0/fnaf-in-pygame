import pygame, random

from files.animatronics.animatronic_base import Animatronic

class GoldenFreddy(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity, 0, App.animations.golden_freddy_jump, 0, custom_index, img_show=img_show)
        self.time_to_react = 1000
        self.in_office = False
        self.attempted_once = False
        self.leave = False

    def movement(self, App):
        #print("entering: ", App.objects.open_monitor_button.entering_camera)
        #print("quitting: ", App.objects.open_monitor_button.quitting_camera)
        # Conditions
        if App.objects.open_monitor_button.quitting_camera and not self.in_office and not self.attempted_once and not App.objects.office.animatronic_in_office:
            show_ran_num = random.randint(1, 1000)

            if show_ran_num < 10*((self.aggresivity + 1)*1.2) and not self.leave:
                self.change_location_id(App, -1, forced=True)
                self.in_office = True
                self.leave = True
            else:
                self.leave = False
            self.attempted_once = True

        if (App.objects.open_monitor_button.inCamera and not App.objects.open_monitor_button.quitting_camera) or (App.objects.mask_button.inMask and not App.objects.mask_button.quitting_mask):
            self.change_location_id(App, 0, forced=True)
            self.in_office = False
            self.attempted_once = False

        # Time to react
        if pygame.time.get_ticks() - self.timer > self.time_to_react and self.locationId == -1 and self.in_office:
            self.jumpscare(App)

        if self.locationId == 0:
            self.timer = pygame.time.get_ticks()
