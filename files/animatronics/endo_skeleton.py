import pygame, random

from files.animatronics.animatronic_base import Animatronic

class EndoSkeleton(Animatronic):
    def __init__(self, App, aggresivity:int, custom_index:int, img_show=None):
        super().__init__(aggresivity, -2, None, -2, custom_index, img_show)
        self.chance_ran = 0
        self.occupied_camera_time = 1500

    def movement(self, App): 
        pass

    def try_appearance(self, App):
        self.chance_ran = random.randint(1, 40_000)
        if self.chance_ran == 30_000:
            if self.verify_free_room(App, 5):
                self.locationId = 5
        elif self.chance_ran == 10_000:
            self.locationId = 11

    def rest(self, App): self.change_location_id(App, -2)