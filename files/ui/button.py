import pygame

class Button:
    def __init__(self, position:list, dimentions:tuple, sprite:pygame.sprite.Sprite, draw_box:bool=False):
        self.dimension:tuple = dimentions
        self.position:list = position
        self.sprite:pygame.sprite.Sprite = sprite
        self.mouse_hovered = False
        self.draw_box = draw_box

    def update(self, surface:pygame.Surface, mouse_hitbox:pygame.rect):
        rect = pygame.Rect(self.position[0], self.position[1], self.dimension[0], self.dimension[1])

        # Draw sprite
        if self.sprite:
            surface.blit(self.sprite, self.position)

        if self.draw_box:
            if self.mouse_hovered:
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)

            pygame.draw.rect(surface, color, rect)

        self.mouse_update(mouse_hitbox, rect)

    def mouse_update(self, mouse_hitbox:pygame.rect, button_rect:pygame.rect):
        if mouse_hitbox.colliderect(button_rect):
            self.mouse_hovered = True
        else:
            self.mouse_hovered = False