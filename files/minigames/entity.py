import pygame
from files.animations.sprites_animation import SpritesAnimation

class Entity:
    def __init__(self, 
                 texture:pygame.Surface, initial_position:tuple,
                 walkingRightAnimation:SpritesAnimation = None, 
                 walkingDownAnimation:SpritesAnimation = None, 
                 walkingUpAnimation:SpritesAnimation = None,
                 hitboxDims:pygame.Rect = None
                 ):
        self.texture:pygame.Surface = texture
        self.position:list = list(initial_position)
        self.lastFramePos:list = list(initial_position)
        self.walkingRightAnimation:SpritesAnimation = walkingRightAnimation
        self.walkingDownAnimation:SpritesAnimation = walkingDownAnimation
        self.walkingUpAnimation:SpritesAnimation = walkingUpAnimation
        self.__hitboxDims:pygame.Rect = hitboxDims

        self.speed:int = 15
        self.timer:int = pygame.time.get_ticks()
        self.moving:bool = False
        self.notMovingTimer = pygame.time.get_ticks()
        self.animate:bool = False
        self.moving_direction:chr = 'd'

    def update(self, App):
        self.detect_if_its_not_moving()
        self.drawCharacter(App)
        

    def movement(self, movement:chr):
        self.lastFramePos = list(self.position).copy()
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

            if movement in ['r', 'l', 'u', 'd']:
                self.moving_direction = movement

            self.timer = pygame.time.get_ticks()

    def detect_if_its_not_moving(self):
        if self.position != self.lastFramePos and (self.walkingDownAnimation and self.walkingRightAnimation and self.walkingUpAnimation):
            self.notMovingTimer = pygame.time.get_ticks()
            self.animate = True
            self.moving = True
        else:
            self.moving = False

        if pygame.time.get_ticks() - self.notMovingTimer > 150:
            self.animate = False

    def drawCharacter(self, App):
        surf = App.minigamesSurface
  
        if self.animate:
            if (self.moving_direction == 'r'): # walking right
                self.walkingRightAnimation.position = self.position
                self.walkingRightAnimation.update(surf, App.deltaTime)
            elif (self.moving_direction == 'l'): # walking left
                self.walkingRightAnimation.position = self.position
                self.walkingRightAnimation.update(surf, App.deltaTime, flipx=True)
            elif (self.moving_direction == 'u'): # walking up
                self.walkingUpAnimation.position = self.position
                self.walkingUpAnimation.update(surf, App.deltaTime)
            elif (self.moving_direction == 'd'): # walking down
                self.walkingDownAnimation.position = self.position
                self.walkingDownAnimation.update(surf, App.deltaTime)
            return
        
        surf.blit(self.texture, self.position)
        

    def rect(self)->pygame.Rect:
        if not self.__hitboxDims:
            return pygame.Rect(self.position[0], self.position[1], self.texture.get_width(), self.texture.get_height())
        return pygame.Rect(self.position[0] + self.__hitboxDims.x, self.position[1] + self.__hitboxDims.y, self.__hitboxDims.w, self.__hitboxDims.h)
    
    def show_rect(self, App):
        pygame.draw.rect(App.uiSurface, (200, 200, 200), self.rect())