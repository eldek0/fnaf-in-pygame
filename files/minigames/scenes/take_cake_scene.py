import pygame
from files.minigames.scenes.createScene import CreateScene
from files.minigames.entity import Entity

class TakeCakeToTheChildrenScene(CreateScene):

    def __init__(self, App, root):
        super().__init__(App)
        self.rooms = {}
        self.update(App, 0, root)
    
    def update(self, App, scene, root, *args):
        y_margin_up = 200
        y_margin_down = 130
        x_margin = 100
        wall_width = 30
        door_pos = 180
        door_size = 120
        self._clean_boundary(
            [
            # Box
            (pygame.Rect(x_margin, y_margin_up, door_pos, wall_width), (255, 255, 255)), # Horizontal up left
            (pygame.Rect(x_margin + door_pos, y_margin_up + wall_width/6, door_size, wall_width/2), (150, 150, 200)), # DOOR
            (pygame.Rect(x_margin + door_pos + door_size, y_margin_up, self.surf_width - x_margin*2 - door_pos - door_size, wall_width), (255, 255, 255)), # Horizontal up right

            (pygame.Rect(x_margin, y_margin_up, wall_width, self.surf_height - y_margin_down*2 - wall_width*2), (255, 255, 255)), # Vertical left
            (pygame.Rect(x_margin, self.surf_height - y_margin_down, self.surf_width - x_margin*2, wall_width), (255, 255, 255)), # Horizontal down
            (pygame.Rect(self.surf_width - x_margin - wall_width, y_margin_up, wall_width, self.surf_height - y_margin_down*2 - wall_width*2), (255, 255, 255)) # Vertical right

            ], scene
        )