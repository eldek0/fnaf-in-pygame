import pygame
from files.minigames.scenes.createScene import CreateScene

class SaveThemScene(CreateScene):

    def __init__(self, App):
        super().__init__(App)
        self.rooms = []

        # BOUNDARIES
        # spawn
        ### ROOM 0 ###
        self._clean_boundary( 
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(True, scene=1),
            self.bottom_wall(False),

            # Elements
            self.tables(App, left=False),
            (App.assets.sad_soul, (650, 600), "def", "def", "def", "def", True)
            ]
        )

         ### ROOM 1 ###
        self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), None, False),

            # Box
            self.up_wall(True, scene=2),
            self.left_wall(True, scene=0),
            self.right_wall(True, scene=10),
            self.bottom_wall(True, scene=11)
            ] 
        )

         ### ROOM 2 ###
        self._clean_boundary(
            [

            (App.assets.floor1, (0, 0), None, False),

            # Box
            self.up_wall(False),
            self.left_wall(True, scene=9),
            self.right_wall(True, scene=3),
            self.bottom_wall(True, scene=1)
            ] 
        )

         ### ROOM 3 ###
        self._clean_boundary(
            [

            (App.assets.floor1, (0, 0), None, False),
            
            # Box
            self.up_wall(False),
            self.left_wall(True, scene=2),
            self.right_wall(True, scene=4),
            self.bottom_wall(False),

            (App.assets.dust, (100, 200), None, False),
            (App.assets.dust, (300, 500), None, False),
            (App.assets.sad_soul, (650, 600))

            ] 
        )

         ### ROOM 4 ###
        self._clean_boundary(
            [
            (App.assets.floor1, (0, 0), None, False),

            # Box
            self.up_wall(True, 8),
            self.left_wall(True, scene=3),
            self.right_wall(False),
            self.bottom_wall(True, scene=5),

            # Elements
            self.tables(App, left=True)

            ] 
        )

         ### ROOM 5 ###
        self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), None, False),

            # Box
            self.up_wall(True, scene=4),
            self.left_wall(False),
            self.right_wall(True, scene=6),
            self.bottom_wall(True, scene=7),

            # Elements
            (App.assets.blood, (150, 200), None, False),
            (App.assets.blood, (410, 400), None, False),

            ] 
        )

         ### ROOM 6 ###
        self._clean_boundary(
            [
            (App.assets.floor1, (0, 0), None, False),

            # Box
            self.up_wall(False),
            self.left_wall(True, scene=5),
            self.right_wall(False),
            self.bottom_wall(False),

            # Elements
            (App.assets.blood, (440, 410), None, False),
            (App.assets.bigGift, pygame.Rect(440, 260, 350, 200)),

            (pygame.transform.flip(App.assets.sad_soul, True, False), (390, 500)),

            ] 
        )

         ### ROOM 7 ###
        self._clean_boundary(
            [
            (App.assets.floor2, (0, 0), None, False),

            # Box
            self.up_wall(True, 5),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(False),

            (App.animations.endoAnim, (300, 460))
            ] 
        )

         ### ROOM 8 ###
        self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(False),
            self.right_wall(False),
            self.bottom_wall(True, 4),

            (App.assets.blood, (200, 360), None, False),
            (App.assets.sceneary, (200, 100)),
            (App.assets.sad_soul, (120, 500))
            ] 
        )

         ### ROOM 9 ###
        self._clean_boundary(
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

         ### ROOM 10 ###
        self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(True, 1),
            self.right_wall(False),
            self.bottom_wall(False),

            self.tables(App, left=True)

            ] 
        )

         ### ROOM 11 ###
        self._clean_boundary(
            [

            # Box
            self.up_wall(True, 1),
            self.left_wall(True, 12),
            self.right_wall(True, 13),
            self.bottom_wall(True, 14),

            (App.assets.blood,(200, 200), None, False)

            ] 
        )

         ### ROOM 12 ###
        self._clean_boundary( 
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

         ### ROOM 13 ###
        self._clean_boundary(
            [

            # Box
            self.up_wall(False),
            self.left_wall(True, 11),
            self.right_wall(False),
            self.bottom_wall(False),

            self.tables(App, left=True)

            ] 
        )

         ### ROOM 14 ###
        self._clean_boundary(
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

        ### Add the boundary to the list
        self.rooms.append(boundary_to_return)