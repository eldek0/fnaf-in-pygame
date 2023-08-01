import pygame

class MaskAnimation:
    def __init__(self, position:list, move:tuple=(0.3, 0.08)):
        self.position = list(position)
        self.initial_pos = self.position.copy()
        self.timer = pygame.time.get_ticks()
        self.speed = 0.15
        self.direction = [-1, -1] # Left and up
        self.move:tuple = move

    def update(self):
        self.position[0] += self.move[0]*self.direction[0]
        self.position[1] += self.move[1]*self.direction[1]

        if pygame.time.get_ticks() - self.timer > 2000:

            self.direction[0] *= -1
            self.direction[1] *= -1

            self.timer = pygame.time.get_ticks()

    def reset(self):
        self.__init__(position=self.initial_pos)