import pygame
from files.minigames.scenes.createScene import CreateScene

class SaveThemScene(CreateScene):

    def __init__(self, App):
        super().__init__(App)

        # BOUNDARIES
        # spawn
        self.room0_boundaries = self._clean_boundary( 
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(True, scene=1),
            self.bottom_wall(False),

            # Elements
            self.tables(App, left=False)
            ]
        )

        
        self.room1_boundaries =  self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(True, scene=2),
            self.left_wall(True, scene=0),
            self.right_wall(True, scene=10),
            self.bottom_wall(True, scene=11)
            ] 
        )

        self.room2_boundaries =  self._clean_boundary(
            [

            (App.assets.floor2, (0, 0), False),

            # Box
            self.up_wall(False),
            self.left_wall(True, scene=9),
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
            self.up_wall(True, 8),
            self.left_wall(True, scene=3),
            self.right_wall(False),
            self.bottom_wall(True, scene=5),

            # Elements
            self.tables(App, left=True)

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

        self.room8_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(True, 4),

            (App.assets.blood, (200, 260), False),
            (App.assets.sceneary, (200, 150))
            ] 
        )

        self.room9_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(True, 2),
            self.bottom_wall(False),

            (App.assets.suit2, (100, 170)),
            (App.assets.suit3, (120, 300)),
            (App.assets.suit4, (600, 110))
            ] 
        )

        self.room10_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(True, 1),

            self.tables(App, left=True)

            ] 
        )

        self.room11_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(True, 1),
            self.left_wall(True, 12),
            self.right_wall(True, 13),
            self.bottom_wall(True, 14),

            (App.assets.blood,(200, 200), False)

            ] 
        )

        self.room12_boundaries = self._clean_boundary( 
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(True, scene=11),
            self.bottom_wall(False),

            # Elements
            self.tables(App, left=False),
            (App.assets.sad_soul, (300, 600))
            ]
        )

        self.room13_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(True, 11),
            self.right_wall(False),
            self.bottom_wall(False),

            self.tables(App, left=True)

            ] 
        )

        self.room14_boundaries =  self._clean_boundary(
            [

            # Box
            self.up_wall(True, 11),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(False),

            (App.assets.desk_min, pygame.Rect(400, 380, 200, 100)),

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