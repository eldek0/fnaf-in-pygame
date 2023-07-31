import pygame
from files.ui.button import Button

class CameraButton:
    def __init__(self, App, draw_box=False):
        spr_monitor_dims = [App.assets.monitor_button.get_width(), App.assets.monitor_button.get_height()]
        self.monitor_button = Button((510, App.dimentions[1] - spr_monitor_dims[1]- 20), [spr_monitor_dims[0], spr_monitor_dims[1] + 500], sprite=App.assets.monitor_button, draw_box=draw_box)
        self.inCamera = False
        self.camera_being_pressed = False
        self.quitting_camera = False
        self.entering_camera = False

    def update(self, App, canInteract=True):

        self.monitor_button.update(App.surface, App.mouse_hitbox)
        if canInteract:
            if App.objects.battery.charge == 0:
                self.quitting_camera = True
                if self.monitor_button.mouse_hovered:
                    if not self.camera_being_pressed:
                        App.assets.error_sound.play()
                        self.camera_being_pressed = True
                else:
                    self.camera_being_pressed = False
        
        self.animation(App, canInteract=canInteract)
        

    def animation(self, App, canInteract=True):
        # Monitor animation
        if not self.inCamera:
            if (self.monitor_button.mouse_hovered and canInteract) or self.entering_camera:
                if not self.camera_being_pressed:
                    self.entering_camera = True
                    App.animations.monitor.update(App.surface)

                    # Get in camera
                    if App.animations.monitor.sprite_num == len(App.animations.monitor.sprites) - 1:
                        if not App.objects.battery.charge == 0:
                            self.inCamera = True
                            App.objects.camera.static_animation = True
                            self.entering_camera = False
                            App.assets.camera_sound_1.play()
                        App.animations.monitor.desactivate = True

                        self.camera_being_pressed = True
            else:
                self.camera_being_pressed = False
                if App.animations.monitor.sprite_num != 0:
                    App.animations.monitor.update(App.surface, reversed=True)
        else:
            if self.monitor_button.mouse_hovered or self.quitting_camera:
                if not self.camera_being_pressed:
                    self.quitting_camera = True

            else:
                self.camera_being_pressed = False

            if self.quitting_camera:
                App.animations.monitor.desactivate = False
                
                if not App.objects.music_box.times_out:
                    pygame.mixer.Channel(2).set_volume(0)

                App.animations.monitor.update(App.surface, reversed=True)
                # Get off camera
                if App.animations.monitor.sprite_num == 0:
                    self.inCamera = False
                    self.camera_being_pressed = True
                    self.quitting_camera = False
                    App.assets.camera_sound_2.play()
                    