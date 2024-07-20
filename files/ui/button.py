import pygame
from files.utils import draw_hitbox, transform_rect
from files.ui.Text import Lock_to

class Button:
    def __init__(self, position:list, dimentions:tuple, sprite:pygame.sprite.Sprite, draw_box:bool=False, lock_to:str=None):
        self.dimension:tuple = dimentions
        self._position:list = position
        self.sprite:pygame.sprite.Sprite = sprite
        self.mouse_hovered = False
        self.draw_box = draw_box
        self.lock_to = lock_to
        self.Lock_formula = (0,0)

    def update(self, surface:pygame.Surface, mouse_hitbox:pygame.rect):

        if not self.lock_to == None:
            self.Lock_formula = Lock_to(self.lock_to, tuple(self._position), self.dimension[0], self.dimension[1], surface.get_rect() )
        
        rect = pygame.Rect(self.position[0], self.position[1], self.dimension[0], self.dimension[1])
        transform_rect(surface, rect)

        # Draw sprite
        if self.sprite:
            surface.blit(self.sprite, self.position)

        if self.draw_box:
            if self.mouse_hovered:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)

            draw_hitbox(surface, color, rect)

        self.mouse_update(mouse_hitbox, rect)

    def mouse_update(self, mouse_hitbox:pygame.rect, button_rect:pygame.rect):
        if mouse_hitbox.colliderect(button_rect):
            self.mouse_hovered = True
        else:
            self.mouse_hovered = False

    @property
    def position(self): return (self._position[0] + self.Lock_formula[0], self._position[1] + self.Lock_formula[1])