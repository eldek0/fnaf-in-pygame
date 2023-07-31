import pygame

class MaskAnimation:
    def __init__(self, position:list):
        self.position = list(position)
        self.initial_pos = self.position.copy()
        self.timer = pygame.time.get_ticks()
        self.speed = 0.15
        self.direction = [-1, -1] # Left and up

    def update(self):
        self.position[0] += 0.3*self.direction[0]
        self.position[1] += 0.08*self.direction[1]

        if pygame.time.get_ticks() - self.timer > 2000:

            self.direction[0] *= -1
            self.direction[1] *= -1

            self.timer = pygame.time.get_ticks()

    def reset(self):
        self.__init__(position=self.initial_pos)