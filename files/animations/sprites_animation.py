import pygame

class SpritesAnimation:
    def __init__(self, sprites:tuple, position:tuple, frame_wait=1, isLoop=False, alpha=255):
        self.sprites:tuple = sprites
        self.frame_wait:int = frame_wait
        self.position:tuple = position
        self.sprite_num:int = 0
        self.loop :bool= isLoop
        self.frame:int = 0
        self.alpha:int = alpha
        self.desactivate:bool = False
        self.animate:bool = True

        
    def update(self, surface:pygame.Surface, reversed=False):
        if not self.desactivate:
            self.sprites[self.sprite_num].set_alpha(self.alpha)
            surface.blit(self.sprites[self.sprite_num], self.position)
            
            if self.animate:
                self.frame += 1
                if self.frame == self.frame_wait:
                    # Change the sprite
                    if not reversed:
                        if self.sprite_num < len(self.sprites) - 1:
                            self.sprite_num += 1
                        else:
                            if self.loop:
                                self.sprite_num = 0
                    else:
                        if not self.sprite_num == 0:
                            self.sprite_num -= 1
                        else:
                            if self.loop:
                                self.sprite_num = len(self.sprites) - 1

                    self.frame = 0