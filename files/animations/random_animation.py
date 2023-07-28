import pygame, random

class RandomSpritesAnimation:
    def __init__(self, 
                App, sprites:list, position:tuple,
                speed_frame:int=1, alpha:int=40,
                randoms_intervals=(120, 1500),
                randoms_intervals_time=900
            ):
        self.sprites = sprites
        self.position = position
        self.speed_frame = speed_frame
        self.randoms_intervals = randoms_intervals
        self.randoms_intervals_time = randoms_intervals_time
        self.alpha = alpha
        self.index = 0
        self.prev_index = 0
        self.frame = 0
        self.timer = pygame.time.get_ticks()

        self.update_random_time_for_interval()

    def update_random_time_for_interval(self):
        self.random_time_for_interval = random.randint(self.randoms_intervals[0], self.randoms_intervals[1])

    def update(self, App):
        if pygame.time.get_ticks() - self.timer < self.random_time_for_interval:
            self.sprites[self.index].set_alpha(self.alpha)
            App.surface.blit(self.sprites[self.index], self.position)
            self.frame += 1
            if self.frame >= self.speed_frame:
                self.prev_index = self.index
                while self.index == self.prev_index:
                    self.index = random.randint(0, len(self.sprites)-1)
                self.frame = 0

        else:
            if pygame.time.get_ticks() - self.timer > self.random_time_for_interval + self.randoms_intervals_time:
                self.timer = pygame.time.get_ticks()
                self.update_random_time_for_interval()