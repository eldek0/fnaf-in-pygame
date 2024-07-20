import pygame
from files.ui.game_timer import GameTimer

class Battery:
    def __init__(self, App, real_time_mode=False):
        # 100 = Maximum
        # 0 = No battery
        self.charge = 100
        self.position = [45, 40]
        self.surface_index = 0
        self.real_time_mode = real_time_mode
        self.CHANGE_CONST = 0.0152

    def update(self, App, update_charge=True):
        App.uiSurface.blit(App.assets.flashlight_label, [self.position[0] + 5, self.position[1] - 15])
        App.uiSurface.blit(App.assets.battery_stages[self.surface_index], self.position)

        if update_charge:
            self.detect_usage(App)
            self.charge_update()
        
    def detect_usage(self, App):
        usage_detections = [
            App.objects.office.hallway_on,
            App.objects.office.right_vent_on,
            App.objects.office.left_vent_on,
            App.objects.camera.camera_flashlighting
        ]
        for state in usage_detections:
            if state:
                if self.real_time_mode:
                    self.charge -= (self.CHANGE_CONST * App.objects.gameTimer.GAMEHOUR) / App.objects.gameTimer.REALLIFEHOUR
                else:
                    self.charge -= self.CHANGE_CONST * App.deltaTime
        
        if self.charge < 0:
            self.charge = 0

    def charge_update(self):
        if self.charge > 75:
            self.surface_index = 0
        elif self.charge > 50 and self.charge <= 75:
            self.surface_index = 1
        elif self.charge > 25 and self.charge <= 50:
            self.surface_index = 2
        elif self.charge > 0 and self.charge <= 25:
            self.surface_index = 3
        elif self.charge == 0:
            self.surface_index = 4