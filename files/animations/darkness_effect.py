import pygame

class DarknessAnimation:
    def __init__(self, App, position:tuple, frame_wait=1,fading_time=3000,time_until_fade=16000, fade=True, reversed_=False):
        self.frame_wait:int = frame_wait
        self.position:tuple = position
        self.sprite_num:int = 0
        self.frame:int = 0
        self._fade:bool = fade
        self.fading_time:int = fading_time
        self.black_rect_anim:int = [
            0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1,1,1, 0, 0, 1, 0, 1,
            0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1,1 ,0, 1, 0, 1,1 , 0, 1, 0, 1
        ]
        self.black_screen = pygame.Surface((App.dimentions[0], App.dimentions[1])).convert_alpha()
        self.is_animating = False
        self.timer = pygame.time.get_ticks()
        self._isFading = False
        self.time_until_fade = time_until_fade
        self.hold_black_screen_time = 750
        self.reversed = reversed_
        if self.reversed:
            self.fade_alpha = 1
        else:
            self.fade_alpha = 255
        
    def reset(self):
        print("resetting darkness")
        if self.reversed:
            self.fade_alpha = 1
        else:
            self.fade_alpha = 255
        self.is_animating = False
        self._isFading = False
        self.sprite_num = 0

    def fade(self, deltaTime:float, force=False):
        if self._fade:
            # Hold black screen some time
            if pygame.time.get_ticks() - self.timer <= self.hold_black_screen_time:
                if self.reversed:
                    self.fade_alpha = 1
                else:
                    self.fade_alpha = 255
            else:
                min_time = self.hold_black_screen_time
                max_time = self.hold_black_screen_time + self.fading_time
                if self.reversed:
                    steps = max_time // (255 - self.fade_alpha)
                else:
                    steps = max_time // (self.fade_alpha)
                if pygame.time.get_ticks() - self.timer >= min_time + steps:
                    if self.reversed:
                        self.fade_alpha += 1 * deltaTime
                    else:
                        self.fade_alpha -= 1 * deltaTime

                if self.reversed:
                    if self.fade_alpha >= 255:
                        self.reset()
                else:
                    if self.fade_alpha <= 15:
                        self.reset()

        else:
            self.reset()

    def update(self, surface:pygame.Surface, deltaTime:float, reversed=False):
        if not self.is_animating:
            self.timer = pygame.time.get_ticks()
            self.is_animating = True

        if self.black_rect_anim[self.sprite_num] or self._isFading:
            self.black_screen.set_alpha(self.fade_alpha)
            surface.blit(self.black_screen, self.position)

        if not self._isFading:
            if pygame.time.get_ticks() - self.timer <= self.time_until_fade:
                self.frame += 1 * deltaTime
                if self.frame >= self.frame_wait:
                    # Change the sprite
                    if self.sprite_num < len(self.black_rect_anim) - 1:
                        self.sprite_num += 1
                    else:
                        self.sprite_num = 0

                    self.frame = 0
            else:
                self.fade_screen()
        else:
            self.fade(deltaTime)

    def fade_screen(self):
        if not self._isFading:
            self._isFading = True
            self.timer = pygame.time.get_ticks()