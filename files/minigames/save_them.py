import pygame
from files.minigames.entity import Entity
from files.minigames.dummy import MinigameDummy

class SAVETHEM(MinigameDummy):
    def __init__(self, App):
        super().__init__(App)
        self.surf_width, self.surf_height = App.surface.get_width(), App.surface.get_height()
        self.fredbear = Entity(
            texture = App.assets.freddy_walking[0], 
            initial_position = (self.surf_width/2 - App.assets.puppet_minigame.get_width()/2 + 100, self.surf_height/2 - App.assets.puppet_minigame.get_height()/2),
            walkingRightAnimation = App.animations.fredbear_walking1, 
            walkingDownAnimation = App.animations.fredbear_walking3, 
            walkingUpAnimation = App.animations.fredbear_walking2,
            hitboxDims=pygame.Rect(50, 20, 110, 170)
            )
        self.puppet = Entity(App.assets.puppet_minigame, (self.surf_width/2, self.surf_height/2))

    def update(self, App):
        self.draw_scene(App)

        self.fredbear.update(App)

        self.key_movement(App)

        #self.fredbear.show_rect(App)

    def key_movement(self, App):
        key = pygame.key.get_pressed()

        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.fredbear.movement('r')
        
        elif (key[pygame.K_LEFT] or key[pygame.K_a]):
            self.fredbear.movement('l')

        elif (key[pygame.K_UP] or key[pygame.K_w]):
            self.fredbear.movement('u')

        elif (key[pygame.K_DOWN] or key[pygame.K_s]):
            self.fredbear.movement('d')

    def draw_scene(self, App):
        surf = App.minigamesSurface
        match self.scene:
            case 0:
                # Floor
                surf.blit(App.assets.floor1, (0, 0))
                self.draw_boundaries(App, self.room1_boundaries, self.fredbear)

            case 1:
                # Floor
                surf.blit(App.assets.floor2, (0, 0))
                self.draw_boundaries(App, self.room2_boundaries, self.fredbear)
                self.draw_puppet(App)

    def draw_puppet(self, App):
        self.puppet.update(App)
        self.puppet.movement('u')

    