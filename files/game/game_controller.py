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

        self.num_of_channels = 32

    def set_audio(self, volume:int):
        self.sounds_shutted = False
        pygame.mixer.set_num_channels(self.num_of_channels)

        pygame.mixer.music.set_volume(1)
        pygame.mixer.Channel(1).set_volume(volume)
        pygame.mixer.Channel(2).set_volume(0) # Music box
        pygame.mixer.Channel(3).set_volume(volume) # Sounds effects
        pygame.mixer.Channel(4).set_volume(volume) # Mask breathing
        pygame.mixer.Channel(5).set_volume(volume) # Stare at an animatrionic
        pygame.mixer.Channel(6).set_volume(volume) # Mangle noise
        pygame.mixer.Channel(7).set_volume(volume) # Baloon boy laugh
        pygame.mixer.Channel(8).set_volume(volume) # Jumpscare scream
        pygame.mixer.Channel(9).set_volume(volume) # Flashlight
        pygame.mixer.Channel(10).set_volume(volume) # Camera's static
        pygame.mixer.Channel(11).set_volume(volume) # Animatronics noises

    def stop_sounds(self):
        self.sounds_shutted = True
        pygame.mixer.music.unload()
        for i in range(self.num_of_channels):
            if i != 8:
                pygame.mixer.Channel(i).stop()

    def updater(self, App):
        if App.objects.gameTimer.time == 6:
            self.night_beaten = True

        if App.objects.Animatronics.being_jumpscared and not self.sounds_shutted:
            self.stop_sounds()

        if not (self.night_beaten and self.you_lost):
            self.ai_updater.update(App, App.menu.nightToPlay)
            if App.menu.nightToPlay != 7 and App.objects.Animatronics.being_jumpscared:
                self.telephone.update(App, App.menu.nightToPlay)

        self.game_update(App)

        if (not App.objects.Animatronics.being_jumpscared and App.menu.nightToPlay != 7) and not self.night_beaten:
            self.telephone.update(App, App.menu.nightToPlay)

        if self.night_beaten:
            if not self.sounds_shutted:
                pygame.mixer.stop()
                pygame.mixer.music.unload()
                pygame.mixer.Channel(1).set_volume(1)
                pygame.mixer.Channel(1).play(App.assets.clock_chimes)
                self.sounds_shutted = True
            self.beaten_animation.update(App)

        if not self.night_beaten and self.sounds_shutted and self.you_lost:
            self.you_lost_animation.update(App)

        if not pygame.mixer.music.get_busy() and not self.night_beaten:
            pygame.mixer.music.load(App.assets.background_music)
            pygame.mixer.music.play(-1)

    def game_update(self, App):
        if not self.night_beaten and not self.you_lost:
            if not self.audio_set:
                self.set_audio(1)
                self.audio_set = True

            if App.objects.Animatronics.gameOver:
                # YOU LOST
                self.you_lost = True
                pygame.mixer.Channel(8).stop()
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
                        App.objects.office.hallway_on = False
                        App.objects.office.right_vent_on = False
                        App.objects.office.left_vent_on = False
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

                # Music box warning
                App.objects.music_box.warning_sign(App)

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

