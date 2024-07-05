import pygame
from files.minigames.scenes.createScene import CreateScene

class SaveThemScene(CreateScene):

    def __init__(self, App) -> tuple:
        super().__init__(App)

        # BOUNDARIES
        # spawn
        self.room0_boundaries = self._clean_boundary( 
            [
            (App.assets.floor1, (0, 0), False),

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(True, scene=1),
            self.bottom_wall(False),

            # Elements
            (App.assets.table, pygame.Rect(200, 150, 350, 100)),
            (App.assets.table, pygame.Rect(200, 300, 350, 100))
            ]
        )

        
        self.room1_boundaries =  self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(True, scene=2),
            self.left_wall(True, scene=0),
            self.right_wall(True),
            self.bottom_wall(True)
            ] 
        )

        self.room2_boundaries =  self._clean_boundary(
            [

            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(False),
            self.left_wall(True),
            self.right_wall(True, scene=3),
            self.bottom_wall(True, scene=1)
            ] 
        )

        self.room3_boundaries =  self._clean_boundary(
            [

            (App.assets.floor2, (0, 0), False),
            
            # Box
            self.up_wall(False),
            self.left_wall(True, scene=2),
            self.right_wall(True, scene=4),
            self.bottom_wall(True),

            (App.assets.dust, (100, 200), False),
            (App.assets.dust, (300, 500), False),
            (App.assets.sad_soul, (400, 400))

            ] 
        )

        self.room4_boundaries =  self._clean_boundary(
            [
            (App.assets.floor1, (0, 0), False),

            # Box
            self.up_wall(False),
            self.left_wall(True, scene=3),
            self.right_wall(False),
            self.bottom_wall(True, scene=5),

            # Elements
            (App.assets.table, pygame.Rect(400, 250, 350, 100)),
            (App.assets.table, pygame.Rect(400, 300, 350, 100)),

            ] 
        )

        self.room5_boundaries =  self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(True, scene=4),
            self.left_wall(False),
            self.right_wall(True, scene=6),
            self.bottom_wall(True, scene=7),

            # Elements
            (App.assets.blood, (150, 200), False),
            (App.assets.blood, (410, 400), False),

            ] 
        )

        self.room6_boundaries =  self._clean_boundary(
            [
            (App.assets.floor1, (0, 0), False),

            # Box
            self.up_wall(False),
            self.left_wall(True, scene=5),
            self.right_wall(False),
            self.bottom_wall(False),

            # Elements
            (App.assets.blood, (440, 410), False),
            (App.assets.bigGift, pygame.Rect(440, 260, 350, 200)),

            (pygame.transform.flip(App.assets.sad_soul, True, False), (390, 500)),

            ] 
        )

        self.room7_boundaries =  self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(True, 5),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(False),

            (App.animations.endoAnim, (300, 460))
            ] 
        )


    def _clean_boundary(self, boundary):
        boundary_to_return = []
        for element in boundary:
            if (isinstance(element[0], str) and str(element[0]).lower() == "<multiple>"):
                for e in element[1:]:
                    boundary_to_return.append(e)
            else:
                boundary_to_return.append(element)

        return boundary_to_return