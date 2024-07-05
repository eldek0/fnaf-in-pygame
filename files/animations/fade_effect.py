import pygame

class FadeEffect:
    def __init__(self, App,position:tuple, effect_out=True, alpha_speed=1):
        self.black_screen = pygame.Surface((App.dimentions[0], App.dimentions[1])).convert_alpha()
        self.alpha = 0
        self.effect_out = effect_out
        self._stop = True
        self.alpha_speed = alpha_speed
        self.position = position
        if self.effect_out:
            self.fade_alpha = 255
        else:
            self.fade_alpha = 0

    def continue_effect(self, out_effect:bool= None):
        if out_effect == None:
            out_effect = not self.effect_out

        if self._stop:
            if out_effect:
                self.effect_out = True
                self.fade_alpha = 255
            else:
                self.effect_out = False
                self.fade_alpha = 0
            self._stop = False

    def effect_stopped(self): return self._stop

    def stop_effect(self): self._stop = True

    def update(self, surface:pygame.Surface, deltaTime:float):
        self.black_screen.set_alpha(self.fade_alpha)

        if type(surface) is list:
            for surf in surface:
                surf.blit(self.black_screen, self.position)
        else:
            surface.blit(self.black_screen, self.position)

        if self.effect_out:
            self.fade_alpha -= self.alpha_speed * deltaTime
            if self.fade_alpha < 0:
                self.fade_alpha = 0
                self._stop = True
        else:
            self.fade_alpha += self.alpha_speed * deltaTime
            if self.fade_alpha > 255:
                self.fade_alpha = 255
                self._stop = True