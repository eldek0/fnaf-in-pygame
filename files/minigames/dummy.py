import pygame
from abc import ABC
from files.minigames.entity import Entity
from files.animations.sprites_animation import SpritesAnimation
from files.minigames.scenes.boundaries_exception import BoundException

class MinigameDummy(ABC):
    def __init__(self, App):
        self.ended:bool = False
        self.scene:int = 0

    def update(self, App):
        pass

    def key_movement(self, App):
        pass

    def jumpscare(self, App, animation:SpritesAnimation):
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).set_volume(1)
            pygame.mixer.Channel(0).play(App.assets.xScream1)
        if animation.sprite_num >= len(animation.sprites) - 1:
            self.ended = True
            pygame.mixer.Channel(0).stop()

        animation.update(App.uiSurface, App.deltaTime)

    def draw_boundaries(self, App, boundaries:list, mainCharacter:Entity, mainCharacterLayer=0):
        """ Will draw all the elements that the player can hit (or not) \n
        Each element goes between parentesis (). \n
        -- Sintax:\n 
        [0]: pygame.Surface, pygame.Rect or SpritesAnimation\n
        [1]: tuple(), if [0] is pygame.Surface or SpritesAnimation this will be the position, if [0] is pygame.Rect this will be the color, Represented by (R, G, B) If its None it will not draw it
        [2]: lambda object, will be called when the player's entity collides with the object. Can also be a special tuple that will have elements like the identificator and the arguments. 
                The current types are: - Change the scene: ("scene", 4, 'l') args=id, scene_to_change, direction ('r', 'l', 'u', 'd')\n
        [3]: bool(), whether the object can be hit or not. By default is True\n
        [4]: int(), layer of the object. By default is 0\n
        [5]: tuple(), hitbox initial position. By default is (0, 0)\n
        [6]: bool(), view object hitbox
        """

        surf = App.minigamesSurface
        index = 0
        objs_to_draw = []

        ordered_elements = {}
        try:
            # Check which layer the element has first (element[4])
            for element in boundaries:
                if (len(element) > 4 and not self.__check_is_default(element[4])):
                    layer = element[4]
                else:
                    layer = 0 # layer by default, higher the number higher the element will be
                if not layer in list(ordered_elements.keys()):
                    ordered_elements[layer] = []
                ordered_elements[layer].append(element)

            ordered_keys = list(ordered_elements.keys())
            ordered_keys.sort()

            # First calculate hitboxes
            for layer in ordered_keys:
                index = 0
                for element in ordered_elements[layer]:
                    element_rect = None
                    canHit = True
                    is_lambda_object = None
                    if isinstance(element[0], pygame.Surface):
                        if isinstance(element[1], pygame.Rect):
                            objs_to_draw.append(
                                lambda img=element[0], rect=element[1].copy(): surf.blit(img, (rect.x, rect.y))
                            )

                            element_rect = element[1]
                        elif isinstance(element[1], tuple):
                            objs_to_draw.append(
                                lambda img=element[0], pos=element[1]:surf.blit(img, pos)
                            )
                
                            element_rect = pygame.Rect(element[1][0], element[1][1], element[0].get_width(), element[0].get_height())
                        else:
                            raise BoundException("The [1] element must be a pygame.Rect or a tuple!", boundaries, index)
                        
                    elif isinstance(element[0], pygame.Rect):
                        element_rect = element[0]
                        color = element[1]
                        if not (color is None):
                            if not (isinstance(color, tuple)):
                                raise BoundException("The [1] element must be a (R, G, B) tuple!", boundaries, index)
                            
                            objs_to_draw.append(
                                lambda r=element_rect, c=color:pygame.draw.rect(surf, c, r)
                            )

                    elif isinstance(element[0], SpritesAnimation):
                        if isinstance(element[1], pygame.Rect):
                            element[0].position = [element[1].x, element[1].y]
                            element_rect = element[1]
                        elif isinstance(element[1], tuple):
                            spr_width, spr_height = element[0].sprites[0].get_width(), element[0].sprites[0].get_height()
                            pos = element[1]
                            element[0].position = pos
                            element_rect = pygame.Rect(pos[0], pos[1], spr_width, spr_height)
                        else:
                            raise BoundException("The [1] element must be a pygame.Rect or a tuple!", boundaries, index)
                        
                        objs_to_draw.append(
                            lambda anim=element[0], deltaTime=App.deltaTime:anim.update(surf, deltaTime)
                        )
                        

                    else:
                        raise BoundException("The [0] element must be pygame.Surface, pygame.Rect or SpritesAnimation!", boundaries, index)

                    # Detect if element[2] is a lambda object or a special tuple (and if its not None)
                    if (len(element) > 2 and element[2] and not self.__check_is_default(element[2]) ):
                        if (isinstance(element[2], tuple)): is_lambda_object = False # Is a special tuple
                        elif (isinstance(element[2], object)): is_lambda_object = True
                        else: raise BoundException("The [2] element must be a lambda object or a special tuple!", boundaries, index)

                    # Detect if element[3] (can be hit) is true or false (by default true):
                    if (len(element) > 3 and isinstance(element[3], bool) and not self.__check_is_default(element[3])):
                        canHit = element[3]

                    # Hitbox initial position
                    if (len(element) > 5 and isinstance(element[5], tuple) and not self.__check_is_default(element[5])):
                        ex, ey = element[5][0], element[5][1]
                        element_rect.x += ex
                        element_rect.width += ex
                        element_rect.y += ey
                        element_rect.height += ey

                    # See element hitbox
                    if (len(element) > 6 and isinstance(element[6], bool) and not self.__check_is_default(element[6])):
                        if (element[6]):
                            objs_to_draw.append(
                                lambda color=(0, 255, 0), rect=element_rect:self.draw_hitbox(App, color, rect)
                            )

                    if (mainCharacter.rect().colliderect(element_rect)):
                        if (is_lambda_object != None):
                            obj = element[2]
                            if (is_lambda_object):
                                obj()
                            else:
                                # Special tuple
                                tupleId = str(obj[0]).lower()
                                sceneToChange = int(obj[1])
                                dir = str(obj[2])
                                match tupleId:
                                    case "scene":
                                        self.__change_position(App, mainCharacter, sceneToChange, dir)
                        if canHit:  
                            mainCharacter.position = mainCharacter.lastFramePos
                            mainCharacter.update()
                    index += 1
                # Update the main character if its in the corresponding layer
                if (layer == mainCharacterLayer):
                    mainCharacter.update()
                    objs_to_draw.append(
                        lambda:mainCharacter.draw(App)
                    )
        
        except ValueError or IndexError as e:
            raise BoundException(e, boundaries, index)
        
        # Draw everything from the obj_to_draw list
        for draw in objs_to_draw:
            draw()

    def __change_position(self, App, mainCharacter:Entity, scene:int, dir:chr):
        surf = App.minigamesSurface
        surf_width, surf_height = surf.get_width(), surf.get_height()
        self.change_scene(App, scene)
        
        match dir:
            
            case 'l':
                mainCharacter.position = [90, mainCharacter.position[1]]
            case 'r':
                mainCharacter.position = [surf_width - 130*2, mainCharacter.position[1]]
            case 'u':
                mainCharacter.position = [mainCharacter.position[0], 10]
            case 'd':
                mainCharacter.position = [mainCharacter.position[0], surf_height - 130*2]


        mainCharacter.lastFramePos = mainCharacter.position.copy()

    def __check_is_default(self, element):return (str(element).lower() == "def")

    def draw_hitbox(self, App, color, rect):
        surf = App.uiSurface
        x = rect.x
        y = rect.y
        w = rect.width
        h = rect.height
        color = color
        pygame.draw.line(surf, color, (x, y), (x + w, y), 1)
        pygame.draw.line(surf, color, (x + w, y), (x + w, y + h), 1)
        pygame.draw.line(surf, color, (x, y), (x, y + h), 1)
        pygame.draw.line(surf, color, (x, y + h), (x + w, y + h), 1)


    def change_scene(self, App, scene):
        print(scene)
        self.scene = scene