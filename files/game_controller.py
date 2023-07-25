import pygame

import files.utils as f
from files.sound_effects import sounds_effects_updater

class Game:
    def __init__(self, App):
        self.gameOver = False

        self.TIME_PLAYING = pygame.time.get_ticks()
        self.ambiance_sound = pygame.time.get_ticks()

        self.audio_set = False

    def set_audio(self, App):
        pygame.mixer.set_num_channels(16)
        pygame.mixer.music.load(App.assets.background_music)

        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        pygame.mixer.Channel(1).set_volume(0.8)
        pygame.mixer.Channel(2).set_volume(0) # Music box
        pygame.mixer.Channel(3).set_volume(1) # Sounds effects
        pygame.mixer.Channel(4).set_volume(1) # Mask breathing
        pygame.mixer.Channel(5).set_volume(1) # Stare at an animatrionic
        pygame.mixer.Channel(6).set_volume(1) # Mangle noise
        pygame.mixer.Channel(7).set_volume(1) # Baloon boy laugh
        pygame.mixer.Channel(8).set_volume(1) # Jumpscare scream

    def updater(self, App):
        if not self.audio_set:
            self.set_audio(App)
            self.audio_set = True

        if App.objects.Animatronics.gameOver and not pygame.mixer.Channel(8).get_busy():
            App.animations.static_anim_1.alpha = 255
            App.animations.static_anim_1.update(App.surface)
        else:
            # Background
            App.objects.camera.timers_update(App)

            if not App.objects.Animatronics.being_jumpscared:
                if App.objects.open_monitor_button.inCamera == False:
                    App.objects.office.update(App)
                elif App.objects.open_monitor_button.inCamera and App.objects.open_monitor_button.quitting_camera:
                    App.objects.office.update(App, canInteract=False, draw=True)
                elif App.objects.open_monitor_button.inCamera:
                    App.objects.office.update(App, canInteract=False, draw=False)
            else:
                App.objects.office.update(App, canInteract=False, draw=True)


            if App.objects.open_monitor_button.inCamera and not App.objects.open_monitor_button.quitting_camera:
                # Update camera
                App.objects.camera.update(App)
                App.objects.open_monitor_button.update(App)
            elif App.objects.mask_button.inMask:
                # Update mask button
                App.objects.mask_button.update(App)
            else:
                # Update mask button
                App.objects.mask_button.update(App)
                # Update camera button
                App.objects.open_monitor_button.update(App)

            App.objects.battery.update(App)

            # Update animatronics
            App.objects.Animatronics.update(App)
            App.gameOver = App.objects.Animatronics.gameOver

            # Sounds
            sounds_effects_updater(App)

