import pygame

class Entity:
    def __init__(self, texture:pygame.Surface, initial_position:tuple):
        self.texture:pygame.Surface = texture
        self.position:list = list(initial_position)
        self.speed = 15
        self.timer = pygame.time.get_ticks()

    def update(self, App):
        App.minigamesSurface.blit(self.texture, self.position)

    def movement(self, movement:chr):
        if (pygame.time.get_ticks() - self.timer > 100):
            match movement:
                case 'r':
                    self.position[0] += self.speed
                case 'l':
                    self.position[0] -= self.speed
                case 'u':
                    self.position[1] -= self.speed
                case 'd':
                    self.position[1] += self.speed

            self.timer = pygame.time.get_ticks()

    def rect(self)->pygame.Rect:
        return pygame.Rect(self.position[0], self.position[1], self.texture.get_width(), self.texture.get_height())