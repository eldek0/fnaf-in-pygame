import pygame
from abc import ABC
from files.minigames.entity import Entity

class MinigameDummy(ABC):
    def __init__(self, App):
        self.ended:bool = False
        self.scene:int = 0

    def update(self, App):
        pass

    def key_movement(self, App):
        pass

    def draw_boundaries(self, App, boundaries:list, mainCharacter:Entity):
        """ Will draw all the elements that the player can hit """
        surf = App.minigamesSurface
        for element in boundaries:
            element_rect = None
            rect_changes_scene = False
            if isinstance(element[0], pygame.Surface):
                surf.blit(element[0], (element[1].x, element[1].y))
                element_rect = element[1]
            elif isinstance(element[0], pygame.Rect):
                element_rect = element[0]
                if (isinstance(element[1], int)): # Changes scene
                    rect_changes_scene = True
                elif (isinstance(element[1], tuple)):
                    pygame.draw.rect(surf, element[1], element[0])

            if rect_changes_scene:
                pygame.draw.rect(App.uiSurface, (200, 200, 100), element_rect)

            if (mainCharacter.rect().colliderect(element_rect)):
                if rect_changes_scene:
                    self.change_scene(App, element[1])
                    match element[2]:
                        case 'l':
                            mainCharacter.position = [100, surf.get_height()/2]
                        case 'r':
                            mainCharacter.position = [100, surf.get_height()/2]
                        case 'u':
                            mainCharacter.position = [100, surf.get_height()/2]
                        case 'd':
                            mainCharacter.position = [100, surf.get_height()/2]

                    mainCharacter.lastFramePos = mainCharacter.position.copy()
                    return
                mainCharacter.position = mainCharacter.lastFramePos

    def change_scene(self, App, scene):
        print(scene)
        self.scene = scene