import pygame

class FadeEffect:
    def __init__(self, App,position:tuple, effect_out=True, alpha_speed=2):
        self.black_screen = pygame.Surface((App.dimentions[0], App.dimentions[1]))
        self.alpha = 0
        self.effect_out = effect_out
        self._stop = True
        self.alpha_speed = alpha_speed
        self.position = position
        if self.effect_out:
            self.fade_alpha = 255
        else:
            self.fade_alpha = 0

    def continue_effect(self, change_effect=True):
        self._stop = False
        if change_effect:
            if self.effect_out:
                self.effect_out = False
            else:
                self.effect_out = True

    def effect_stopped(self): return self._stop

    def update(self, App):
        self.black_screen.set_alpha(self.fade_alpha)
        App.surface.blit(self.black_screen, self.position)
        if self.effect_out:
            self.fade_alpha -= self.alpha_speed
            if self.fade_alpha < 0:
                self.fade_alpha = 0
                self._stop = True
        else:
            self.fade_alpha += self.alpha_speed
            if self.fade_alpha > 255:
                self.fade_alpha = 255
                self._stop = True