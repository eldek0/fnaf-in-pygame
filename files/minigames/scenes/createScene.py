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
                (pygame.Rect(-50, self.surf_height/2 - self.right_left_exit_hitbox/2, self.left_wall_size, self.right_left_exit_hitbox),  scene, 'r'),
            )
        return (pygame.Rect(0, 0, self.left_wall_size, self.surf_height), (200, 200, 200))

    def right_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(self.surf_width - self.left_wall_size, 0, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.left_wall_size, self.surf_height - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width -  self.left_wall_size + 50, self.surf_height/2 -  self.right_left_exit_hitbox/2,  self.left_wall_size,  self.right_left_exit_hitbox),  scene, 'l'),
            )
        return (pygame.Rect(self.surf_width - self.left_wall_size, 0, self.left_wall_size, self.surf_height), (200, 200, 200))

    def up_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(0, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width/2 - self.down_up_exit_hitbox/2, -50, self.down_up_exit_hitbox, self.up_wall_size),  scene, 'd'),
            )
        return (pygame.Rect(0, 0, self.surf_width, self.up_wall_size), (200, 200, 200))

    def bottom_wall(self, open=False, scene=-1) -> tuple:
        if open:
            return (
                "<multiple>",
                (pygame.Rect(0, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width/2 -  self.down_up_exit_hitbox/2, self.surf_height -  self.up_wall_size + 50,  self.down_up_exit_hitbox,  self.up_wall_size),  scene, 'u'),
            )
        return (pygame.Rect(0, self.surf_height - self.up_wall_size, self.surf_width, self.up_wall_size), (200, 200, 200))
    
    def tables(self, App, left:bool=False):
        if not left:
            return (
                "<multiple>",
                (App.assets.table, pygame.Rect(200, 150, 350, 100)),
                (App.assets.table, pygame.Rect(200, 300, 350, 100))
            )
        
        return (
            "<multiple>",
            (App.assets.table, pygame.Rect(400, 150, 350, 100)),
            (App.assets.table, pygame.Rect(400, 300, 350, 100))
        )
