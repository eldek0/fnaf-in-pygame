import pygame
from files.minigames.entity import Entity
from files.minigames.dummy import MinigameDummy
from files.minigames.scenes.foxy_go_scene import FoxyGoGoScene

class FoxyGoGo(MinigameDummy):
    def __init__(self, App):
        super().__init__(App)
        self.foxy = Entity(App.animations.foxy_anim, (300, 200))
        
        self.childs = [
            Entity(App.assets.happy_child, (600, 160)),
            Entity(App.assets.happy_child, (543, 260)),
            Entity(App.assets.happy_child, (543, 336)),
            Entity(App.assets.happy_child, (750, 440)),
            Entity(App.assets.happy_child, (600, 510))
        ]

        self.reset_vals(App)

        #self.scene = 1 # unescesary TODO

        self.game_status = 0

        self.sceneElements = FoxyGoGoScene(App, self)

        self.texts = [
            App.assets.get_ready_txt,
            App.assets.go_txt,
            App.assets.hurray_txt
        ]

    def reset_vals(self, App):
        self.confetti_updating = []
        self.scene = 0
        self.foxy.position = [450, 200]
        self.conf_index = 0
        self.conf_timer = pygame.time.get_ticks()
        self.text_index = 0

        self.canWalk = False
        self.timer = pygame.time.get_ticks()
        self.text_shown = True

        self.bool_draw_game_status = False
        self.finished_status = False

        for anim in App.animations.confs_animation2:
            anim.reset()

    def update(self, App):
        self.sceneElements.update(App, self.scene, self)
        self.draw_scene(App)

        if (self.canWalk):
            self.key_movement(App)

        else:
            if pygame.time.get_ticks() - self.timer > 5000:
                self.canWalk = True
                self.text_index = 1

        if (self.finished_status):
            self.change_state(App)

    def draw_scene(self, App):
        rooms = self.sceneElements.rooms
        if self.scene == 1:
            for child in self.childs:
                rooms[1].append(
                    (child.texture, tuple(child.position), lambda:self.collided_child(App), False)
                )

        if (self.game_status == 2 and self.scene == 0):
            rooms[0].append(
                (App.assets.purple_guy, (140, 450), None, False)
            )

        if (self.scene < len(rooms)):
            self.draw_boundaries(App, rooms[self.scene], self.foxy)

        if self.bool_draw_game_status:
            self.draw_game_status(App)
        pos = (App.surface.get_width()/2 - self.texts[self.text_index].get_width()/2, 10)

        if (self.text_index == 1):
            if (pygame.time.get_ticks() - self.conf_timer > 100):
                if self.text_shown: self.text_shown = False
                else: self.text_shown = True
                self.conf_timer = pygame.time.get_ticks()
        else:
            self.text_shown = True
        
        if self.text_shown:
            App.minigamesSurface.blit(self.texts[self.text_index], pos)

    def key_movement(self, App):
        key = pygame.key.get_pressed()

        if (key[pygame.K_RIGHT] or key[pygame.K_d]):
            self.foxy.movement('r')
        
        elif (key[pygame.K_LEFT] or key[pygame.K_a]):
            self.foxy.movement('l')

        elif (key[pygame.K_UP] or key[pygame.K_w]):
            self.foxy.movement('u')

        elif (key[pygame.K_DOWN] or key[pygame.K_s]):
            self.foxy.movement('d')

    def draw_confetti(self, App):
        for c_data in self.confetti_updating:
            confetti = c_data[0]
            timer = c_data[1]
            if confetti.sprite_num >= len(confetti.sprites)-1:
                if (pygame.time.get_ticks() - timer > 1500):
                    self.confetti_updating.remove(c_data)
            else:
                timer = pygame.time.get_ticks()
            confetti.update(App.surface, App.deltaTime)
        
        if self.confetti_updating == [] and self.conf_index > 1:
            self.finished_status = True

    def draw_game_status(self, App):
        if self.game_status == 0 or self.game_status == 1:
            self.canWalk = False
            if pygame.time.get_ticks() - self.conf_timer > 500:
                if (self.conf_index < len(App.animations.confs_animation2)):
                    self.confetti_updating.append(
                        [App.animations.confs_animation2[self.conf_index], pygame.time.get_ticks()]
                        )
                    self.conf_index += 1
                    self.conf_timer = pygame.time.get_ticks()
                    pygame.mixer.Channel(1).play(App.assets.pop)

            self.draw_confetti(App)

        elif self.game_status == 2:
            self.foxy.speed = 5
            
                

    def change_state(self, App):
        self.reset_vals(App)
        self.game_status += 1
        if (self.game_status == 2):
            for child in self.childs:
                child.texture = App.assets.sad_child

    def change_draw_bool(self, state):
        self.bool_draw_game_status = state
        if self.game_status != 2:
            self.text_index = 2

    def collided_child(self, App):
        self.canWalk = False
        self.jumpscare(App, App.animations.foxy_jump)
