import pygame

import files.utils as f
from files.game.sound_effects import sounds_effects_updater
from files.menu.night_beaten_animation import NightBeatenAnimation
from files.menu.you_lost_animation import YouLostAnimation
from files.game.night import NightAIChanger
from files.game.telephone import Telephone

class Game:
    def __init__(self, App):
        self.gameOver = False

        self.TIME_PLAYING = pygame.time.get_ticks()
        self.ambiance_sound = pygame.time.get_ticks()

        self.audio_set = False

        self.night_beaten = False

        self.you_lost = False

        self.sounds_shutted = True

        self.beaten_animation = NightBeatenAnimation(App)

        self.you_lost_animation = YouLostAnimation(App)

        self.ai_updater = NightAIChanger(App)

        self.telephone = Telephone(App)

    def set_audio(self, App):
        self.sounds_shutted = False
        pygame.mixer.set_num_channels(16)

        pygame.mixer.music.set_volume(1)
        pygame.mixer.Channel(1).set_volume(0.8)
        pygame.mixer.Channel(2).set_volume(0) # Music box
        pygame.mixer.Channel(3).set_volume(1) # Sounds effects
        pygame.mixer.Channel(4).set_volume(1) # Mask breathing
        pygame.mixer.Channel(5).set_volume(1) # Stare at an animatrionic
        pygame.mixer.Channel(6).set_volume(1) # Mangle noise
        pygame.mixer.Channel(7).set_volume(1) # Baloon boy laugh
        pygame.mixer.Channel(8).set_volume(1) # Jumpscare scream

    def stop_sounds(self):
        self.sounds_shutted = True
        pygame.mixer.music.unload()
        pygame.mixer.Channel(1).set_volume(0)
        pygame.mixer.Channel(2).set_volume(0) # Music box
        pygame.mixer.Channel(3).set_volume(0) # Sounds effects
        pygame.mixer.Channel(4).set_volume(0) # Mask breathing
        pygame.mixer.Channel(5).set_volume(0) # Stare at an animatrionic
        pygame.mixer.Channel(6).set_volume(0) # Mangle noise
        pygame.mixer.Channel(7).set_volume(0) # Baloon boy laugh

    def updater(self, App):
        self.game_update(App)
        if App.objects.gameTimer.time == 6:
            if not self.night_beaten:
                App.animations.darkness_reversed.fade_screen()
            self.night_beaten = True

        if self.night_beaten:
            if not self.sounds_shutted:
                pygame.mixer.Channel(1).set_volume(1)
                pygame.mixer.Channel(1).play(App.assets.clock_chimes)
            App.animations.darkness_reversed.update(App)
            self.beaten_animation.update(App)

        if App.objects.Animatronics.being_jumpscared and not self.sounds_shutted:
            self.stop_sounds()

        if not self.night_beaten and self.sounds_shutted and self.you_lost:
            self.you_lost_animation.update(App)

        if not self.night_beaten and not self.you_lost:
            self.ai_updater.update(App, App.menu.inNight)
            self.telephone.update(App, App.menu.inNight)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(App.assets.background_music)
            pygame.mixer.music.play(-1)

    def game_update(self, App):
        if not self.night_beaten and not self.you_lost:
            if not self.audio_set:
                self.set_audio(App)
                self.audio_set = True

            if App.objects.Animatronics.gameOver and not pygame.mixer.Channel(8).get_busy():
                # YOU LOST
                self.you_lost = True
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

                App.objects.gameTimer.update(App)

                # Update animatronics
                App.objects.Animatronics.update(App)
                App.gameOver = App.objects.Animatronics.gameOver

                # Sounds
                sounds_effects_updater(App)
        else:
            App.objects.office.update(App, canInteract=False, draw=True, animate=False)

            App.objects.battery.update(App, update_charge=False)

            App.objects.gameTimer.update(App, update_time=False)

            App.objects.open_monitor_button.update(App, canInteract=False)
            App.objects.open_monitor_button.quitting_camera = True

            App.objects.mask_button.update(App, canInteract=False)
            App.objects.mask_button.quitting_mask = True

