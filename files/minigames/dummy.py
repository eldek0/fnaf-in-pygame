import pygame
from abc import ABC
from files.minigames.entity import Entity
from files.animations.sprites_animation import SpritesAnimation

class MinigameDummy(ABC):
    def __init__(self, App):
        self.ended:bool = False
        self.scene:int = 0

    def update(self, App):
        pass

    def key_movement(self, App):
        pass

    def draw_boundaries(self, App, boundaries:list, mainCharacter:Entity, mainCharacterLayer=0):
        """ Will draw all the elements that the player can hit (or not) \n
        Each element goes between parentesis (). Sintax:\n 
        [0]: pygame.Surface, pygame.Rect or SpritesAnimation\n
        [1]: int() means when touched will change to that scene (only when [0] is pygame.Rect)\n 
        [2]: bool(), whether the object can be hit or not
        [3]: int(), layer of the object
        """

        surf = App.minigamesSurface
        surf_width, surf_height = surf.get_width(), surf.get_height()

        ordered_elements = {}

        # Check which layer the element has first (4th list component)
        for element in boundaries:
            if (len(element) > 4):
                layer = element[3]
                element = tuple(list(element).pop(4)) # Remove the layer component
            else:
                layer = 0 # layer by default, higher the number higher the element will be
            if not layer in list(ordered_elements.keys()):
                ordered_elements[layer] = []
            ordered_elements[layer].append(element)

        ordered_keys = list(ordered_elements.keys())
        ordered_keys.sort()

        for layer in ordered_keys:
            for element in ordered_elements[layer]:
                element_rect = None
                rect_changes_scene = False
                canHit = True
                if isinstance(element[0], pygame.Surface):
                    if isinstance(element[1], pygame.Rect):
                        surf.blit(element[0], (element[1].x, element[1].y))
                        element_rect = element[1]
                    else:
                        surf.blit(element[0], element[1])
                        element_rect = pygame.Rect(element[1][0], element[1][1], element[0].get_width(), element[0].get_height())
                    
                elif isinstance(element[0], pygame.Rect):
                    element_rect = element[0]
                    if (isinstance(element[1], int)): # Changes scene
                        rect_changes_scene = True
                    elif (isinstance(element[1], tuple)):
                        pygame.draw.rect(surf, element[1], element[0])

                elif isinstance(element[0], SpritesAnimation):
                    if isinstance(element[1], pygame.Rect):
                        element[0].position = [element[1].x, element[1].y]
                        element_rect = element[1]
                    elif isinstance(element[1], tuple):
                        spr_width, spr_height = element[0].sprites[0].get_width(), element[0].sprites[0].get_height()
                        pos = element[1]
                        element[0].position = pos
                        element_rect = pygame.Rect(pos[0], pos[1], spr_width, spr_height)
                    element[0].update(surf, App.deltaTime)

                # If the third component is a boolean:
                if (len(element) >= 3 and isinstance(element[2], bool)):
                    canHit = element[2]
                    rect_changes_scene = False

                """if rect_changes_scene:
                    pygame.draw.rect(App.uiSurface, (200, 200, 100), element_rect)"""

                if (mainCharacter.rect().colliderect(element_rect) and canHit):
                    if rect_changes_scene:
                        if element[1] != -1:
                            self.change_scene(App, element[1])
                        match element[2]:
                            case 'l':
                                mainCharacter.position = [90, mainCharacter.position[1]]
                            case 'r':
                                mainCharacter.position = [surf_width - 130*2, mainCharacter.position[1]]
                            case 'u':
                                mainCharacter.position = [mainCharacter.position[0], 10]
                            case 'd':
                                mainCharacter.position = [mainCharacter.position[0], surf_height - 130*2]

                        mainCharacter.lastFramePos = mainCharacter.position.copy()
                        return
                    mainCharacter.position = mainCharacter.lastFramePos

            # Update the main character if its in the corresponding layer
            if (layer == mainCharacterLayer):
                mainCharacter.update(App)

    def change_scene(self, App, scene):
        print(scene)
        self.scene = scene