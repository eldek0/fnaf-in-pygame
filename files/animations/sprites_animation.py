import pygame, random

class SpritesAnimation:
    def __init__(self, sprites:tuple, position:list, frame_wait=1, isLoop=False, alpha=255):
        self.sprites:tuple = sprites
        self.frame_wait:int = frame_wait
        self.position:list = position
        self.sprite_num:int = 0
        self.loop :bool= isLoop
        self.frame:int = 0
        self.alpha:int = alpha
        self.desactivate:bool = False
        self.animate:bool = True
        self.ran_value:int = random.randint(1, 100)

        
    def update(self, surface:pygame.Surface, deltaTime:float, reversed=False, flipx=False, flipy=False):
        if not self.desactivate:
            spriteToDraw = self.sprites[self.sprite_num]
            spriteToDraw.set_alpha(self.alpha)

            spriteToDraw = pygame.transform.flip(spriteToDraw, flipx, flipy)

            surface.blit(spriteToDraw, self.position)
            
            if self.animate:
                self.frame += 1 * deltaTime
                if self.frame >= self.frame_wait:
                    # Change the sprite
                    if not reversed:
                        if self.sprite_num < len(self.sprites) - 1:
                            self.sprite_num += round(1 * deltaTime)
                            if (self.sprite_num > len(self.sprites) - 1):
                                self.sprite_num = len(self.sprites) - 1
                        else:
                            if self.loop:
                                self.sprite_num = 0
                    else:
                        if not self.sprite_num == 0:
                            self.sprite_num -= round(1 * deltaTime)
                            if self.sprite_num < 0:
                                self.sprite_num = 0
                        else:
                            if self.loop:
                                self.sprite_num = len(self.sprites) - 1

                    self.frame = 0
    
    def get_width(self):
        return self.sprites[0].get_width()
    
    def get_height(self):
        return self.sprites[0].get_height()
    
    def reset(self):self.__init__(self.sprites, self.position, self.frame_wait, self.loop, self.alpha)