import pygame, random
from files.minigames.entity import Entity
from files.minigames.dummy import MinigameDummy
from files.minigames.scenes.save_them_scene import SaveThemScene

class SAVETHEM(MinigameDummy):
    def __init__(self, App):
        super().__init__(App)
        self.surf_width, self.surf_height = App.surface.get_width(), App.surface.get_height()
        self.fredbear = Entity(
            texture = App.assets.freddy_walking[0], 
            initial_position = (self.surf_width/2 - App.assets.puppet_minigame.get_width()/2 + 100, self.surf_height/2 - App.assets.puppet_minigame.get_height()/2 - 50),
            walkingRightAnimation = App.animations.fredbear_walking1, 
            walkingDownAnimation = App.animations.fredbear_walking3, 
            walkingUpAnimation = App.animations.fredbear_walking2,
            hitboxDims=pygame.Rect(50, 20, 110, 170),
            speed=12
            )

        self.puppet = Entity(App.assets.puppet_minigame, (self.surf_width/2, self.surf_height/2), framesToMove=400, speed=40)
        self.puppet_state = 0

        self.sceneElements = SaveThemScene(App, self)

        self.suit = Entity(App.assets.suit_gr_1, (0, 0))
        self.suit.desactivate()
        self.show_suit = False
        self.timer = pygame.time.get_ticks()

        self.endo_anim_initial = (430, 460)
        self.endo_anim = Entity(App.animations.endoAnim, self.endo_anim_initial, speed=1)
        self.endo_anim_dir = 'r'

    def update(self, App):
        self.sceneElements.update(App, self.scene, self)

        self.draw_scene(App)

        if self.wasd_adv:
            App.minigamesSurface.blit(App.assets.wasd, (self.fredbear.position[0] - 50, self.fredbear.position[1] - 200))

        self.key_movement(App)

        self.update_abrupt_end()

    def key_movement(self, App):
        key = pygame.key.get_pressed()

        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.fredbear.movement('r')
            self.desactivate_wasd()
        
        elif (key[pygame.K_LEFT] or key[pygame.K_a]):
            self.fredbear.movement('l')
            self.desactivate_wasd()

        elif (key[pygame.K_UP] or key[pygame.K_w]):
            self.fredbear.movement('u')
            self.desactivate_wasd()

        elif (key[pygame.K_DOWN] or key[pygame.K_s]):
            self.fredbear.movement('d')
            self.desactivate_wasd()

    def draw_scene(self, App):
        rooms = self.sceneElements.rooms
        if (self.scene < len(rooms)):
            if self.show_suit:
                self.update_suit(App)
            else:
                self.suit.desactivate()
            
            # Add suit to rooms[self.scene]
            if self.suit.is_activated():
                rooms[self.scene].append(
                    (self.suit, None, lambda:self.suit_collide(), False, 0)
                )

            if (self.scene == 7):
                self.endo_anim.movement(self.endo_anim_dir)

                rooms[self.scene].append(
                    (self.endo_anim,None, None, True, 1, (0, 90), False)
                )
            
                if (self.endo_anim.position[0] > self.endo_anim_initial[0] + 40):
                    self.endo_anim_dir = 'l'
                elif (self.endo_anim.position[0] < self.endo_anim_initial[0] - 30):
                    self.endo_anim_dir = 'r'


            self.draw_boundaries(App, rooms[self.scene], self.fredbear)

            if self.isPuppetRoom(self.scene):
                self.draw_puppet(App)

    def draw_puppet(self, App):
        self.puppet.update()
        self.puppet.draw(App)
        if (self.puppet_state == 1 and self.scene == 1):
            self.puppet.movement('u')

        elif (self.puppet_state == 2 and self.scene == 2) or (self.puppet_state == 3 and self.scene == 3) or (self.puppet_state == 5 and self.scene == 5):
            self.puppet.movement('r')

        elif (self.puppet_state == 4 and self.scene == 4):
            self.puppet.movement('d')

    def isPuppetRoom(self, scene):
        return (scene == 1 or scene == 2 or scene == 3 or scene == 4 or scene == 5)

    def change_scene(self, App, scene):

        puppet_width, puppet_height = self.puppet.texture.get_width(), self.puppet.texture.get_height()

        puppet_init_pos = (self.surf_width/2 - puppet_width/2, self.surf_height/2 - puppet_height/2)

        if (self.isPuppetRoom(scene)):
            if (self.puppet_state == scene-1):
                self.puppet.position = list(puppet_init_pos)
                self.puppet_state += 1
            else:
                self.puppet.position = [-puppet_width, -puppet_height]

        super().change_scene(App, scene)

        if (random.randint(1, 100) < 5):
            self.show_suit = True
            self.suit.position = [random.randint(160, 850), random.randint(250, 630)]
        else:
            self.show_suit = False
    
    def update_suit(self, App):
        self.suit.activate()
        rect_size = (300, 300)
        size = (self.suit.rect().w, self.suit.rect().h)
        rectCollide = pygame.Rect(
            self.suit.position[0] - rect_size[0]/2 + size[0]/2, self.suit.position[1] - rect_size[1]/2 + size[1]/2, rect_size[0], rect_size[1]
            )

        if (self.fredbear.rect().colliderect(rectCollide)):
            self.suit.texture = App.assets.suit_gr_2
        else:
            self.suit.texture = App.assets.suit_gr_1
            
        self.suit.update()

    def suit_collide(self):
        if self.show_suit:self.show_suit = False

    def update_abrupt_end(self):
        # Every 30 seconds there is a 1/4 chance of finishing it
        if pygame.time.get_ticks() - self.timer > 30_000:
            if random.randint(1, 4) == 1:
                self.end_minigame()
            self.timer = pygame.time.get_ticks()

    