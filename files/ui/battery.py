import pygame

class Battery:
    def __init__(self, App):
        # 100 = Maximum
        # 0 = No battery
        self.charge = 100
        self.position = [45, 40]
        self.surface_index = 0

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
                self.charge -= 0.0152 * App.deltaTime
        
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