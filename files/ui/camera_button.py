import pygame
from files.ui.button import Button

class CameraButton:
    def __init__(self, App, draw_box=False):
        spr_monitor_dims = [App.assets.monitor_button.get_width(), App.assets.monitor_button.get_height()]
        self.monitor_button = Button((510, App.dimentions[1] - spr_monitor_dims[1]- 20), [spr_monitor_dims[0], spr_monitor_dims[1] + 100], sprite=App.assets.monitor_button, draw_box=draw_box)
        self.inCamera = False
        self.camera_being_pressed = False
        self.quitting_camera = False

    def update(self, App):

        self.monitor_button.update(App.surface, App.mouse_hitbox)
        if App.objects.battery.charge == 0:
            self.inCamera = False
            if self.monitor_button.mouse_hovered:
                if not self.camera_being_pressed:
                    App.assets.error_sound.play()
                    self.camera_being_pressed = True
            else:
                self.camera_being_pressed = False
        
        self.animation(App)
        

    def animation(self, App):
        # Monitor animation
        if not self.inCamera:
            if self.monitor_button.mouse_hovered:
                if not self.camera_being_pressed:
                    App.animations.monitor.update(App.surface)

                    # Get in camera
                    if App.animations.monitor.sprite_num == len(App.animations.monitor.sprites) - 1:
                        if not App.objects.battery.charge == 0:
                            self.inCamera = True
                            App.objects.camera.static_animation = True
                            App.animations.monitor.desactivate = True

                        self.camera_being_pressed = True
            else:
                self.camera_being_pressed = False
                if App.animations.monitor.sprite_num != 0:
                    App.animations.monitor.update(App.surface, reversed=True)
        else:
            if self.monitor_button.mouse_hovered:
                if not self.camera_being_pressed:
                    self.quitting_camera = True

            else:
                self.camera_being_pressed = False

            if self.quitting_camera:
                App.animations.monitor.desactivate = False
                if App.objects.music_box.charge != 0:
                    pygame.mixer.Channel(2).set_volume(0)
                App.animations.monitor.update(App.surface, reversed=True)
                # Get off camera
                if App.animations.monitor.sprite_num == 0:
                    self.inCamera = False
                    self.camera_being_pressed = True
                    self.quitting_camera = False
                    App.assets.camera_sound_2.play()
                    