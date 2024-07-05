import pygame
from files.minigames.entity import Entity
from files.minigames.dummy import MinigameDummy
from files.minigames.scenes.save_them_scene import SaveThemScene

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
        
        # TODO CHANGE
        #self.fredbear.speed = 70

        self.puppet = Entity(App.assets.puppet_minigame, (self.surf_width/2, self.surf_height/2))
        self.puppet_state = 0

        self.sceneElements = SaveThemScene(App)
        self.scene = 5

        self.rooms = [
            self.sceneElements.room0_boundaries,
            self.sceneElements.room1_boundaries,
            self.sceneElements.room2_boundaries,
            self.sceneElements.room3_boundaries,
            self.sceneElements.room4_boundaries,
            self.sceneElements.room5_boundaries,
            self.sceneElements.room6_boundaries,
            self.sceneElements.room7_boundaries
        ]

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
        if (self.scene < len(self.rooms)):
            self.draw_boundaries(App, self.rooms[self.scene], self.fredbear)

            if self.isPuppetRoom(self.scene):
                self.draw_puppet(App)

    def draw_puppet(self, App):
        self.puppet.update(App)
        if (self.puppet_state == 0 and self.scene == 1):
            self.puppet.movement('u')

    def isPuppetRoom(self, scene):
        return (scene == 1 or scene == 2 or scene == 3)

    def change_scene(self, App, scene):
        super().change_scene(App, scene)

        puppet_init_pos = (self.surf_width/2, self.surf_height/2)
        match scene:
            case 1:
                if (self.puppet_state == 0):
                    self.puppet.position = list(puppet_init_pos)

    