import pygame
from files.animations.sprites_animation import SpritesAnimation

class Entity:
    def __init__(self, 
                 texture:pygame.Surface, initial_position:tuple,
                 walkingRightAnimation:SpritesAnimation = None, 
                 walkingDownAnimation:SpritesAnimation = None, 
                 walkingUpAnimation:SpritesAnimation = None,
                 hitboxDims:pygame.Rect = None,
                 framesToMove:int = 100,
                 speed:int = 15
                 ):
        self.texture:pygame.Surface = texture
        self.position:list = list(initial_position)
        self.lastFramePos:list = list(initial_position)
        self.walkingRightAnimation:SpritesAnimation = walkingRightAnimation
        self.walkingDownAnimation:SpritesAnimation = walkingDownAnimation
        self.walkingUpAnimation:SpritesAnimation = walkingUpAnimation
        self.__hitboxDims:pygame.Rect = hitboxDims
        self.framesToMove:int = framesToMove
        self.speed:int = speed
        
        self.timer:int = pygame.time.get_ticks()
        self.moving:bool = False
        self.notMovingTimer = pygame.time.get_ticks()
        self.animate:bool = False
        self.moving_direction:chr = 'd'

    def update(self):
        self.detect_if_its_not_moving()
        self.updateCharacter()
        
    def draw(self, App):
        surf = App.minigamesSurface
        if (self.is_in_screen_bounds(surf)):
            self.drawCharacter(App)


    def movement(self, movement:chr):
        self.lastFramePos = list(self.position).copy()
        if (pygame.time.get_ticks() - self.timer > self.framesToMove):
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

    def updateCharacter(self):
        if self.animate:
            match self.moving_direction:
                case 'r':
                    self.walkingRightAnimation.position = self.position
                case 'l':
                    self.walkingRightAnimation.position = self.position
                case 'u':
                    self.walkingUpAnimation.position = self.position
                case 'd':
                    self.walkingDownAnimation.position = self.position
            return


    def drawCharacter(self, App):
        surf = App.minigamesSurface
  
        if self.animate:
            match self.moving_direction:
                case 'r':
                    self.walkingRightAnimation.update(surf, App.deltaTime)
                case 'l':
                    self.walkingRightAnimation.update(surf, App.deltaTime, flipx=True)
                case 'u':
                    self.walkingUpAnimation.update(surf, App.deltaTime)
                case 'd':
                    self.walkingDownAnimation.update(surf, App.deltaTime)
            return

        surf.blit(self.texture, self.position)
        
        
        
    def is_in_screen_bounds(self, surface:pygame.Surface):
        entity_w, entity_h = self.texture.get_width(), self.texture.get_height()
        surf_w, surf_h = surface.get_width(), surface.get_height()
        return self.position[0] > -entity_w and self.position[1] > -entity_h and self.position[0] < surf_w + entity_w and self.position[1] < surf_h + entity_h

    def rect(self)->pygame.Rect:
        if not self.__hitboxDims:
            return pygame.Rect(self.position[0], self.position[1], self.texture.get_width(), self.texture.get_height())
        return pygame.Rect(self.position[0] + self.__hitboxDims.x, self.position[1] + self.__hitboxDims.y, self.__hitboxDims.w, self.__hitboxDims.h)
    
    def show_rect(self, App):
        pygame.draw.rect(App.uiSurface, (200, 200, 200), self.rect())