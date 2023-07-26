import pygame
from files.ui.button import Button

class Telephone:
    def __init__(self, App):
        self.call_started = False
        self.muted = False

        dims = App.assets.telephone_mute.get_rect()
        self.mute_button = Button(position=(160, 43), dimentions=(dims.w, dims.h), sprite=App.assets.telephone_mute)
        self.timer = pygame.time.get_ticks()

    def update(self, App, inNight:int):
        if not self.call_started and pygame.time.get_ticks() - self.timer > 3000:
            pygame.mixer.music.load(App.assets.telephone_audios[inNight - 1])
            pygame.mixer.music.play(1)
            self.call_started = True

        if self.call_started and not self.muted:
            if pygame.time.get_ticks() - self.timer < 15000:
                self.mute_button.update(App.surface, App.mouse_hitbox)

            mouse = pygame.mouse.get_pressed()

            if self.mute_button.mouse_hovered:
                if mouse[0]:
                    self.muted = True
                    pygame.mixer.music.unload()