import pygame
from files.minigames.scenes.createScene import CreateScene

class SaveThemScene(CreateScene):

    def __init__(self, App) -> tuple:
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
            (App.assets.table, pygame.Rect(200, 150, 350, 100)),
            (App.assets.table, pygame.Rect(200, 300, 350, 100)),

            # Exit
            (pygame.Rect(self.surf_width - 100, self.surf_height/2, 100, 50), 1, 'l')
            ]
        )

        
        self.room1_boundaries =  self._clean_boundary(
            [
            # Box
            self.up_wall(True, scene=2),
            self.left_wall(True, scene=0),
            self.right_wall(True),
            self.bottom_wall(True)
            ] 
        )

        self.room2_boundaries =  self._clean_boundary(
            [
            # Box
            self.up_wall(False),
            self.left_wall(True, scene=1),
            self.right_wall(True),
            self.bottom_wall(True)
            ] 
        )

        self.room3_boundaries =  self._clean_boundary(
            [
            # Box
            self.up_wall(False),
            self.left_wall(True, scene=1),
            self.right_wall(True, scene=4),
            self.bottom_wall(True),

            ] 
        )

        self.room4_boundaries =  self._clean_boundary(
            [
            # Box
            self.up_wall(False),
            self.left_wall(True, scene=3),
            self.right_wall(False),
            self.bottom_wall(True)
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

        print(len(boundary_to_return))
        return boundary_to_return