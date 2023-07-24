import pygame
from files.ui.button import Button

class MusicBoxButton:
    def __init__(self, App, position:list):
        self.charge = 21
        self.position = position
        button_size = [App.assets.music_box_button_off.get_width(), App.assets.music_box_button_off.get_height()]
        self.button = Button(position, button_size, App.assets.music_box_button_off)
        self.timer = pygame.time.get_ticks()
        self.timer_sound = pygame.time.get_ticks()
        self.recharging_time = False
        self.times_out = False

    def update(self, App):

        self.button.update(App.surface, App.mouse_hitbox)
        App.surface.blit(App.assets.music_box_label, [self.position[0] + 10, self.position[1] + 10])

        mouse_click = pygame.mouse.get_pressed()
        if self.button.mouse_hovered:
            if mouse_click[0]:
                self.button.sprite = App.assets.music_box_button_on
                self.recharge_time()
                if not pygame.mixer.Channel(3).get_busy() and pygame.time.get_ticks() - self.timer_sound > 450:
                    pygame.mixer.Channel(3).play(App.assets.charge)
                    self.timer_sound = pygame.time.get_ticks()

        if not self.button.mouse_hovered or not mouse_click[0]:
            self.button.sprite = App.assets.music_box_button_off
            if self.recharging_time:
                self.timer = pygame.time.get_ticks()
                self.recharging_time = False

        if not self.times_out:
            # Draw timer
            App.surface.blit(App.assets.music_box_timer_sprites[self.charge-1], [self.position[0] - 100, self.position[1]])

    def run_time(self, App):
        if not self.times_out:
            if pygame.time.get_ticks() - self.timer > 1000 and not self.charge == 0 and not self.recharging_time:
                self.charge -= 1
                self.timer = pygame.time.get_ticks()

            if self.charge == 0:
                if not self.times_out:
                    pygame.mixer.music.unload()
                self.times_out = True

    def recharge_time(self):
        if not self.times_out:
            if not self.recharging_time:
                self.timer = pygame.time.get_ticks()
                self.recharging_time = True

            if self.recharging_time:
                if pygame.time.get_ticks() - self.timer > 300:
                    if not self.charge >= 21:
                        self.charge += 1
                    self.timer = pygame.time.get_ticks()