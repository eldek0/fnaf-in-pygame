import pygame

class CreateScene:
    def __init__(self, App) -> None:
        self.surf_width, self.surf_height = App.surface.get_width(), App.surface.get_height()
        self.left_wall_size = 125
        self.up_wall_size = 75
        self.door_y_size = 150
        self.door_x_size = 350
        self.down_up_exit_hitbox = 250
        self.right_left_exit_hitbox = 100

    def left_wall(self, open=False)->tuple:
        if open:
            return ( 
                (pygame.Rect(0, 0, self.left_wall_size, self.door_y_size), (200, 200, 200)), 
                (pygame.Rect(0, self.surf_height - self.up_wall_size - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200))
            )

        return (pygame.Rect(0, 0, self.surf_width, self.up_wall_size), (200, 200, 200))
    
    def right_wall(self, open=False)->tuple:
        if open:
            return (
                (pygame.Rect(self.surf_width - self.left_wall_size, self.up_wall_size, self.left_wall_size, self.door_y_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.left_wall_size, self.surf_height - self.up_wall_size - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200))
            )
        return (pygame.Rect(self.surf_width - self.left_wall_size, 0, self.surf_height))
    
    def up_wall(self, open=False)->tuple:
        if open:
            return (
                (pygame.Rect(0, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, 0, self.door_x_size, self.up_wall_size), (200, 200, 200)),
            )
        
        return (pygame.Rect(0, 0, self.surf_width, self.up_wall_size), (200, 200, 200))
    
    def bottom_wall(self, open=False)->tuple:
        if open:
            return (
                (pygame.Rect(0, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
                (pygame.Rect(self.surf_width - self.door_x_size, self.surf_height - self.up_wall_size, self.door_x_size, self.up_wall_size), (200, 200, 200)),
            )
        
        return (pygame.Rect(self.surf_width - self.left_wall_size, self.surf_height - self.up_wall_size - self.door_y_size, self.left_wall_size, self.door_y_size), (200, 200, 200))