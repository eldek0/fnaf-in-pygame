import pygame
from files.minigames.scenes.createScene import CreateScene
from files.minigames.entity import Entity

class FoxyGoGoScene(CreateScene):

    def __init__(self, App, root):
        super().__init__(App)
        self.rooms = {}
        for i in range(2):
            self.update(App, i, root)
    
    def update(self, App, scene, root, *args):

        surf_width = App.surface.get_width()
        surf_height = App.surface.get_height()
        x_margin = 30
        y_margin = 100
        y_down_margin = 20
        wall_width = 30
        small_wall_x = 900
        small_wall_y_size = 300
        match scene:
            case 0:
                # spawn
                ### ROOM 0 ###
                self._clean_boundary( 
                    [
                    (pygame.Rect(x_margin, y_margin, wall_width, surf_height - y_down_margin), (255, 255, 255)),
                    (pygame.Rect(x_margin, y_margin, surf_width, wall_width), (255, 255, 255)),
                    (pygame.Rect(x_margin, surf_height - y_down_margin - wall_width, surf_width, 50), (255, 255, 255)),

                    (pygame.Rect(x_margin + small_wall_x, y_margin, wall_width, small_wall_y_size), (255, 255, 255)),

                    # Door to change room
                    (pygame.Rect(surf_width-50, y_margin + small_wall_y_size, 100, 600),  None, ("scene", 1, 'l')),

                    # Elements
                    (App.assets.courtain, (200, y_margin + wall_width), "def", False),
                    (App.assets.courtain, (600, y_margin + wall_width), "def", False)
                    ], scene
                )

            case 1:
                ### ROOM 1 ###
                toadd = [
                    (pygame.Rect(surf_width - x_margin - wall_width, y_margin, wall_width, surf_height - y_down_margin), (255, 255, 255)),
                    (pygame.Rect(0, y_margin, surf_width - x_margin, wall_width), (255, 255, 255)), # HORIZONTAL UP
                    (pygame.Rect(0, surf_height - y_down_margin - wall_width, surf_width - x_margin, 50), (255, 255, 255)), # horizontal down

                    (pygame.Rect(x_margin + 40, y_margin, wall_width, small_wall_y_size), (255, 255, 255)),

                    # Trigger to make events happen
                    (pygame.Rect(300, 0, 50, 1000), None, lambda:root.change_draw_bool(True), False)
                    ]
                
                if len(args) > 0:
                    for c in args[0]:
                        child:Entity = c
                        toadd.append(
                            (child.texture, tuple(child.position), "def", False)
                        )

                self._clean_boundary( 
                    toadd, scene
                )