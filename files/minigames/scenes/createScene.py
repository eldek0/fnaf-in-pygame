import pygame

class CreateScene:
    def __init__(self, App):
        self.surf_width, self.surf_height = App.surface.get_width(), App.surface.get_height()
        self.left_wall_size = 125
        self.up_wall_size = 75
        self.door_y_size = 250
        self.door_x_size = 350
        self.down_up_exit_hitbox = 250
        self.right_left_exit_hitbox = 100
        self.down_up_exit_hitbox = 250
        self.right_left_exit_hitbox = 100

    def left_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(0, 0, self.left_wall_size, self.door_y_size), (200, 200, 200)), 
                (pygame.Rect(0, self.surf_height - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(-50, self.surf_height/2 - self.right_left_exit_hitbox/2, self.left_wall_size, self.right_left_exit_hitbox),  None, ("scene", scene, 'r')),
            )
        return (pygame.Rect(0, 0, self.left_wall_size, self.surf_height), (200, 200, 200))

    def right_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(self.surf_width - self.left_wall_size, 0, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.left_wall_size, self.surf_height - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width -  self.left_wall_size + 50, self.surf_height/2 -  self.right_left_exit_hitbox/2,  self.left_wall_size,  self.right_left_exit_hitbox),  None, ("scene", scene, 'l')),
            )
        return (pygame.Rect(self.surf_width - self.left_wall_size, 0, self.left_wall_size, self.surf_height), (200, 200, 200))

    def up_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(0, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width/2 - self.down_up_exit_hitbox/2, -50, self.down_up_exit_hitbox, self.up_wall_size),  None, ("scene", scene, 'd')),
            )
        return (pygame.Rect(0, 0, self.surf_width, self.up_wall_size), (200, 200, 200))

    def bottom_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(0, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width/2 -  self.down_up_exit_hitbox/2, self.surf_height -  self.up_wall_size + 50,  self.down_up_exit_hitbox,  self.up_wall_size),  None, ("scene", scene, 'u')),
            )
        return (pygame.Rect(0, self.surf_height - self.up_wall_size, self.surf_width, self.up_wall_size), (200, 200, 200))
    
    def tables(self, App, right:bool=True):
        separation = 170
        x1, x2, y = 150, 510, 100
        if right: 
            return (
                "<multiple>",
                (App.assets.table, pygame.Rect(x2, y, 350, 0), "def", "def", 1, (0, 100), True),
                (App.assets.table, pygame.Rect(x2, y + separation, 350, 100), "def", "def", 0, "def", True)
            )
    
        return (
                    "<multiple>",
                    (App.assets.table, pygame.Rect(x1, y, 350, 0), "def", "def", 1, (0, 100), True),
                    (App.assets.table, pygame.Rect(x1, y + separation, 350, 100), "def", "def", 0, "def", True)
                )
