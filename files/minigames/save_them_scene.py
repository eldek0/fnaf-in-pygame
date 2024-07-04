import pygame
from files.minigames.scenes import createScene

class SaveThemScene(createScene):

    def __init__(self, App) -> tuple:
        

        # BOUNDARIES
        left_wall_size = 125
        up_wall_size = 75
        door_y_size = 150
        door_x_size = 350
        down_up_exit_hitbox = 250
        right_left_exit_hitbox = 100

        room1_boundaries = [
            # Box
            (pygame.Rect(0, 0, self.surf_width, up_wall_size), (200, 200, 200)),
            (pygame.Rect(0, 0, left_wall_size, self.surf_height), (200, 200, 200)),
            (pygame.Rect(0, self.surf_height - up_wall_size, self.surf_width, up_wall_size), (200, 200, 200)),
            
            (pygame.Rect(self.surf_width - left_wall_size, up_wall_size, left_wall_size, door_y_size), (200, 200, 200)),
            (pygame.Rect(self.surf_width - left_wall_size, self.surf_height - up_wall_size - door_y_size, left_wall_size, door_y_size), (200, 200, 200)),

            # Elements
            (App.assets.table, pygame.Rect(200, 150, 350, 100)),
            (App.assets.table, pygame.Rect(200, 300, 350, 100)),

            # Exit
            (pygame.Rect(self.surf_width - 100, self.surf_height/2, 100, 50), 1, 'l')
        ]

        room2_boundaries = [
            # Box
            # Door up
            (pygame.Rect(0, 0, door_x_size, up_wall_size), (200, 200, 200)),
            (pygame.Rect(self.surf_width - door_x_size, 0, door_x_size, up_wall_size), (200, 200, 200)),
            
            # Door left
            (pygame.Rect(0, 0, left_wall_size, door_y_size), (200, 200, 200)),
            (pygame.Rect(0, self.surf_height - up_wall_size - door_y_size, left_wall_size, door_y_size), (200, 200, 200)),

            # Door down
            (pygame.Rect(0, self.surf_height - up_wall_size, door_x_size, up_wall_size), (200, 200, 200)),
            (pygame.Rect(self.surf_width - door_x_size, self.surf_height - up_wall_size, door_x_size, up_wall_size), (200, 200, 200)),

            # Door right
            (pygame.Rect(self.surf_width - left_wall_size, up_wall_size, left_wall_size, door_y_size), (200, 200, 200)),
            (pygame.Rect(self.surf_width - left_wall_size, self.surf_height - up_wall_size - door_y_size, left_wall_size, door_y_size), (200, 200, 200)),

            # Exit up
            (pygame.Rect(self.surf_width/2 - down_up_exit_hitbox/2, 0, down_up_exit_hitbox, up_wall_size),  2, 'l'),

            # Exit down
            (pygame.Rect(self.surf_width/2 - down_up_exit_hitbox/2, self.surf_height - up_wall_size, down_up_exit_hitbox, up_wall_size),  3, 'l'),

            # Exit right
            (pygame.Rect(self.surf_width - left_wall_size, self.surf_height/2 - right_left_exit_hitbox/2, left_wall_size, right_left_exit_hitbox),  4, 'l'),

            # Exit left
            (pygame.Rect(0, self.surf_height/2 - right_left_exit_hitbox/2, left_wall_size, right_left_exit_hitbox),  0, 'l'),
        ]